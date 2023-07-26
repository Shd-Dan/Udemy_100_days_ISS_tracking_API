import smtplib
import time
from datetime import datetime

import requests

MY_LAT = 43.222015
MY_LONG = 76.851250

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(type(data))

# parameters = {
#     "lat": MY_LAT,
#     "long": MY_LONG,
#     "formatted": 0
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
# sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
#
# print(data)

# print(sunset)
#
# time_now = datetime.datetime.now()
#
# print(time_now.hour)

""" ----------------------------- Main Challenge -----------------------------"""
""" ----------------------------- My Solution -----------------------------"""
MY_EMAIL = "big_bob_roof@mail.ru"
APP_PASSWORD = "XGKCjx3rfQ28uXZA3qBD"
MAIL_SMTP = "smtp.mail.ru"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour


# If the ISS is close to my current position
def check_is_close():
    my_latitude_range = range(int(MY_LAT) - 5, int(MY_LAT) + 5)
    my_longitude_range = range(int(MY_LONG) - 5, int(MY_LONG) + 5)

    if int(iss_latitude) in my_latitude_range and int(iss_longitude) in my_longitude_range:

        return True
    else:
        return False


# and it is currently dark
def check_is_dark():
    if hour_now not in range(sunrise, sunset):
        return True


# Then send me an email to tell me to look up.

while True:
    time.sleep(60)

    if check_is_close() is True and check_is_dark() is True:

        with smtplib.SMTP(MAIL_SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:It's comiiiing!!!\n\nHey look up!!!")
    else:
        print("Something wrong")

    # BONUS: run the code every 60 seconds.

""" ----------------------------- Angela's Solution -----------------------------"""

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
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

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
