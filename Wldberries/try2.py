import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import html

def compare_html():
    URL = r"https://www.wildberries.ru/seller/225613?sort=popular&page=1"
    HEADERS = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    req=requests.get(url=URL,headers=HEADERS)
    print(req.text)

    with open('req.html','w', encoding = "utf-8") as file:
        file.write(req.text)
#compare_html()

'''x=urlopen(r"https://www.wildberries.ru/seller/225613?sort=popular&page=1").read()
print(x)
with open('req2.html','wb') as file:
        file.write(x)'''


with open ('req.html',encoding='utf-8') as file:
    src = file.read()

soup=BeautifulSoup(src,'lxml')

#-------------------------------------------------------------
#all_brands=soup.find_all('strong',class_='brand-name')

#for item in all_brands:
    #print(item.text[:-2])
    
#-------------------------------------------------------------



#-------------------------------------------------------------
#products_name= soup.find_all("span", class_='goods-name') 

#for item in products_name:
    #print(item.text)
#-------------------------------------------------------------


#-------------------------------------------------------------
#links_products=soup.find_all('a',class_='product-card__main j-open-full-product-card')

#i=0
#for item in links_products:
    
    #links_products[i]=(r'https://www.wildberries.ru'+item.get('href'))
    #i+=1
#i=0

#for item in links_products:
    #print(item)

#print(len(links_products))
#-------------------------------------------------------------

'''items_lover_price=soup.find_all('ins',class_='lower-price')

for item in items_lover_price:
    print(item.text)
'''

products_ids=[]
def gets_id_product():  
    global products_ids      
    links_products=soup.find_all('a',class_='product-card__main j-open-full-product-card')
    count=0
    for item in links_products:   
        links_products=(item.get('href')[9:])

        links_products_list=[]
        for i in links_products:
            if i !='/':
                links_products_list.append(i)
            else:
                break
        #print(''.join(links_products_list))
        products_ids.append(''.join(links_products_list))
        count+=1
    print('Выведено id - ',count)
    
gets_id_product()
print(products_ids)           