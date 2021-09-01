# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:31:26 2021

@author: RDWyttenDa
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#firefox_driver_path = "/home/zellkoss/Programme/geckodriver"
google_driver_path = "C:\dev\chromedriver.exe"

#driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver = webdriver.Chrome(executable_path=google_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_of_articles = driver.find_element_by_css_selector("#articlecount a")
#number_of_articles.click()


all_portals = driver.find_element_by_link_text("All portals")
#all_portals.click()

search = driver.find_element_by_name("search")  # Getting hold on the search bar
search.send_keys("Python")  # Entering Python in the search bar
search.send_keys(Keys.ENTER)  # Enter

#driver.quit()  # Close the browser
