from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import os

url = input('Url : ')

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    os.makedirs('images', exist_ok=True)

    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_url = img_tag.get('src')

        if img_url:
            img_url = urljoin(url, img_url)
            img_name = os.path.basename(img_url)
            img_path = os.path.join('images', img_name)
            img_response = requests.get(img_url, stream=True)

            if img_response.status_code == 200:
                with open(img_path, 'wb') as file:
                    for chunk in img_response.iter_content(1024):
                        file.write(chunk)
                print(f'Saved {img_name}')

else:
    print(f'error {response.status_code}')