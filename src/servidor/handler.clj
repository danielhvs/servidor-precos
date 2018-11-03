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
            [ring.middleware.defaults :refer [wrap-defaults api-defaults]])
  (:import org.bson.types.ObjectId)
)

;; Banco
(defn conecta-bd []
  (let [uri "mongodb://user-mercado:M3rc4d0*@ds237723.mlab.com:37723/mercado"] 
    (mg/connect-via-uri uri)))

(defn db-consulta-produto [db query]
  (mc/find-maps db "produtos" query))

(defn db-consulta-mercado [db nome]
  (mc/find-maps (:db (conecta-bd)) "mercado" {:nome nome}))

(defn update-mercado [db p]
  (when (empty? (db-consulta-mercado db (:nome p)))  
    (let [m {:nome (:nome p) :comprar true :estoque 0}]
      (mc/insert (:db (conecta-bd)) "mercado" m))))

;; Utils
(defn _merge [table-a table-b]
  (->> (concat table-a table-b)  ;; stat with all the data
       (sort-by :nome)           ;; split it into groups
       (partition-by :nome)      ;; by produto
       (map (partial apply merge))  ;; merge each group into a single map.
))

(defn filtra-produto [nome colecao] 
  (filter (fn [p] (= nome (:nome p))) colecao))

(defn transforma-id-para-string [chave valor]
  (if (= chave :_id) (str (ObjectId.)) valor))

;; Servicos
(defn consulta-mercado []
  (-> (r/response (json/write-str (mc/find-maps (:db (conecta-bd)) "mercado") :value-fn transforma-id-para-string))
      (r/header  "Access-Control-Allow-Origin" "*")))

(defn consulta [nome]
  (let [db (:db (conecta-bd))]
    (-> (r/response (json/write-str (db-consulta-produto db {:nome nome}) :value-fn transforma-id-para-string))
        (r/header "Access-Control-Allow-Origin" "*"))))

(defn consulta-produtos []
  (let [db (:db (conecta-bd))]
    (-> (r/response (json/write-str (db-consulta-produto db {}) :value-fn transforma-id-para-string))
        (r/header "Access-Control-Allow-Origin" "*"))))

(defn salva-mercado [request]
  (-> (r/response
       (dosync (let [db (:db (conecta-bd))
                     m (json/read-str (slurp (:body request)) :key-fn keyword)
                     todo-mercado (mc/find-maps db "mercado")
                     resultado (_merge todo-mercado m)]
                 (mc/remove db "mercado")
                 (mc/insert-batch db "mercado" resultado)
                 (json/write-str (mc/find-maps db "mercado") :value-fn transforma-id-para-string))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn cadastra [request]
  (-> (r/response
       (dosync (let [p-request (json/read-str (slurp (:body request)) :key-fn keyword)
                     p (assoc p-request :data (str (t/local-date)))
                     db (:db (conecta-bd))]
                 (update-mercado db p)
                 (json/write-str (mc/insert-and-return db "produtos" p) :value-fn transforma-id-para-string))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn opcoes []
  (-> (r/response "")
      (r/header "Access-Control-Allow-Origin" "*")
      (r/header "Allow" "POST")
      (r/header "Access-Control-Allow-Methods" "POST")
      (r/header "Access-Control-Allow-Headers" "content-type")))

;; Rotas
(defroutes app-routes
  (GET "/" [] "Hello World")
  (GET "/consulta/:nome" [nome] (consulta nome))
  (GET "/consulta" [] (consulta-produtos))
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
