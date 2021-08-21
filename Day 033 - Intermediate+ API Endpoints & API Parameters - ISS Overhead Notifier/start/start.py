# Get value from a simple API, without parameters
import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status() # raise exception in case of error
# data = response.json()
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# iss_position = (latitude, longitude)
#
# print(data)
# print(iss_position)

MY_LAT = 50
MY_LONG = -60

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

print(sunrise_hour, sunset_hour)

time_now = datetime.now()
print(time_now.hour)
