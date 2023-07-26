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

print(data)


# If the ISS is close to my current position
def check_is_close():
    my_latitude_range = range(int(MY_LAT) - 5, int(MY_LAT) + 5)
    my_longitude_range = range(int(MY_LONG) - 5, int(MY_LONG) + 5)

    if iss_latitude in my_latitude_range and iss_longitude in my_longitude_range:
        return True


# and it is currently dark
def check_is_dark():
    pass

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
