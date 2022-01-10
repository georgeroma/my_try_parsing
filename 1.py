from bs4 import BeautifulSoup
import requests

def parse():
  URL = 'https://www.wildberries.ru/seller/225613?sort=newly&page=2'
  HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
  }

  response = requests.get(URL,headers = HEADERS)
  print(response.text)
  with open('req.html','w', encoding = "utf-8") as file:
        file.write(response.text)
parse()