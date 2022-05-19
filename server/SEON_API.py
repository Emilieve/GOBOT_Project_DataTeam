import email
import requests
import json

headers = {
  "X-API-KEY": "006c4bc3-4454-4990-8be1-3b0ce6e4df50"
}

r = requests.get("https://api.seon.io/SeonRestService/email-api/v2.1/emilie.van.eps@gmail.com", headers=headers)
a = r.json()
print(a['data']['email'])
