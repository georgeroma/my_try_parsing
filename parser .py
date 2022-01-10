import requests
from bs4 import BeautifulSoup 

URL = 'https://auto.ria.com/newauto/marka-lexus/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content (html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all ('a', class_='proposition_link')
    #print(items)
    cars=[]
    for item in items:
        cars.append({
            'title': item.find('span',class_='link').get_text(),
            #'link': item.find('a',class_='proposition_link').get('href')
            #'price': item.find('span',class_='green bold size22 tooltip-price').get_text()
            #'city': item.find('i',class_='i16_pin').find_next()()
            'city': item.find("i",class_="i16_pin").string,


        })

    #items = soup.find_all ('a', class_='proposition_link')
    print(cars)






def parse():
    html = get_html(URL)
    #print (html.text)
    get_content(html.text)


parse()
