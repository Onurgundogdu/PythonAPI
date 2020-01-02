import requests
weather_api='https://api.openweathermap.org/data/2.5/weather?appid=['Your api key']&q='
city=input("Şehir: ")
url=weather_api+city
data=requests.get(url).json()
description=data['weather'][0]['main']
wind=data['wind']['speed']
print("Hava Durumu:",description,"\nRüzgar hızı:",wind)