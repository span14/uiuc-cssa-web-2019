import json 
import requests
from flask import current_app

def get_location(ip):
    url = "https://freegeoip.app/{}/{}".format("json", ip)
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
    }
    request = requests.get(url, headers=headers)

    
    if request.status_code != 200:
        return ('Error', 'Error')
    
    response = request.json()
    if response['country_code'] == '':
        return ('Error', 'Error')
    
    return (response['country_code'], response['zip_code'])

def get_weather(country, zip_code):

    if current_app.config['OPENWEATHER'] is None:
        return ('Error', 'Error')

    url = "api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}".format(country.lower(), zip_code, current_app.config['OPENWEATHER'])

    headers = {
        'accept': "application/json",
        'content-type': "application/json"
    }

    request = requests.get(url, headers=headers)

    if request.status_code != 200:
        return ('Error', 'Error')
    
    response = request.json()

    if response
    
    return ()
    








