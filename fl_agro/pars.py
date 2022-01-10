from os import replace
from typing import Text
import requests
from bs4 import BeautifulSoup
import time
import pandas

URL=r'https://agroserver.ru/semena/Y2l0eT18cmVnaW9uPXxjb3VudHJ5PXxtZXRrYT18c29ydD0x/1/'
def compare_html(URL,filename):
    
    HEADERS={"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    response = requests.get(url=URL,headers=HEADERS)
    with open(filename,'w', encoding = "utf-8") as file:
        file.write(response.text)

#compare_html()


with open ('req.html',encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src,'lxml')




links_arr=[]
def search_links():
    global links_arr
    find_links=soup.find_all('div', class_='th')

    
    for item in find_links:
        #print(item)
        x=item.find_all('a')
        for lin in x:
            links_arr.append(r'https://agroserver.ru'+lin.get('href'))

    del links_arr[0]
search_links()
#print((links_arr))  


'''for i in range (41,51):
    filename= str(i)+'_product_html.html'
    URL=links_arr[i]
    compare_html(URL,filename)
    print(i)
    time.sleep(2)'''


def compare_category_name(filename):
    with open(filename,encoding="utf-8") as file:
        src=file.read()
    soup=BeautifulSoup(src,'lxml')

    category_product=soup.find('div', class_='nav').find_next('a').find_next('a').find_next('a').find_next('a').text
    print(category_product)
    return category_product

#compare_category_name(filename)


def compare_product_name(filename):

    with open(filename,encoding="utf-8") as file:
        src=file.read()
    soup=BeautifulSoup(src,'lxml')

    name_product=soup.find('div', class_='nav').find_next('a').find_next('a').find_next('a').find_next('a').find_next().text
    print(name_product)
    return(name_product)
#compare_product_name()


def compare_product_description(filename):
    with open(filename, encoding="utf-8") as file:
        src = file.read()
    soup=BeautifulSoup(src,'lxml')

    descriprion_product=soup.find('div', class_='text')
    print(descriprion_product.text)
    return(descriprion_product.text)

#compare_product_description()


def compare_price_product(filename):
    with open(filename,encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src,'lxml')
    product_price=soup.find('div',class_='mprice').text
    print(product_price)
    product_price=str(product_price)
    try :
        product_price[0]=='ц' 
    except:
        product_price='Цена не указана'
    return product_price

#compare_price_product()#r'1_product_html.html'


def compare_telephons(filename):
    with open(filename,encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src,'lxml')
    product_telephones=soup.find('div',class_='bl phone ico_call').text
    
    product_telephones=list(product_telephones)
    
    for i in range(len(product_telephones)):
        try:
            if product_telephones[i] == '\n' and product_telephones[(i+1)] != '+':
                del product_telephones[i]

            
                
        except:
            try:
                if product_telephones[i] == '\n' and product_telephones[(i-1)] == '\n':
                    del product_telephones[i]
            except:
                pass
        try:
            if product_telephones[i] == '\n' and product_telephones[(i+1)] == '\n':
                del product_telephones[i]    
        except:
            pass
        if product_telephones[0] == '\n' :
            del product_telephones[0]
        if product_telephones[len(product_telephones)-1] == '\n' :
            del product_telephones[len(product_telephones)-1]
        
        try:
            if product_telephones[i] == '\n' and product_telephones[(i+1)] != '+':
                del product_telephones[i]

            
                
        except:
            try:
                if product_telephones[i] == '\t' and product_telephones[(i-1)] == '\t':
                    del product_telephones[i]
            except:
                pass
        try:
            if product_telephones[i] == '\t' and product_telephones[(i+1)] == '\t':
                del product_telephones[i]    
        except:
            pass
        if product_telephones[0] == '\t' :
            del product_telephones[0]
        if product_telephones[len(product_telephones)-1] == '\t' :
            del product_telephones[len(product_telephones)-1]
    product_telephones=''.join(product_telephones)
    print((product_telephones))
    return product_telephones
#compare_telephons()#r'1_product_html.html'

def compare_seller_name(filename):
    with open(filename,encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src,'lxml')
    seller_name = soup.find('a',class_='personal_org_menu ajs').text
    print(seller_name)
    return(seller_name)

#compare_seller_name()#r'2_product_html.html'

def compare_adres(filename):
    with open(filename,encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src,'lxml')
    adres=soup.find('div',class_='bl ico_location').text
    #adres=list(adres)
    adres = adres.replace('\t','')
    adres = adres.replace('\n','')
    print(adres)
    return adres
#compare_adres()#r'2_product_html.html'

filenames=[]
for i in range (0,50):
    filenames.append(str(i)+'_product_html.html')

print(filenames)

df = {'Название категории': }
itog=[]

itog.append(compare_category_name(filenames[0])) #1
itog.append(compare_product_name(filenames[0])) #2
itog.append(compare_product_description(filenames[0])) #3
itog.append(compare_price_product(filenames[0])) #4
itog.append(compare_seller_name(filenames[0])) #5
itog.append(compare_telephons(filenames[0])) #6
itog.append(compare_adres(filenames[0])) #7
itog.append(links_arr[0])#8

print(itog)
itog.pandas.to_excel('./teams.xlsx', sheet_name='Budgets', index=False)