# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:31:26 2021

@author: RDWyttenDa
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#firefox_driver_path = "/home/zellkoss/Programme/geckodriver"
google_driver_path = "C:\dev\chromedriver.exe"

#driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver = webdriver.Chrome(executable_path=google_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")


f_name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
#signup_button = driver.find_element_by_xpath('/html/body/form/button')
signup_button = driver.find_element_by_css_selector("form button")
f_name.send_keys("MyF_Name")
l_name.send_keys("MyL_Name")
email.send_keys("MyEmail@gmail.com")
signup_button.click()
