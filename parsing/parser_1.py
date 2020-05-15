import requests
from bs4 import BeautifulSoup

#url страницы
URL = 'https://auto.ria.com/newauto/marka-jeep/'

#для защиты от бана
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko', 'acept' :'*/*'}
HOST = 'https://auto.ria.com'

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

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
            'usd_price': (item.find('div', class_='proposition_price')).find('span').get_text(strip=True),
            'uah_price': item.find('div', class_='proposition_price').find_next('span',class_='size13').get_text(strip=True),
            'city': item.find('div', class_='proposition_region').find_next('strong').get_text(),
        })
    return cars

#Основная функция
def parse():
    html = get_html(URL)

    #Тут проверяем статус код, а потом уже делаем условие
    # print(html.status_code)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error!')

parse()

