#import the necessary libaries
import email
import requests
import json
import numpy as np


#make an array of social platforms & information that will be gathered
socialPlatform_registered = np.array([])
name = np.array([])
photo = np.array([])
company = np.array([])
linkedIn_title = np.array([])
website = np.array([])
location = np.array([])
country = np.array([])
city = np.array([])
id = np.array([])
bio = np.array([])
age = np.array([])
language = np.array([])
skype_state = np.array([])
airbnb_created_at = np.array([])
reviewee_count = np.array([])
work = np.array([])
gender = np.array([])
twitter_name = np.array([])

#create an array of the several arrays for easy indexing later
info = np.array([socialPlatform_registered, name, photo, company, linkedIn_title,
website, location, country, city, id, bio, age, language, skype_state, airbnb_created_at,
airbnb_created_at, reviewee_count, work, gender, twitter_name])

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
            #print(socialPlatform)
            np.append(socialPlatform_registered, socialPlatform)
                        
            #go over all the keys and their corresponding value for this social platform, e.g. age, name are keys and 20, Emilie are values
            for key,value in value.items():
                #check whether the key has a value
                if value is not None:
                  #save the value of the key in the corresponing array
                  #check for switch
                  if key == "name":
                    np.append(name, value) 
                  if key == "photo" or key == "image":
                    np.append(photo, value) 
                  if key == "company":
                    np.append(company, value) 
                  if key == "title":
                    np.append(linkedIn_title, value) 
                  if key == "website":
                    np.append(website, value)
                  if key == "twitter":
                    np.append(twitter_name, value)
                  if key == "location":
                    np.append(location, value)
                  if key == "country":
                    np.append(country, value)
                  if key == "city":
                    np.append(city, value)
                  if key == "gender":
                    np.append(gender, value)
                  if key == "id":
                    np.append(id, value)
                  if key == "bio" or "about":
                    np.append(bio, value)
                  if key == "age":
                    np.append(age, value)
                  if key == "language":
                    np.append(language, value)
                  if key == "state":
                    np.append(skype_state, value)
                  if key == "created_at":
                    np.append(airbnb_created_at, value)
                  if key == "first_name":
                    np.append(name, value)
                  if key == "reviewee_count":
                    np.append(reviewee_count, value)
                  if key == "work":
                    np.append(work, value)


#not working yet, some bug somewhere
for i in range(len(info)):
  print (info)
