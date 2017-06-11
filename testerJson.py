import requests
import json
son = '{"name":"Jose"}'

headers = {'content-type': 'application/json'}


response = requests.post('http://localhost:56951/ApiUrlThatPythonUses/Test',data=json.dumps(son),headers = headers)

print response