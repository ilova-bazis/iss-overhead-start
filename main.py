import requests
from datetime import datetime

MY_LAT = 40.289982 # Ваша широта (latitude)
MY_LONG = 69.619926 # Ваша долгота (longitude)

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Ваша позиция в пределах +5 или -5 градусов от позиции МКС.


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

# Если МКС находится близко к моему текущему положению
# и сейчас темно
# Тогда отправьте мне электронное письмо, чтобы сказать мне посмотреть вверх.
# БОНУС: запускайте код каждые 60 секунд.




