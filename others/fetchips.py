import json
import requests

URL = "https://api.config.zscaler.com/zscaler.net/cenr/json"

response = requests.get(URL).content

json_response = json.loads(response)

print(json_response['zscaler.net']['continent : Americas'])
