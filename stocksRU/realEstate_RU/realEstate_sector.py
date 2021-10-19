import requests
from bs4 import BeautifulSoup

# Парсинг данных о котировках акций промышленного сектора фондового рынка России
stocks_industrial_rub = {}
stocks_industrial_name = []

'================================================================================================================================='
pik_data = 'https://ru.investing.com/equities/pik_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
pik_page = requests.get(pik_data, headers=headers).text
pik_soup = BeautifulSoup(pik_page, 'html.parser')
pik_convert = pik_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
pik_rub = pik_convert[0].text

pik_name_data = 'https://ru.investing.com/equities/pik_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
pik_name_page = requests.get(pik_name_data, headers=headers).text
pik_name_soup = BeautifulSoup(pik_name_page, 'html.parser')
pik_name_convert = pik_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
pik_name = pik_name_convert[0].text

stocks_industrial_name.append(pik_name)
stocks_industrial_rub[pik_name] = pik_rub
'====================================================================================================================='
lsr_data = 'https://ru.investing.com/equities/lsr-group_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
lsr_page = requests.request(lsr_data, headers=headers).text
lsr_soup = BeautifulSoup(lsr_page, 'html.parser')
lsr_convert = lsr_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
lsr_rub = lsr_convert[0].text

lsr_name_data = 'https://ru.investing.com/equities/lsr-group_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
lsr_name_page = requests.get(lsr_name_data, headers=headers).text
lsr_name_soup = BeautifulSoup(lsr_name_page, 'html.parser')
lsr_name_convert = lsr_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
lsr_name = lsr_name_convert[0].text

stocks_industrial_name.append(lsr_name)
stocks_industrial_rub[lsr_name] = lsr_rub
'=========================================================================================================='
