import requests
import smtplib
import os


def send_email():
    print("email send")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:It will rain today!\n\nHi, take your umbrella! It will rain today.\nBye")


API_KEY = os.environ.get("OWM_API_KEY")
print(API_KEY)
LAT = 0.00
LONG = 0.000

my_email = os.environ.get("GMAIL_BOT_MAIL")
password = os.environ.get("GMAIL_BOT_PASSWORD")

weather_params = {
    "lat": 46.519653,
    "lon": 6.632273,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
data.raise_for_status()
weather_data = data.json()

weather_data_hourly_list = [weather_data["hourly"][n] for n in range(0, 12)]

# I could have have get the first 12 hours more easily with Slice methode, like below
# weather_data_hourly_list = data["hourly"]
# print(weather_data_hourly_list[slice(11)])

is_raining = False
rain_status = ""

for item in weather_data_hourly_list:
    condition_id = item["weather"][0]["id"]
    if condition_id < 700:
        print("Bring an umbrella")
        is_raining = True
        # break

if is_raining:
    send_email()
    print("Bring an umbrella")
