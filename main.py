import requests
import translate
from translate import Translator
from pyowm import OWM
from requests import get




owm = OWM('8c32dd4e6171baabc661ac89852c5509')
mgr = owm.weather_manager()


ip = get('https://ipapi.co/ip/').text

def find_city_by_ip(ip=ip):
    try:
        response = requests.get(url= f'http://ip-api.com/json/{ip}').json()
        city = response.get('city')
        return city 
    except requests.exceptions.ConnectionError:
        print('[!] Please chel your connection!')
def find_country_lang_by_ip(ip=ip):
    try:
        response = requests.get(url= f'http://ip-api.com/json/{ip}').json()
        lang =response.get('countryCode')
        return lang 
    except requests.exceptions.ConnectionError:
        print('[!] Please chel your connection!')


def wather_in_your_city():
    observation = mgr.weather_at_place(str(find_city_by_ip()))
    w = observation.weather
    wather = w.detailed_status
    return f'{wather}'

def temp_in_your_city():
    observation = mgr.weather_at_place(str(find_city_by_ip()))
    w = observation.weather
    temp =  w.temperature('celsius')['temp']
    
    return f'{temp} C'

def translate():
    translator= Translator(from_lang="english",to_lang='ru')
    translation = translator.translate(wather_in_your_city())
def check_lang():
    if find_country_lang_by_ip() != 'RU' or 'UA':
        print(f'Wether: {wather_in_your_city()}\nTemp: {temp_in_your_city()}')
    elif find_country_lang_by_ip() == 'RU' or 'UA':
        print(f'Погода: {translate()}\nТемпература: {temp_in_your_city()}')
def main():
    check_lang()
    
      

if __name__ == '__main__':
    main()

