import requests
vitsi = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(vitsi).json()
print(vastaus["value"])
