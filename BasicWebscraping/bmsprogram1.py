from bs4 import BeautifulSoup
import requests

url = input('url : ')

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'lxml')
    links = soup.find_all('a')
    for link in links:
        print(link['href'])
    
    slink = soup.find('a')
    print(slink['href'])

    paras = soup.find_all('p')

    for para in paras:
        print(para.text)

    heads = soup.find_all('h1')
    heads2 = soup.find_all('h2')
    heads3 = soup.find_all('h3')

    for head in heads:
        print(head.text)
    for head2 in heads2:
        print(head2.text)
    for head3 in heads3:
        print(head3.text)