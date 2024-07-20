from bs4 import BeautifulSoup
import requests

url = input('Url : ')

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    title = soup.title.string
    print(f'Title : {title}')

    para = soup.find_all('p')
    for parag in para:
        print(parag.text)

else:
    print(f"Error {response.status_code}")
