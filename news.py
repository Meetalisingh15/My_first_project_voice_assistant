#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dines
#
# Created:     30-05-2024
# Copyright:   (c) dines 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests
api_address= "https://newsapi.org/v2/top-headlines?country=us&apiKey=a215ce3b945b4b8f8a0b47eb371fb695"
json_data=requests.get(api_address).json()
def get_top_headlines():
    headlines = []
    for i in range(3):
        headline = "Number {}, {}".format(i+1,  json_data["articles"][i]["title"])
        headlines.append(headline)
    return headlines


