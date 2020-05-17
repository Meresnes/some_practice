import requests
from bs4 import BeautifulSoup
import csv
import os

HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 YaBrowser/20.4.1.304 Yowser/2.5 Safari/537.36', 'acept' :'*/*'}
URL = 'https://www.kinoafisha.info/rating/movies/'
FILE = 'top_films.csv'

def get_html(url,params=None):
    r = requests.get(url,headers = HEADERS, params = params)
    return r.text


def get_pages(html):
    soup = BeautifulSoup(html,'html.parser')
    pagination = soup.find_all('a',class_='pager_item')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        1


def get_content(html,k):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_='films_padding')
    film_list = []
    
    for item in items:
        
        try:
            k += 0.5
            film_list.append({
            'number': int(k),
            'title': item.find('a',class_='films_name ref').get_text(),
            'rate': item.find('span',class_='rating_num').get_text(),
            'year': item.find('span',class_='films_info').get_text()[:4],
            'country': item.find('span',class_='films_info').get_text(strip=True)[6:],
            'genre': item.find('span',class_='films_info').find_next('span',class_='films_info').get_text(strip=True),
            'regisseur': item.find('a',class_='films_info_link').get_text(),
            
            })
        except:
            pass
        
    return film_list

def save_films(items,path):
    try :
        with open(path,'w', newline= '') as file:
            writer = csv.writer(file,delimiter = ';')
            writer.writerow(['Номер','Назавние','Рейтинг','Год','Страна','Жанр','Режисёр'])
            for item in items:
                writer.writerow([item['number'],item['title'],item['rate']+'*',item['year'],item['country'],item['genre'],item['regisseur']])
    except PermissionError:
        print('Закройте csv файл')
def parsing():
    
    html = get_html(URL)
    #pages = get_pages(html)
    pages = int(input('Введите кол-во страниц: '))
    film = []
    k = 0
    for page in range(0,pages):
        
        print(f'Parsin {page+1} page of {pages}...')
        html = get_html(URL,params={'page':page})
        film.extend(get_content(html,k))
        k += 100
    
    save_films(film,FILE)
    os.startfile(FILE)
    

parsing()   
#get_content(html)
#print(get_pages(html))
#print(n)
