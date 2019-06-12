(ns servidor.handler
  (:require [compojure.core :refer :all]
            [compojure.handler :refer [site]]
            [clojure.data.json :as json]
            [clojure.string :as string]
            [java-time :as t]
            [compojure.route :as route]
            [ring.adapter.jetty :as jetty]
            [ring.util.response :as r]
            [monger.core :as mg]
            [monger.collection :as mc]
            [environ.core :refer [env]]
            [monger.operators :refer :all]
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
  (mc/find-maps db "mercado" {:nome nome}))

(defn db-remove-tudo [db nome]
  (mc/remove db nome))

(defn update-mercado [db {:keys [nome preco local data]}]
  (let [m-banco (db-consulta-mercado db nome)]  
    (if (empty? m-banco)
        (let [m {:nome nome :comprar true :estoque 0 :preco preco :local local :data data}]
          (mc/insert (:db (conecta-bd)) "mercado" m))
        (let [mais-barato (if (< preco (:preco (first m-banco))) 
                            {:preco preco :local local :data data} 
                            (first m-banco))
              m {:preco (:preco mais-barato) :local (:local mais-barato) :data (:data mais-barato)}]
          (mc/update-by-id db "mercado" (:_id (first m-banco)) {$set m})))))

;; Utils
(defn normaliza [nome]
  "Faz kebab-case e remove 'de'"
  (let [palavras
        (filter #(and (not (empty? %)))
                (map string/lower-case (string/split nome #" ")))]
    (string/replace 
     (reduce #(str %1 "-" %2) palavras)
     #"-de-"
     "-")))

(defn transforma-valor-request [chave valor]
  (cond 
   (= chave :preco) (Float/valueOf valor) 
   (= chave :nome) (normaliza valor) 
   :else valor))

(defn parse-request-cadastro [json]
  (json/read-str (slurp json) :key-fn keyword :value-fn transforma-valor-request))

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

(defn transforma-preco [chave valor]
  (if (= chave :preco) (Float/valueOf valor) valor))



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

(defn remove-tudo []
  (let [db (:db (conecta-bd))]
    (db-remove-tudo db "mercado")
    (db-remove-tudo db "produtos")
    (-> (r/response "Removido")
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

(defn boot-mercado [request]
  (-> (r/response
       (dosync (let [db (:db (conecta-bd))
                     todo-mercado (json/read-str (slurp (:body request)) :key-fn keyword)
                     tudo (map #(assoc % :local "nenhum" :preco 99999999 :nome (normaliza (:nome %))) todo-mercado)]
                 (mc/insert-batch db "mercado" tudo)
                 (json/write-str (mc/find-maps db "mercado") :value-fn transforma-id-para-string))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn cadastra [request]
  (-> (r/response
       (dosync (let [p-request (parse-request-cadastro (:body request))
                     p (assoc p-request :data (str (t/local-date)))
                     db (:db (conecta-bd))]
                 (update-mercado db p)
                 (json/write-str (mc/insert-and-return db "produtos" p) :value-fn transforma-id-para-string))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn boot-cadastra [request]
  (-> (r/response
       (dosync (let [todos-produtos (map (fn [{:keys [nome preco] :as produto}]
                                           (assoc produto :nome (normaliza nome) :preco (Float/valueOf preco))) 
                                         (parse-request-cadastro (:body request)))
                     tudo (map #(assoc % :data (str (t/local-date))) todos-produtos)
                     db (:db (conecta-bd))]
                 (doall (map #(update-mercado db %) tudo))
                 (mc/insert-batch db "produtos" tudo)
                 (json/write-str (db-consulta-produto db {}) :value-fn transforma-id-para-string))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn opcoes []
  (-> (r/response "")
      (r/header "Access-Control-Allow-Origin" "*")
      (r/header "Allow" "POST")
      (r/header "Access-Control-Allow-Methods" "POST")
      (r/header "Access-Control-Allow-Headers" "content-type")))

(defn le-payload! [request]
  (json/read-str (slurp (:body request)) :key-fn keyword))

(defn registro [obs preco]
  {:obs obs :preco preco})

;:banana {:sumario (registro "banana-obs" 1) :historico [(registro "" 1) (registro "" 2)]}
(def todos-produtos (atom {}))

(defn get-produtos-nome [nome]
  ((keyword nome) @todos-produtos))

(defn produtos []
  (-> (r/response (json/write-str @todos-produtos))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn produtos-nome [nome]
  (-> (r/response (json/write-str (get-produtos-nome nome)))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn produtos-nome-sumario [nome request]
  (let [payload (le-payload! request)]
    (do
      (swap! todos-produtos #(assoc-in % [(keyword nome) :sumario] payload))
      {:status 200
       :headers {"Access-Control-Allow-Origin" "*"}})))

(defn produtos-nome-historico [nome request]
  (let [payload (le-payload! request)]
    (do
      (swap! todos-produtos #(update-in % [(keyword nome) :historico] (fn [coll] (conj coll payload))))
      {:status 200
       :headers {"Access-Control-Allow-Origin" "*"}})))

(defn produtos-nome-id [nome id]
  (-> (r/response (json/write-str (first (filter #(= (:id %) (read-string id)) (:historico (get-produtos-nome nome))))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn insere-produtos [request]
  (let [payload (le-payload! request)]
    (do (swap! todos-produtos conj payload)
        {:status 200
         :headers {"Access-Control-Allow-Origin" "*"}})))

;; Rotas
(defroutes app-routes
  (GET "/produtos" [] (produtos))
  (GET "/produtos/:nome" [nome] (produtos-nome nome))
  (POST "/produtos/:nome/sumario" [nome :as r] (produtos-nome-sumario nome r))
  (POST "/produtos/:nome/historico" [nome :as r] (produtos-nome-historico nome r))
  (GET "/produtos/:nome/:id" [nome id] (produtos-nome-id nome id))
  (POST "/produtos" request (insere-produtos request))
  (GET "/consulta/:nome" [nome] (consulta nome))
  (GET "/consulta" [] (consulta-produtos))
  (GET "/consulta-mercado" [] (consulta-mercado))
  (POST "/remove-tudo" [] (remove-tudo))
  (POST "/cadastra" request (cadastra request))
  (POST "/boot-cadastra" request (boot-cadastra request))
  (POST "/boot-mercado" request (boot-mercado request))
  (POST "/salva-mercado" request (salva-mercado request))
  (OPTIONS "/cadastra" request (opcoes))
  (OPTIONS "/produtos" request (opcoes))
  (OPTIONS "/boot-cadastra" request (opcoes))
  (OPTIONS "/boot-mercado" request (opcoes))
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
