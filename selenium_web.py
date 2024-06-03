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
class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search=self.driver.find_element("xpath",'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element("xpath",'//*[@id="search-form"]/fieldset/button')
        enter.click()
