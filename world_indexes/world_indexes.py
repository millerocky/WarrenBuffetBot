import requests
from bs4 import BeautifulSoup

prices_index = {}
array_index = []

# Парсинг данных о котировках мировых индексов

MOEX_index_data = 'https://ru.investing.com/indices/mcx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MOEX_index_page = requests.get(MOEX_index_data, headers=headers).text
MOEX_index_soup = BeautifulSoup(MOEX_index_page, 'html.parser')
MOEX_index_convert = MOEX_index_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
MOEX_index_rub = MOEX_index_convert[0].text

MOEX_index_name_data =  'https://ru.investing.com/indices/mcx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MOEX_index_name_page = requests.get(MOEX_index_name_data, headers=headers).text
MOEX_index_name_soup = BeautifulSoup(MOEX_index_name_page, 'html.parser')
MOEX_index_name_convert = MOEX_index_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
MOEX_index_name = MOEX_index_name_convert[0].text

array_index.append(MOEX_index_name)
prices_index[MOEX_index_name] = MOEX_index_rub
'============================================================================'
SnP500_index_data = 'https://ru.investing.com/indices/us-spx-500'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SnP500_index_page = requests.get(SnP500_index_data, headers=headers).text
SnP500_index_soup = BeautifulSoup(SnP500_index_page, 'html.parser')
SnP500_index_convert = SnP500_index_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
SnP500_index = SnP500_index_convert[0].text

SnP500_index_name_data = 'https://ru.investing.com/indices/us-spx-500'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SnP500_index_name_page = requests.get(SnP500_index_name_data, headers=headers).text
SnP500_index_name_soup = BeautifulSoup(SnP500_index_name_page, 'html.parser')
SnP500_index_name_convert = SnP500_index_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
SnP500_index_name = SnP500_index_name_convert[0].text

array_index.append(SnP500_index_name)
prices_index[SnP500_index_name] = SnP500_index
'================================================================'
NASDAQ_index_data = 'https://ru.investing.com/indices/nq-100'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
NASDAQ_index_page = requests.get(NASDAQ_index_data, headers=headers).text
NASDAQ_index_soup = BeautifulSoup(NASDAQ_index_page, 'html.parser')
NASDAQ_index_convert = NASDAQ_index_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
NASDAQ_index = NASDAQ_index_convert[0].text

NASDAQ_index_name_data = 'https://ru.investing.com/indices/nq-100'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
NASDAQ_index_name_page = requests.get(NASDAQ_index_name_data, headers=headers).text
NASDAQ_index_name_soup = BeautifulSoup(NASDAQ_index_name_page, 'html.parser')
NASDAQ_index_name_convert = NASDAQ_index_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
NASDAQ_index_name = NASDAQ_index_name_convert[0].text

array_index.append(NASDAQ_index_name)
prices_index[NASDAQ_index_name] = NASDAQ_index
'======================================================================================='
SHANGAI_index_data = 'https://ru.investing.com/indices/shanghai-composite'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SHANGAI_index_page = requests.get(SHANGAI_index_data, headers=headers).text
SHANGAI_index_soup = BeautifulSoup(SHANGAI_index_page, 'html.parser')
SHANGAI_index_convert = SHANGAI_index_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
SHANGAI_index = SHANGAI_index_convert[0].text

SHANGAI_index_name_data = 'https://ru.investing.com/indices/shanghai-composite'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SHANGAI_index_name_page = requests.get(SHANGAI_index_name_data, headers=headers).text
SHANGAI_index_name_soup = BeautifulSoup(SHANGAI_index_name_page, 'html.parser')
SHANGAI_index_name_convert = SHANGAI_index_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
SHANGAI_index_name = SHANGAI_index_name_convert[0].text

array_index.append(SHANGAI_index_name)
prices_index[SHANGAI_index_name] = SHANGAI_index
'=================================================================='