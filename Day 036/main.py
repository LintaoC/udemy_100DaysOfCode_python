import requests
import smtplib


def send_email(status, percentage, news_title, news_link):
    print("email send")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:TSLA Stock is {status} by {percentage}%\n\nHi,\nTesla stock is {status} by {percentage}%\n"
                f"Latest Tesla news:\n1. {news_title} - {news_link}")


my_email = "xxx@gmail.com"
password = "xxx"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "xxx"
NEWS_PARAMS = {
    "apiKey" : NEWS_KEY,
    "q": f"({COMPANY_NAME})",
    "language": "en",
    "pageSize": 3
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "xxx"
STOCK_PARAMS = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey": STOCK_KEY,
}


r = requests.get(STOCK_ENDPOINT, STOCK_PARAMS)
r.raise_for_status()
data = r.json()

date_last_2_days = list(data["Time Series (Daily)"])[:2]  # Get the date of the two last days
closing_price_1 = float(data["Time Series (Daily)"][date_last_2_days[0]]["4. close"])  # Get the closing price of yesterday
closing_price_2 = float(data["Time Series (Daily)"][date_last_2_days[1]]["4. close"])  # Get the closing price of the day before yesterday

price_change_percentage = (closing_price_1 - closing_price_2) / closing_price_1 * 100

status = "up/down"

if price_change_percentage > 0:
    status = "UP"
else:
    status = "DOWN"

if price_change_percentage >= 5.0 or price_change_percentage <= -5.0:
    print("get news")
    r_news = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    r_news.raise_for_status()
    r_news_data = r_news.json()
    r_news_data_list = r_news_data["articles"]
    [send_email(status, round(price_change_percentage), news["title"], news["url"]) for news in r_news_data_list]
