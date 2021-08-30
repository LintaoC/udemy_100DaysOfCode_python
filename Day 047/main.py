from bs4 import BeautifulSoup
import requests
import os
import smtplib

my_email = os.environ.get("my_email")
password = os.environ.get("password")


def send_email():
    print("email send")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amzone Price alert!\n\nCore email")


# ************ SCRAPING THE ITEM PRICE *************
url = "https://www.amazon.com/" \
      "ASUS-Graphics-Axial-Tech-2-9-Slot-AllyFlex/dp/B092KQ6LGF/" \
      "ref=sr_1_3?crid=3R38I01TZULMJ&dchild=1&keywords=nvidia+geforce+rtx+3060+ti&qid=" \
      "1630354093&sprefix=nvida+%2Caps%2C200&sr=8-3"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept-Language": "en-US,en;q=0.5",
}
r = requests.get(url, headers=header)
amazon_page = r.text

soup = BeautifulSoup(amazon_page, 'html.parser')
price = soup.find("span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price_int = int(price.getText()[1:-3].replace(",", ""))  # Refining the price, to turn it into an int
print(price_int)
print(type(price_int))
