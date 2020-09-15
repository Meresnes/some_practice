import requests
import json

MY_API = 'ac1b1fb80956f9d9659b9c4acff36371'
City1 = 'Chicago, US'
City2 = 'Saint Petersburg, RU'
City3 = 'Bangladesh, BD'


def get_info_frm_api(tods):
    """Получение нужных данный из api"""
    info_data = [('name', ''), ('coord', 'lat'), ('coord', 'lon'), ('main', 'temp'), ('main', 'feels_like'),
                 ('timezone', ''),
                 ('sys', 'country')]
    k = []
    for key, value in info_data:
        if value:
            if key == 'main':
                k.append(int(tods[key][value] - 273))
            else:
                k.append(tods[key][value])
        else:
            if key == 'timezone':
                if int(tods[key]) < 0:
                    k.append(str(tods[key] / 3600))
                else:
                    k.append('+' + str(tods[key] / 3600))
            else:
                k.append(tods[key])
    return k


def json_create(k):
    """Создания json файла для вывода"""
    dict_json = {'name': '', 'coord': {'lat': '', 'lon': ''}, 'temp': {'temp': '', 'feels_like': ''}, 'utc': '',
                 'code': ''}
    x = 0
    for key in dict_json:
        if key == 'coord':
            dict_json[key]['lat'] = k[x]
            dict_json[key]['lon'] = k[x + 1]
            x += 1
        elif key == 'temp':
            dict_json[key]['temp'] = k[x]
            dict_json[key]['feels_like'] = k[x + 1]
            x += 1
        else:
            dict_json[key] = k[x]
        x += 1
    with open('{}_weather.json'.format(k[0]), 'w') as f:
        json.dump(dict_json, f)


def get_weather(city, api):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api))
    tods = r.json()

    k = get_info_frm_api(tods)
    print(
        'Город {}, координаты {} {}, темпереатура {}, по ощущениям {}. UTC{}, код страны {}'.format(k[0], k[1], k[2],
                                                                                                    k[3], k[4], k[5],
                                                                                                    k[6]))

    json_create(k)


get_weather(City1, MY_API)
get_weather(City2, MY_API)
get_weather(City3, MY_API)
