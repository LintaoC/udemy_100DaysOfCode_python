# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:31:26 2021

@author: RDWyttenDa
"""

from selenium import webdriver


#firefox_driver_path = "/home/zellkoss/Programme/geckodriver"
google_driver_path = "C:\dev\chromedriver.exe"

#driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver = webdriver.Chrome(executable_path=google_driver_path)
driver.get("https://www.python.org")

events_date = driver.find_elements_by_css_selector(".last time")
events_name = driver.find_elements_by_css_selector(".list-widgets .last .menu a")
list_event_date = [event.get_attribute("datetime").split("T")[0] for event in events_date]
list_event_name = [event.text for event in events_name]

# new_dict = {i: "" for i in range(len(list_event_name))}
#
# for i in range(len(list_event_name)):
#     new_dict[i] = {"time": list_event_date[i],
#                    "name": list_event_name[i]}

new_dict = {i: {"time": list_event_date[i], "name": list_event_name[i]} for i in range(len(list_event_name))}

print(new_dict)

driver.quit()  # Close the browser
