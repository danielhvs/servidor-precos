(ns servidor.handler
  (:require [compojure.core :refer :all]
            [compojure.handler :refer [site]]
            [clojure.data.json :as json]
            [java-time :as t]
            [compojure.route :as route]
            [ring.adapter.jetty :as jetty]
            [ring.util.response :as r]
            [monger.core :as mg]
            [monger.collection :as mc]
            [environ.core :refer [env]]
            [ring.middleware.cors :refer [wrap-cors]]
            [ring.middleware.defaults :refer [wrap-defaults api-defaults]]))

;; FIXME: manter conectado
(defn conecta-bd []
  (let [uri "mongodb://user-mercado:M3rc4d0*@ds237723.mlab.com:37723/mercado"] 
    (mg/connect-via-uri uri)))

(defn filtra-produto [nome colecao] 
  (filter (fn [p] (= nome (:produto p))) colecao))

(defn transforma-id-para-string [chave valor]
  (if (= chave :_id) "id" valor))

;; FIXME: definir nomenclatura para servico
(defn consulta-mercado 
  ([]
   (-> (r/response (json/write-str (mc/find-maps (:db (conecta-bd)) "mercado") :value-fn transforma-id-para-string))
       (r/header  "Access-Control-Allow-Origin" "*")))
  ([nome]
   (mc/find-maps (:db (conecta-bd)) "mercado" {:produto nome})))

(defn consulta-produto [nome]
  (mc/find-maps (:db (conecta-bd)) "produtos" {:produto nome}))

(defn consulta [nome]
  (-> (r/response (json/write-str (consulta-produto nome) :value-fn transforma-id-para-string))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn _merge [table-a table-b]
  (->> (concat table-a table-b)     ;; stat with all the data
       (sort-by :produto)           ;; split it into groups
       (partition-by :produto)      ;; by produto
       (map (partial apply merge))  ;; merge each group into a single map.
))


(defn salva-mercado [request]
  (-> (r/response
       (dosync (let [db (:db (conecta-bd))
                     m (json/read-str (slurp (:body request)) :key-fn keyword)
                     todo-mercado (mc/find-maps db "mercado")
                     resultado (_merge todo-mercado m)]
                (mc/remove db "mercado")
                (mc/insert-batch "mercado" resultado))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn update-mercado [p]
  (when (empty? (consulta-mercado (:produto p)))  
    (let [m {:produto (:produto p) :comprar true}]
      (mc/insert (:db (conecta-bd)) "mercado" m))))

;; FIXME: adicionar data no bd
(defn cadastra [request]
  (-> (r/response
       (dosync (let [p (json/read-str (slurp (:body request)) :key-fn keyword)]
                 #_(swap! produtos conj (assoc p :data (str (t/local-date))))
                 (update-mercado p)
                 (json/write-str (mc/insert-and-return (:db (conecta-bd)) "produtos" p) :value-fn transforma-id-para-string))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn opcoes []
  (-> (r/response "")
      (r/header "Access-Control-Allow-Origin" "*")
      (r/header "Allow" "POST")
      (r/header "Access-Control-Allow-Methods" "POST")
      (r/header "Access-Control-Allow-Headers" "content-type")))

(defroutes app-routes
  (GET "/" [] "Hello World")
  (GET "/consulta/:produto" [produto] (consulta produto))
  (GET "/consulta-mercado" [] (consulta-mercado))
  (POST "/cadastra" request (cadastra request))
  (POST "/salva-mercado" request (salva-mercado request))
  (OPTIONS "/cadastra" request (opcoes))
  (OPTIONS "/salva-mercado" request (opcoes))
  (route/not-found "Not Found"))

(defn wrap-debug [handler]
  (fn [request]
    (do
      (println "REQUEST: " request)
      (let [response (handler request)]
        (do (println "RESPONSE: " response)
            response)))))

(def app
  (wrap-debug
   (wrap-cors 
    (wrap-defaults app-routes api-defaults) 
    :access-control-allow-origin [#".*"])))

(defn -main [& [port]]
  (let [port (Integer. (or port (env :port) 3000))]
    (jetty/run-jetty (site #'app) {:port port :join? false})))

; https://mlab.com
