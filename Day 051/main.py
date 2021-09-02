import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
TWITTER_PSW = os.environ.get("TWITTER_PSW")

firefox_driver_path = "/home/zellkoss/Programme/geckodriver"

driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver.get("https://www.speedtest.net/")

speedtest_button = driver.find_element_by_class_name("js-start-test")
speedtest_button.click()

time.sleep(50)

get_down_speed = driver.find_element_by_class_name("download-speed")
get_up_speed = driver.find_element_by_class_name("upload-speed")

print(f"Down: {get_down_speed.text} / Up: {get_up_speed.text}")
tested_down_speed = float(get_down_speed.text)
tested_up_speed = float(get_up_speed.text)

if tested_down_speed < PROMISED_DOWN or tested_up_speed < PROMISED_UP:
    driver.get("https://twitter.com")
    time.sleep(2)
    twitter_connect_button = driver.find_element_by_xpath(
        '/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
    twitter_connect_button.click()
    time.sleep(2)
    twitter_connect_mail_button = driver.find_element_by_xpath(
        '/html/body/div/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a')
    twitter_connect_mail_button.click()
    time.sleep(2)
    twitter_input_mail = driver.find_element_by_name("session[username_or_email]")
    twitter_input_psw = driver.find_element_by_name("session[password]")
    twitter_input_mail.send_keys(TWITTER_USERNAME)
    twitter_input_psw.send_keys(TWITTER_PSW)
    twitter_input_psw.send_keys(Keys.ENTER)
    time.sleep(3)
    twitter_input_tweet = driver.find_element_by_class_name("public-DraftEditor-content")
    twitter_input_tweet.send_keys(
        f"Hey @Test, why is my internet speed is : [{tested_down_speed}down/{tested_up_speed}up] "
        f"when I pay for [{PROMISED_UP}down/{PROMISED_DOWN}up] ?!")
    time.sleep(1)
    twitter_tweet_button = driver.find_element_by_xpath(
        '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
        '3]/div/div/div[2]/div[3]/div/span/span')
    twitter_tweet_button.click()
