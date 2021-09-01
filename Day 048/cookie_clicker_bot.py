from selenium import webdriver
import time

def check_my_cookie():
    my_cookie = driver.find_element_by_id("money")
    return int(my_cookie.text.replace(",",""))

def buy_addon(cookie):
    items = driver.find_elements_by_css_selector("#store b")
    item_to_buy = ""
    is_buying = False
    for item in items:
        try:
            price = item.text.split("-")[1]
            price = price.replace(",","").strip()
            if cookie >= int(price):
                item_to_buy = item
                is_buying = True
        except IndexError:
            print ("empty item")
    
    if is_buying:
        print(f"I'm buying {item_to_buy.text}")
        item_to_buy.click()
        is_buying = False

#firefox_driver_path = "/home/zellkoss/Programme/geckodriver"
google_driver_path = "C:\dev\chromedriver.exe"

#driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver = webdriver.Chrome(executable_path=google_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
         
time_to_buy = time.time() + 15   # Every 15 second we buy the most expensice item
timeout = time.time() + 5*60   # After 5 minutes we end the program
   
while True:
    cookie.click()
    if time.time() > timeout:
        break
    elif time.time() > time_to_buy:
        my_coockie = check_my_cookie()
        buy_addon(my_coockie)
        time_to_buy = time.time() + 15   # Every 15 second we buy the most expensice item

print(f"My cookie number after 5min: {check_my_cookie()}")
