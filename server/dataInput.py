from re import X
import requests
import json

# request Spreadsheet API
headers  = {'content-type': 'application/json'}
response = requests.get("https://sheet2api.com/v1/AcvTsTprT7Kr/usersdata/Sheet1", headers=headers)

# read data from the newest user
x        = json.dumps(response.json())
userList = json.loads(x)
listCout = len(userList)
newUser  = userList[listCout - 1]

# request SEON API
headers  = {"X-API-KEY": "aea77273-6080-4d20-b90c-d48fbe5095e0"}
userData = requests.get("https://api.seon.io/SeonRestService/email-api/v2.1/" + newUser['EMAIL'], headers=headers)

# save the data into SERVER
with open(newUser['USER NAME'] + ".json", 'w') as file:
    json.dump(userData.json(), file, indent=4, separators=(".","="))
