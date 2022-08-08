import requests
from datetime import datetime

MY_LAT = 7.348720
MY_LONG = 3.879290

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# response2 = requests.get(url="https://api.kanye.rest/")
# print(response2.json())
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)

# wikipedia api

# wiki_response = requests.get("https://en.wikipedia.org/w/api.php")
# response.raise_for_status()
# print(wiki_response.json())

