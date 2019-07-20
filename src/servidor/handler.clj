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

(def db
  (:db (conecta-bd)))

(defn db-consulta-produto [query]
  (mc/find-maps db "produtos" query))

(defn insert [item]
  (mc/insert-and-return db "produtos" item))

(defn db-remove-tudo [db nome]
  (mc/remove db nome))

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

(defn filtra-produto [nome colecao] 
  (filter (fn [p] (= nome (:nome p))) colecao))

(defn transforma-id-para-string [chave valor]
  (if (= chave :_id) (str (ObjectId.)) valor))

(defn transforma-preco [chave valor]
  (if (= chave :preco) (Float/valueOf valor) valor))

;; Servicos
(defn remove-tudo []
  (let [db (:db (conecta-bd))]
    (db-remove-tudo db "mercado")
    (db-remove-tudo db "produtos")
    (-> (r/response "Removido")
        (r/header "Access-Control-Allow-Origin" "*"))))

(defn opcoes []
  (-> (r/response "")
      (r/header "Access-Control-Allow-Origin" "*")
      (r/header "Allow" "POST")
      (r/header "Access-Control-Allow-Methods" "POST")
      (r/header "Access-Control-Allow-Headers" "content-type")))

(defn le-payload! [request]
  (json/read-str (slurp (:body request)) :key-fn keyword :value-fn transforma-valor-request))

; {:nome "banana" :sumario "sumario" :melhor-preco "" :historico [{:preco :obs :local}]}}
(defn get-produtos-nome [nome]
  (db-consulta-produto {:nome nome}))

(defn tem-sumario [nome]
  (let [item (db-consulta-produto {:nome nome})]
    (:sumario (first item))))

(defn insere-sumario [nome payload]
  (let [item (db-consulta-produto {:nome nome})]
    (if (empty? item)
      (mc/insert db "produtos" (conj {:nome nome} payload))
      (mc/update-by-id db "produtos" (:_id (first item)) {$set payload}))))

(defn produtos []
  (-> (r/response (json/write-str (db-consulta-produto {}) :value-fn transforma-id-para-string))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn produtos-nome [nome]
  (-> (r/response (json/write-str (get-produtos-nome nome) :value-fn transforma-id-para-string))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn produtos-nome-sumario [nome request]
  (let [payload (le-payload! request)]
    (do
      (if (tem-sumario nome)
        (insere-sumario nome payload)
        (insert {:nome nome :sumario (:sumario payload)}))
      {:status 200
       :headers {"Access-Control-Allow-Origin" "*"}})))

(defn insere-historico [nome payload]
  (let [item (first (db-consulta-produto {:nome nome}))
        historico (:historico item)
        novo-historico (conj historico payload)
        melhor-preco (apply min (map :preco novo-historico))
        novo-item (assoc (assoc item :melhor-preco (min melhor-preco (:preco payload))) :historico novo-historico)
        x (println (str "novo-item " novo-item))
]
    (mc/update-by-id db "produtos" (:_id item) {$set novo-item})))

(defn produtos-nome-historico [nome request]
  (let [payload (le-payload! request)]
    (do
      (if (tem-sumario nome)
        (insere-historico nome payload)
        (do (insere-sumario nome {:sumario ""})
            (insere-historico nome payload)))
      {:status 200
       :headers {"Access-Control-Allow-Origin" "*"}})))

(defn produtos-nome-id [nome id]
  (-> (r/response (json/write-str (first (filter #(= (:id %) (read-string id)) (:historico (get-produtos-nome nome))))))
      (r/header "Access-Control-Allow-Origin" "*")))

(defn insere-produtos [request]
  (let [payload (le-payload! request)]
    (do (insert payload)
        {:status 200
         :headers {"Access-Control-Allow-Origin" "*"}})))

;; Rotas
(defroutes app-routes
  (GET "/produtos" [] (produtos))
  (POST "/produtos" request (insere-produtos request))
  (GET "/produtos/:nome" [nome] (produtos-nome (normaliza nome)))
  (POST "/produtos/:nome/sumario" [nome :as r] (produtos-nome-sumario (normaliza nome) r))
  (POST "/produtos/:nome/historico" [nome :as r] (produtos-nome-historico (normaliza nome) r))
  (GET "/produtos/:nome/:id" [nome id] (produtos-nome-id (normaliza nome) id))
  (POST "/remove-tudo" [] (remove-tudo))
  (OPTIONS "/produtos" request (opcoes))
  (OPTIONS "/produtos/:nome/sumario" [nome :as r] (opcoes))
  (OPTIONS "/produtos/:nome/historico" [nome :as r] (opcoes))
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
