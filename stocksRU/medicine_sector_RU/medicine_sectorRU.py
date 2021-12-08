import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
RUB = 'RUB'

# Парсинг данных о котировках акций медицинского сектора фондового рынка России
life_data = 'https://ru.investing.com/equities/pharmsynthez'
life_page = requests.get(life_data, headers=HEADERS).text
life_soup = BeautifulSoup(life_page, 'html.parser')
life_convert = life_soup.findAll('span', {'class': 'text-2xl'})
life_rub = life_convert[0].text + RUB
life_name = 'Life ➡'

def show_life_name():
    '''
    :return:
    '''
    return life_name

def show_life():
    '''
    :return: Акция "Life"
    '''
    return life_rub

iskj_data = 'https://ru.investing.com/equities/human-stem-cells-institute'
iskj_page = requests.get(iskj_data, headers=HEADERS).text
iskj_soup = BeautifulSoup(iskj_page, 'html.parser')
iskj_convert = iskj_soup.findAll('span', {'class': 'text-2xl'})
iskj_rub = iskj_convert[0].text + RUB
iskj_name = 'ISKJ ➡'

def show_iskj_name():
    '''
    :return: Название акции ISKJ
    '''
    return iskj_name

def show_iskj():
    '''
    :return: Акция "ISKJ"
    '''
    return iskj_rub

mdmg_data = 'https://ru.investing.com/equities/md-medical-drc?cid=1167487'
mdmg_page = requests.get(mdmg_data, headers=HEADERS).text
mdmg_soup = BeautifulSoup(mdmg_page, 'html.parser')
mdmg_convert = mdmg_soup.findAll('span', {'class': 'text-2xl'})
mdmg_rub = mdmg_convert[0].text + RUB
mdmg_name = 'MDMG ➡'

def show_mdmg_name():
    '''
    :return: Название акции MDMG
    '''
    return mdmg_name

def show_mdmg():
    '''
    :return: Акция "MDMG"
    '''
    return mdmg_rub

gemc_data = 'https://ru.investing.com/equities/united-medical-group-drc'
gemc_page = requests.get(gemc_data, headers=HEADERS).text
gemc_soup = BeautifulSoup(gemc_page, 'html.parser')
gemc_convert = gemc_soup.findAll('span', {'class': 'text-2xl'})
gemc_rub = gemc_convert[0].text + RUB
gemc_name = 'GEMC ➡'

def show_gemc_name():
    '''
    :return: Название акции GEMC
    '''
    return gemc_name

def show_gemc():
    '''
    :return: Акция "GEMC"
    '''
    return gemc_rub
