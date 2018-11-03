(ns servidor.handler-test
  (:require [clojure.test :refer :all]
            [ring.mock.request :as mock]
            [clojure.edn :as edn]
            [clojure.data.json :as json]
            [servidor.handler :refer :all]))

(defn tira-ids [produto]
  (dissoc produto :_id))

(def BACKUP "./backup.json")

(defn chama-cadastra [produto]
  (is (= (app (-> (mock/request :post "/cadastra")
                  (mock/json-body produto)))
         {:status 200})))

(deftest test-app
  (testing "consulta tudo e guarda backup"
      (let [response (app (mock/request :get "/consulta"))
            resultado (json/read-str (:body response) :key-fn keyword)]
        (is (= (:status response) 200))
        (let [resultado (map tira-ids resultado)] 
          (spit BACKUP (prn-str resultado)))))
  (testing "cadastra todo backup" 
    (let [produtos (-> BACKUP (slurp) (edn/read-string))] 
      (doall (map chama-cadastra produtos)))))
