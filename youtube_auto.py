#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dines
#
# Created:     25-05-2024
# Copyright:   (c) dines 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
class music():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        video=self.driver.find_element("xpath",'//*[@id="video-title"]/yt-formatted-string')
        video.click()

