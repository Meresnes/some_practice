import requests
from bs4 import BeautifulSoup
import csv
import os

#url страницы
#URL = 'https://auto.ria.com/newauto/marka-lexus/'

#для защиты от бана
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko', 'acept': '*/*'}
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'


def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span',class_='mhide')

    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1



#Парсим контент на странице
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    #Блок для поиска нужных данных (всех!)
    items = soup.find_all('div', class_='proposition')

    cars = []
    for item in items:

        cars.append({
            'title': item.find('h3', class_='proposition_name').get_text(strip=True),
            'link': HOST + item.find('a').get('href'),
            'usd_price': item.find('div', class_='proposition_price').find_next('span', class_='size18').get_text(strip=True),
            'uah_price': item.find('div', class_='proposition_price').find_next('span', class_= 'grey size13').get_text(),
            'city': item.find('div', class_='proposition_region').find_next('strong').get_text(),
        })
    return cars

def save_file(items,path):
    try :
        with open(path,'w', newline= '') as file:
            writer = csv.writer(file,delimiter = ';')
            writer.writerow(['Марка','Ссылка','Цена в $','Цена в UAH','Город'])
            for item in items:
                writer.writerow([item['title'],item['link'],item['usd_price'],item['uah_price'],item['city']])
    except PermissionError:
        print('Закройте csv фалй!!!!')
#Основная ф-ия
def parse():
    URL = input('Введите URL: ')
    URL = URL.strip()
    html = get_html(URL)
    print('Парсинг возможен только на вкладке \'Новые авто!\' ')
    #Тут проверяем статус код, а потом уже делаем условие
    # print(html.status_code)
    if html.status_code == 200:
        #get_content(html.text)

        pages_count = get_pages_count(html.text)
        cars = []

        for page in range(1,pages_count+1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL,params={'page':page})
            cars.extend(get_content(html.text))
        save_file(cars,FILE)
        print(f'Получено {len(cars)} автомобилей')
        os.startfile(FILE)
    else:
        print('Error!')

parse()

