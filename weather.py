#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dines
#
# Created:     01-06-2024
# Copyright:   (c) dines 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests
api_address="https://api.openweathermap.org/data/2.5/weather?lat=28.7&lon=77.1&appid=594bb723ba06bfa79c1be789d2f031ac"
json_data=requests.get(api_address).json()
def temp():
    temperature=round(json_data["main"]["temp"]-273,1)
    return temperature
def des():
    description=json_data["weather"][0]["description"]
    return description

