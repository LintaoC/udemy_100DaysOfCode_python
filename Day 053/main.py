from selenium import webdriver
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import time
import requests

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeu2MGDr2IBZuXaCUyxRNr1uiVh3ZZA-FYa5_A1flvIHKK41g" \
                  "/viewform?vc=0&c=0&w=1&flr=0 "
FIREFOX_DRIVER_PATH = "/home/zellkoss/Programme/geckodriver"

# ******** Scraping Data's with BF4 ************
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept-Language": "en-US,en;q=0.5",
}


def get_addresses_url(bf_soup):
    """Get the addresses and URL's of the listing"""
    #  Only return the 9 first result, tried with different selector but same result
    all_url = bf_soup.select(selector=".list-card-info a")
    addresses_list = []
    addresses_url = []

    for url in all_url:
        if "zillow" not in url.get('href'):
            addresses_url.append(f"https://www.zillow.com{url.get('href')}")
        else:
            addresses_url.append(url.get('href'))

        addresses_list.append(url.getText())

    return addresses_list, addresses_url


def get_price(bf_soup):
    """Get the prices of the listing"""
    all_prices = bf_soup.select(selector=".list-card-price")
    addresses_price = []

    for price in all_prices:
        price_unformated = price.getText()
        if "+" in price_unformated:
            price_formated = price_unformated.split("+")
        elif " " in price_unformated:
            price_formated = price_unformated.split(" ")
        else:
            price_formated = price_unformated.split("/")
        addresses_price.append(price_formated[0])

    return addresses_price

NBR_OF_PAGE_TO_SCRAP = 30
addresses_list_all_pages = []
price_list_all_pages = []
url_list_all_pages = []

for n in range(1, NBR_OF_PAGE_TO_SCRAP):
    try:
        time.sleep(2)
        r = requests.get(
            f"https://www.zillow.com/homes/for_rent/1-_beds/50_p/?searchQueryState=%7B%22pagination%22%3A%7B"
            f"%22currentPage%22%3A{n}%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83501662207031%2C%22east%22%3A-122"
            f".03164137792969%2C%22south%22%3A37.5491679977143%2C%22north%22%3A38.000725404586724%7D%2C%22mapZoom%22"
            f"%3A11 "
            f"%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22"
            f"%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C"
            f"%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22"
            f"%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22"
            f"%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D",
            headers=HEADER)

        r.raise_for_status()
        zillow_page = r.content
        soup = BeautifulSoup(zillow_page, 'html.parser')

        zillow_url_addresses = get_addresses_url(soup)
        addresses_list_all_pages += zillow_url_addresses[0]
        url_list_all_pages += zillow_url_addresses[1]
        price_list_all_pages += get_price(soup)
        print(price_list_all_pages)
    except requests.exceptions.HTTPError:
        print("no more page to scrap")
        break
    except requests.TooManyRedirects:
        print("Too many redirect")
        break


print(len(url_list_all_pages))
print(len(addresses_list_all_pages))
print(len(price_list_all_pages))

# ******** Add data's to the form using Selenium ************
if len(price_list_all_pages) > 0:
    driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)

    for n in range(len(price_list_all_pages)):
        driver.get(GOOGLE_FORM_URL)

        address = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div['
                                               '2]/div/div[1]/div/div[1]/input')
        url = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                           '1]/div/div[1]/input')
        price = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
        try:
            address.send_keys(addresses_list_all_pages[n])
            url.send_keys(url_list_all_pages[n])
            price.send_keys(price_list_all_pages[n])
            time.sleep(2)

            button_send = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span')
            button_send.click()
        except ElementNotInteractableException:
            print("Form loading error")

        time.sleep(2)
