import requests

resposne = requests.get("https://www.google.com")

print(resposne.text)
