#import the necessary libaries
import email
import requests
import json

#get the API key
headers = {
  "X-API-KEY": "006c4bc3-4454-4990-8be1-3b0ce6e4df50"
}

#get the API data and save it as JSON format
r = requests.get("https://api.seon.io/SeonRestService/email-api/v2.1/emilie.van.eps@gmail.com", headers=headers)
a = r.json()

#specifiy to the account details branch of the API data
b = a['data']['account_details']

#go over every social platform in the account details branch
for key,value in b.items():
        socialPlatform = key
        
        #if registered here -> print the social platform
        if value['registered'] == True:
            print(socialPlatform)
            
            #go over all the keys and their corresponding value for this social platform, e.g. age, name are keys and 20, Emilie are values
            for key,value in value.items():
                print(key, '-> ', value)
