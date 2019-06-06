#!/bin/bash
curl -v -H "Content-Type: application/json"  --request POST -d '{"obs":"Na feira é R$ 2.79"}' localhost:3000/produtos/banana/obs
curl -v -H "Content-Type: application/json"  --request POST -d '{"obs":"No bistek é sempre R$ 3.49"}' localhost:3000/produtos/papel-toalha/obs
