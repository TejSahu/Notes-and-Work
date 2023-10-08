from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/70.0.3538.77 Safari/537.36'}
# Enter the page URL, main page url like the one here where you can see the thumbnails
url = 'https://www.hdwallpapers.in/games-desktop-wallpapers/page/2'


def getlist(main_url):
    response = requests.get(main_url, headers=headers)
    soup = BeautifulSoup(response.content, features="lxml")
    prefix = 'https://www.hdwallpapers.in/download'
    html = soup.findAll('div', {'class': 'thumb'})
    list1 = []
    for links in html:
        list1.append(prefix + str(links.a['href'])[:-15] + '1920x1080.jpeg')
    return list1


def download(image_url):
    for link in image_url:
        response = requests.get(link, headers=headers)
        # with open("/home/tej/Downloads/gamewallpapers/" + str(image_url)[37:], 'wb') as image:
        #     image.write(response.content)
        #     print("Image saved")
        print(response)


if __name__ == "__main__":
    download(getlist(url))
