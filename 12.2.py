import requests

kaupunki = input("haluttava kaupunki?")
saatilanne = f"https://api.openweathermap.org/data/2.5/weather?q="+kaupunki+"&appid=771c76e68d5570c7e31662da24f3bb7c"
vastaus = requests.get(saatilanne).json()

print(vastaus["weather"][0]["description"])

def kelvinToCelsius(kelvin):
    return kelvin - 273.15
kelvin = vastaus["main"]["temp"]
celsius = kelvinToCelsius(kelvin)

print((celsius).__round__(2))
