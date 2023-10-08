import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/70.0.3538.77 Safari/537.36'}

url = 'https://httpbin.org/get'
data = requests.get(url, headers=headers)
print(data.text)
