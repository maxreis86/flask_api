import requests
import json
url = 'http://localhost:5000/predict'
r = requests.post(url, json={'INJURY_0': 1})
#print(json.loads(json.loads(r.json())))
print(r.json())