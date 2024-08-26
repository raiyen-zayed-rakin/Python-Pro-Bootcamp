import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "508100b9b2590e9b616bd81e0d1c86ee"

account_sid = "test"
auth_token = "test"

MY_LAT = 23.810331
MY_LONG = 90.412521

weathers_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weathers_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today, get a freaking umbrella",
        from_='+14422223775',
        to='+88001779309553'
    )
    print(message.status)



