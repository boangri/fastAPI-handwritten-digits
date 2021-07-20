import json
import requests

data = {
    "data": [
        [0.00632, 18, 2.31, 0, 0.538, 6.575, 65.2, 4.09, 1, 296, 15.3, 396.9, 4.98],
        [0.00632, 18, 2.31, 0, 0.538, 3.575, 65.2, 1.09, 1, 296, 15.3, 396.9, 4.98]
    ]
}
with open('data-mnist.json', 'r') as f:
    json_string = json.load(f)
#     print(json_string)
# json_string = json.dumps(data)

headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8000/predict', data=json_string, headers=headers)
try:
    predictions = json.loads(json_response.text)['data']
    output = predictions
except KeyError:
    output = json_response.text

print(output)
