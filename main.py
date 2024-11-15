import requests
import pandas as pd

gender = []
title = []
firstname = []
lastname = []
house_no = []
house_name = []
city = []
state = []
country = []
postal_code = []
email = []
username = []
password = []
dob = []

lines = int(input("How many lines do you want?: "))
cols = int(input("How many columns do you want? (Less than 14): "))

response = requests.get(f'https://randomuser.me/api/?results={lines}')

for i in response.json()['results']:
    gender.append(i['gender'])
    title.append(i['name']['title'])
    firstname.append(i['name']['first'])
    lastname.append(i['name']['last'])
    house_no.append(i['location']['street']['number'])
    house_name.append(i['location']['street']['name'])
    city.append(i['location']['city'])
    state.append(i['location']['state'])
    country.append(i['location']['country'])
    postal_code.append(i['location']['postcode'])
    email.append(i['email'])
    username.append(i["login"]['username'])
    password.append(i["login"]['password'])
    dob.append(i['dob']['date'])

df = pd.DataFrame({'gender': gender, 'title': title, 'firstname': firstname,
                   'lastname': lastname, 'house_no': house_no, 'house_name': house_name,
                   'city': city, 'state': state,'country': country, 'postal_code': postal_code,
                   'email': email, 'username': username, 'password': password, 'dob': dob})

df2 = df.iloc[:, :cols]

df2.to_csv('data.csv', index=False)
print("Successfully exported to a csv called data.csv!")



