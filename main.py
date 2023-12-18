import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f840b45dc8c810b44996350344027870"
account_sid = "AC892a598256d26426d45c64e3187def28"
auth_token = "6ac09ec76cf96cb24c6024ab925aa418"

weather_params = {
    "lat":40.409264,
    "lon":49.867092,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWN_Endpoint, params = weather_params)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today",
        from="+12057362627",
        to='Your verified number',
    )