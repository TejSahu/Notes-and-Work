from bs4 import BeautifulSoup
import httpx
import asyncio

url = 'https://hdqwalls.com/category/games-wallpapers/page/12'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/70.0.3538.77 Safari/537.36'}


def geturls(page_url):
    response = httpx.get(url, headers=headers)
    soup = BeautifulSoup(response.content, features="lxml")
    prefix = 'https://images.hdqwalls.com/download/'
    html = soup.findAll('div', {'class': 'column_padding'})
    htmls = []
    for links in html:
        htmls.append(prefix + str(links.img['src'])[45:-4] + '-1920x1080.jpg')
    return htmls


async def download(image_url):
    async with httpx.AsyncClient() as client:
        tasks = [download_image(client, link) for link in image_url]
        await asyncio.gather(*tasks)


async def download_image(client, link):
    response = await client.get(link, headers=headers)
    # Replace the following line with your desired logic to save the image
    with open("/home/tej/Downloads/gamewallpapers/" + str(link)[37:], 'wb') as image:
        image.write(response.content)
        print("Image saved")


if __name__ == "__main__":
    asyncio.run(download(geturls(url)))
