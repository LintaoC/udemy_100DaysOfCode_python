import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os

FCB_EMAIL = os.environ.get("FCB_EMAIL")
FCB_PSW = os.environ.get("FCB_PSW")

firefox_driver_path = "/home/zellkoss/Programme/geckodriver"

driver = webdriver.Firefox(executable_path=firefox_driver_path,
                           firefox_profile="/home/zellkoss/.mozilla/firefox/62aphpex.bot")

driver.get("https://tinder.com")
base_window = driver.window_handles[0]

time.sleep(2)
acpt_cookie_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/button")
acpt_cookie_button.click()

time.sleep(2)
signin_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/'
                                             'div/div/div/div/header/div/div[2]/div[2]/a')
signin_button.click()

time.sleep(2)
fcb_connection_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
fcb_connection_button.click()

time.sleep(2)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(2)

fcb_cookie = driver.find_elements_by_css_selector("button")
for button in fcb_cookie:
    if button.text == "Alle akzeptieren":
        button.click()

email = driver.find_element_by_id("email")
email.send_keys(FCB_EMAIL)
password = driver.find_element_by_id("pass")
password.send_keys(FCB_PSW)
fcb_signin_buton = driver.find_element_by_id("loginbutton")
fcb_signin_buton.click()

time.sleep(4)
driver.switch_to.window(base_window)

#  --> Localisation and notification are not needed as I created a firefox profile with exceptions for Tinder
# localisation_accept_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
# localisation_accept_button.click()
# time.sleep(4)
# notification_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
# notification_button.click()

time.sleep(2)
tinder_gold_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]')
tinder_gold_button.click()

# Like the next N profiles
for n in range(0, 90):
    waiting_time_s = 1
    time.sleep(waiting_time_s)
    print(f"like {n}")
    try:
        if n > 0:
            like_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/'
                                                       'main/div[1]/div/div/div[1]/div[1]/'
                                                       'div/div[5]/div/div[4]/button')
        else:
            like_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/'
                                                       'main/div[1]/div/div/div[1]/div[1]/'
                                                       'div/div[4]/div/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        print("No more like)")
        break

driver.quit()
