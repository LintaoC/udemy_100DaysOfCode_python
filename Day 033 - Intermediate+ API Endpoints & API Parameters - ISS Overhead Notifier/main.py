import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.0
MY_LONG = -63.0

my_email = "xxx@gmail.com"
password = "xxx"

def send_email():
    print("email send")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look at ISS!\n\nHi, the ISS is close to you! Try to watch it!")


def check_position(iss_lat, iss_long, my_lat, my_long):
    if (iss_lat - 5.0 <= my_lat <= iss_lat + 5.0) and (iss_long - 5.0 <= my_long <= iss_long + 5.0):
        return True


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    if check_position(iss_lat=iss_latitude, iss_long=iss_longitude, my_lat=MY_LAT, my_long=MY_LONG):
        print("Iss is close to my position!")
        if time_now.hour <= sunrise or time_now.hour >= sunset:
            print("Iss is close to my position! And it's dark")
            send_email()

    print(time_now.hour)
    print(f"Sunrise: {sunrise} - Sunset {sunset} /// Now: {time_now.hour}")
    print(f"ISS: {iss_latitude} / {iss_longitude} / Me {MY_LAT} / {MY_LONG}")

    time.sleep(60)
