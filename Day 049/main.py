import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
import os

LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PSW = os.environ.get("LINKEDIN_PSW")

firefox_driver_path = "/home/zellkoss/Programme/geckodriver"

driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver.maximize_window()
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


def save_jobs():
    job_offers = driver.find_elements_by_class_name("jobs-search-results__list-item")
    for jobs in job_offers:
        print(jobs.text)
        jobs.click()
        time.sleep(1)
        save_button = driver.find_element_by_class_name("jobs-save-button")
        save_button.click()
        time.sleep(1)


def goto_next_page(actual_page_number, skip):
    list_page_number = driver.find_elements_by_css_selector(".artdeco-pagination__pages li")
    for pages in list_page_number:
        print(f"Page checked: {pages.text}")
        if pages.text == "…" and not skip:
            pages.click()
            return actual_page_number + 1
        elif pages.text == "…":
            pass
        elif int(pages.text) == (actual_page_number + 1):
            pages.click()
            return actual_page_number + 1


page_number = 1
page_skip = False

while True:
    save_jobs()
    page_number = goto_next_page(page_number, page_skip)
    if page_number >= 9:
        page_skip = True
    time.sleep(5)
