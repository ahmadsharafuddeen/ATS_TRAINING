import requests
from datetime import datetime
import smtplib

MY_EMAIL = "9hyqndpc@mailosaur.net"
MY_PASSWORD = "cR463TChhWkPYD13"


MY_LAT = 7.348720
MY_LONG = 3.879290


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 < iss_latitude <= MY_LAT+5 and MY_LONG-5 < iss_longitude <= MY_LONG+5:
        return True


def is_night():
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

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True


# if is_iss_overhead() and is_night():
try:
    connection = smtplib.SMTP("smtp.mailosaur.net")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look Up🤟\n\nThe ISS is above you in the sky."
    )
except Exception as err:
    print(err)



