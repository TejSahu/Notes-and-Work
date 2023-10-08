from bs4 import BeautifulSoup as bs
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/70.0.3538.77 Safari/537.36'}
url = 'https://www.linkedin.com/jobs/search?keywords=DevOps&location=Pune%2C%20Maharashtra%2C%20India&locationId=&' \
      'geoId=103671728&f_TPR=r2592000&distance=25&position=1&pageNum=0'

response = requests.get(url, headers=headers)
soup = bs(response.content, 'html.parser')
print(soup)
for elements in soup:
    joblist = soup.find()