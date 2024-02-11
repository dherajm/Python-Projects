import requests
from twilio.rest import Client

account_sid = '<AUTH_SID-TWILIO>'
auth_token = '<AUTH_TOKEN-TWILIO>'
client = Client(account_sid, auth_token)

lat = '<YOUR_LATITUDE>'
lon = '<YOUR_LONGITUDE>'
APIkey = '<YOUR_API_KEY>'
time_stamp_count = 4  # (3hrs * 4 = 12) Therefore, when the program is executed, the api will request data only for the next 12 hrs

url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APIkey}&cnt={time_stamp_count}"

whether_next_12_hrs = []


def get_weather_data():
    global whether_next_12_hrs
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    for i in range(0, 4):
        whether_data = (data["list"][i]["weather"][0]["id"])
        whether_next_12_hrs.append(whether_data)

    send_sms()


def send_sms():
    global whether_next_12_hrs

    if any(weather_id < 700 for weather_id in whether_next_12_hrs):
        rain_alert = ("RAINY DAY ALERT!\n\nThere is a possibility that is might in the next 12 hrs.\nPlease carry an "
                      "Umbrella along with you.")

        message = client.messages.create(
            from_='<NUMBER_GENERATED_BY_TWILIO>',
            body=rain_alert,
            to='<YOUR_PHONE_NO.>'
        )

        print(message.sid)


get_weather_data()
