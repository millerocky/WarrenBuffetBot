import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
RUB = 'RUB'
USD = 'USD'

# Парсинг данных о котировках мировых индексов
MOEX_index_data = 'https://ru.investing.com/indices/mcx'
MOEX_index_page = requests.get(MOEX_index_data, headers=HEADERS).text
MOEX_index_soup = BeautifulSoup(MOEX_index_page, 'html.parser')
MOEX_index_convert = MOEX_index_soup.findAll('span', {'class': 'text-2xl'})
MOEX_index_rub = MOEX_index_convert[0].text + RUB
MOEX_index_name = 'MOEX ➡'

def show_MOEX_name():
    '''
    :return: Название Индекса МосБиржы
    '''
    return MOEX_index_name

def show_MOEX():
    '''
    :return: Индекс МосБиржы
    '''
    return MOEX_index_rub

SnP500_index_data = 'https://ru.investing.com/indices/us-spx-500'
SnP500_index_page = requests.get(SnP500_index_data, headers=HEADERS).text
SnP500_index_soup = BeautifulSoup(SnP500_index_page, 'html.parser')
SnP500_index_convert = SnP500_index_soup.findAll('span', {'class': 'text-2xl'})
SnP500_index = SnP500_index_convert[0].text + USD
SnP500_index_name = 'S&P 500 ➡'

def show_SnP500_name():
    '''
    :return: Название Индекса S&P500
    '''
    return SnP500_index_name

def show_snp500():
    '''
    :return: Индекс 500 лучших компаний Америки
    '''
    return SnP500_index

NASDAQ_index_data = 'https://ru.investing.com/indices/nq-100'
NASDAQ_index_page = requests.get(NASDAQ_index_data, headers=HEADERS).text
NASDAQ_index_soup = BeautifulSoup(NASDAQ_index_page, 'html.parser')
NASDAQ_index_convert = NASDAQ_index_soup.findAll('span', {'class': 'text-2xl'})
NASDAQ_index = NASDAQ_index_convert[0].text + USD
NASDAQ_index_name = 'NASDAQ ➡'

def show_NASDAQ_name():
    '''
    :return: Название Биржевого индекса Америки NASDAQ
    '''
    return NASDAQ_index_name

def show_nasdaq():
    '''
    :return: Биржевой индекс Америки NASDAQ
    '''
    return NASDAQ_index

SHANGAI_index_data = 'https://ru.investing.com/indices/shanghai-composite'
SHANGAI_index_page = requests.get(SHANGAI_index_data, headers=HEADERS).text
SHANGAI_index_soup = BeautifulSoup(SHANGAI_index_page, 'html.parser')
SHANGAI_index_convert = SHANGAI_index_soup.findAll('span', {'class': 'text-2xl'})
SHANGAI_index = SHANGAI_index_convert[0].text + USD
SHANGAI_index_name = 'Shanghai Composite ➡'

def show_SHANGAI_name():
    '''
    :return: Название Бииржевого индекса Китая
    '''
    return SHANGAI_index_name

def show_shanghai():
    '''
    :return: Бииржевой индекс Китая
    '''
    return SHANGAI_index