from bs4 import BeautifulSoup
import requests
import os
import smtplib

my_email = os.environ.get("my_email")
password = os.environ.get("password")

TARGET_PRICE = 100.0


def send_email(item_price, item_name, item_url):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="my_email",
            msg=f"Subject:Amzone Price alert!\n\n{item_name} is now ${item_price}\n{item_url}")


# ************ SCRAPING THE ITEM PRICE *************
url = "https://www.amazon.com/PlayStation-Classic-Console/dp/B07HHVF2XG/ref=sr_1_1?dchild=1&keywords=playstation+consoles&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=4G7T8RYC6THTQ9YV28W4&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1630391583&s=videogames&sr=1-1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept-Language": "en-US,en;q=0.5",
}
r = requests.get(url, headers=header)
amazon_page = r.text

soup = BeautifulSoup(amazon_page, 'html.parser')
price = soup.find("span", class_="a-size-base a-color-price")
price_float = float(price.getText().replace("$", "").replace(",", ""))  # Refining the price, to turn it into an float
name = soup.find("span", class_="a-size-large product-title-word-break")
print(name.getText().strip())
print(price_float)

if price_float <= TARGET_PRICE:
    print("sending email")
    send_email(price_float, name, url)
