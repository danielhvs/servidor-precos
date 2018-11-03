(ns servidor.handler-test
  (:require [clojure.test :refer :all]
            [ring.mock.request :as mock]
            [clojure.data.json :as json]
            [servidor.handler :refer :all]))

(defn tira-ids [produto]
  (json/write-str
   (dissoc produto :_id)))

(deftest test-app
  (testing "main route"
    (let [response (app (mock/request :get "/"))]
      (is (= (:status response) 200))
      (is (= (:body response) "Hello World"))))
  (testing "consulta tudo e guarda backup"
    (let [response (app (mock/request :get "/consulta"))
          resultado (json/read-str (:body response) :key-fn keyword)]
      (is (= (:status response) 200))
      (let [resultado (map tira-ids resultado)] 
        (spit "./backup.json" (prn-str resultado)))))
  (testing "not-found route"
    (let [response (app (mock/request :get "/invalid"))]
      (is (= (:status response) 404)))))
