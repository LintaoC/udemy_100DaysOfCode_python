import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os

LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PSW = os.environ.get("LINKEDIN_PSW")

firefox_driver_path = "/home/zellkoss/Programme/geckodriver"
# google_driver_path = "C:\dev\chromedriver.exe"

driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver.maximize_window()
# driver = webdriver.Chrome(executable_path=google_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C"
    "%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

signin_button = driver.find_element_by_link_text("S’identifier")
signin_button.click()

# Wait for the next page to load.
time.sleep(3)

email = driver.find_element_by_id("username")
email.send_keys(LINKEDIN_EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(LINKEDIN_PSW)
password.send_keys(Keys.ENTER)

# Wait for the next page to load.
time.sleep(7)

job_offers = driver.find_elements_by_class_name("jobs-search-results__list-item")

page_number = 1


def goto_next_page(actual_page_number):
    list_page_number = driver.find_elements_by_css_selector(".artdeco-pagination__pages li")
    previous_page = 0
    for pages in list_page_number:
        print("___")
        print(f"Page checked: {pages.text}")
        print(f"Previous page: {previous_page}")
        print(f"actual page n: {actual_page_number}")
        if pages.text == "…" and (previous_page == actual_page_number):
            pages.click()
            print("... page")
            return actual_page_number + 1
        elif pages.text == "…":
            previous_page += 1
        elif int(pages.text) == (actual_page_number + 1):
            pages.click()
            return actual_page_number + 1

        previous_page += 1


while True:
    page_number = goto_next_page(page_number)
    time.sleep(4)

# for jobs in job_offers:
#     print(jobs.text)
#     jobs.click()
#     time.sleep(1)
#     save_button = driver.find_element_by_class_name("jobs-save-button")
#     save_button.click()
#     time.sleep(1)


# save_button = driver.find_element_by_class_name("jobs-save-button")
# save_button.click()


# f_name = driver.find_element_by_name("fName")
# l_name = driver.find_element_by_name("lName")
# email = driver.find_element_by_name("email")
# #signup_button = driver.find_element_by_xpath('/html/body/form/button')
# signup_button = driver.find_element_by_css_selector("form button")
# f_name.send_keys("MyF_Name")
# l_name.send_keys("MyL_Name")
# email.send_keys("MyEmail@gmail.com")
# signup_button.click()
