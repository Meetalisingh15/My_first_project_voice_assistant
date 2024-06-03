#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dines
#
# Created:     31-05-2024
# Copyright:   (c) dines 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests
url="https://official-joke-api.appspot.com/random_joke"
json_data=requests.get(url).json()
arr=["",""]
arr[0]=json_data["setup"]
arr[1]=json_data["punchline"]
def joke():
    return arr

