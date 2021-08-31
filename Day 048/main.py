from selenium import webdriver

python_events = {
    0: {"": "date"},
    1: {"time1": "date1"},
}

firefox_driver_path = "/home/zellkoss/Programme/geckodriver"

driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver.get("https://www.python.org")

events_time = driver.find_elements_by_css_selector(".last time")
events_name = driver.find_elements_by_css_selector(".list-widgets .last .menu a")

list_event_date = [event.text for event in events_time]
print(list_event_date)

list_event_name = [event.text for event in events_name]
print(list_event_name)

# new_dict = {i: "" for i in range(len(list_event_name))}
#
# for i in range(len(list_event_name)):
#     new_dict[i] = {"time": list_event_date[i],
#                    "name": list_event_name[i]}

new_dict = {i: {"time": list_event_date[i], "name": list_event_name[i]} for i in range(len(list_event_name))}

print(new_dict)

driver.quit()  # Close the browser

# driver.get("https://www.amazon.com/ASUS-Graphics-Axial-Tech-2-9-Slot-AllyFlex/dp/B092KQ6LGF")
# # name = driver.find_element_by_id("productTitle")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price[0].text) # Print the price

# for element in price: # Other solutions
#     print(element)
#     print(element.text)


# driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.width)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('/html/body/div/footer/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.close()  # Close the tab
# driver.quit()  # Close the browser
