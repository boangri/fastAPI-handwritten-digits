#/bin/bash

#curl -X POST  http://localhost:8000/predict -H "Accept: application/json" -H "Content-Type: application/json" --data '{"data":[[0.00632,18,2.31,0,0.538,6.575,65.2,4.09,1,296,15.3,396.9,4.98]]}'
curl -i -X POST  http://localhost:8000/predict -H "Accept: application/json" -H "Content-Type: application/json" -d '@data.json'
