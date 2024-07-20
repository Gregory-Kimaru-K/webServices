from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import os

url = input('Url : ')

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    os.makedirs('bmsimages', exist_ok=True)

    img_urls = soup.find_all('img')

    for img_url in img_urls:
        img_src = img_url.get('src')

        if img_src:
            img_src = urljoin(url, img_src)
            img_name = os.path.basename(img_src)
            img_path = os.path.join('bmsimages', img_name)

            img_response = requests.get(img_src, stream=True)

            if img_response.status_code == 200:
                with open(img_path, 'wb') as file:
                    for chunk in img_response.iter_content(1024):
                        file.write(chunk)
                print(f'Saved : {img_name}')

else:
    print(f"Error : {response.status_code}")

