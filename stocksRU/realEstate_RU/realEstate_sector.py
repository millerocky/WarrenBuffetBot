import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
RUB = 'RUB'

# Парсинг данных о котировках акций промышленного сектора фондового рынка России
pik_data = 'https://ru.investing.com/equities/pik_rts'
pik_page = requests.get(pik_data, headers=HEADERS).text
pik_soup = BeautifulSoup(pik_page, 'html.parser')
pik_convert = pik_soup.findAll('span', {'class': 'text-2xl'})
pik_rub = pik_convert[0].text + RUB
pik_name = 'Группа ПИК ➡'

def show_pik_name():
    '''
    :return: Название акции Группа ПИК
    '''
    return pik_name

def show_pik():
    '''
    :return: Акция "Группа ПИК"
    '''
    return pik_rub

lsr_data = 'https://ru.investing.com/equities/lsr-group_rts'
lsr_page = requests.get(lsr_data, headers=HEADERS).text
lsr_soup = BeautifulSoup(lsr_page, 'html.parser')
lsr_convert = lsr_soup.findAll('span', {'class': 'text-2xl'})
lsr_rub = lsr_convert[0].text + RUB
lsr_name = 'ЛСР ➡'

def show_lsr_name():
    '''
    :return: Название акции ЛСР
    '''
    return lsr_name

def show_lsr():
    '''
    :return: Акция "Группа ЛСР"
    '''
    return lsr_rub