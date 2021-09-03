from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os

SIMILAR_ACCOUNT = "elonofficiall"
USERNAME = "xxxx"
PASSWORD = "xxxx"

#FIREFOX_DRIVER_PATH = "/home/zellkoss/Programme/geckodriver"
GOOGLE_DRIVER_PATH = "C:\dev\chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=GOOGLE_DRIVER_PATH)
        # self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)

    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        # Accept Cookies
        cookies_button = self.driver.find_element_by_class_name("bIiDR")
        cookies_button.click()
        time.sleep(3)
        # Login to Instagram
        username_input = self.driver.find_element_by_name("username")
        psw_input = self.driver.find_element_by_name("password") 
        username_input.send_keys(USERNAME)
        psw_input.send_keys(PASSWORD)  
        psw_input.send_keys(Keys.ENTER)   
        time.sleep(4)
        # Do not save info
        not_saving_button = self.driver.find_element_by_class_name("y3zKF")
        not_saving_button.click()
        time.sleep(4)
        # Do not turn on notification
        notification_button = self.driver.find_element_by_class_name("HoLwm")
        notification_button.click()
        time.sleep(4)

    
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        follower_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_button.click()
        
        time.sleep(3)
        
        scroll_bar = self.driver.find_element_by_class_name("isgrP")
        for n in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_bar)
            time.sleep(1)


    def follow(self):
        
        # If I selected the buttons with the class y3zKF, only the people who are not followed will be listed !
        list_followers = self.driver.find_elements_by_class_name("y3zKF")
         # If I selected the buttons with the css selector all the buttons will be listed !
        #list_followers = self.driver.find_elements_by_css_selector("li button")
        
        for item in list_followers:
            try:
                item.click()
            
            except ElementClickInterceptedException:
                print("Already followed")
                cancel_button = self.driver.find_element_by_class_name("HoLwm")
                cancel_button.click()

            
            time.sleep(2)
        

insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
