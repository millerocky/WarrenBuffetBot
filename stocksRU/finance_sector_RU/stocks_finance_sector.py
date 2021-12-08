import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
RUB = 'RUB'
# Парсинг данных о котировках акций финансового сектора экономики Росиии
vtb_data = 'https://ru.investing.com/equities/vtb_rts'
vtb_page = requests.get(vtb_data, headers=HEADERS).text
vtb_soup = BeautifulSoup(vtb_page, 'html.parser')
vtb_convert = vtb_soup.findAll('span', {'class': 'text-2xl'})
vtb_rub = vtb_convert[0].text + RUB
vtb_name = 'ВТБ ➡'

def show_vtb_name():
    '''
    :return: Название акции ВТБ Банк
    '''
    return vtb_name

def show_vtb():
    '''
    :return: Акция "ВТБ"
    '''
    return vtb_rub

tinkoff_bank_data = 'https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662'
tinkoff_bank_page = requests.get(tinkoff_bank_data, headers=HEADERS).text
tinkoff_bank_soup = BeautifulSoup(tinkoff_bank_page, 'html.parser')
tinkoff_bank_convert = tinkoff_bank_soup.findAll('span', {'class': 'text-2xl'})
tinkoff_bank_rub = tinkoff_bank_convert[0].text + RUB
tinkoff_bank_name = 'TCS Group Holding ➡'

def show_tinkoff_bank_name():
    '''
    :return: Название акции Тинькофф Банк
    '''
    return tinkoff_bank_name

def show_tinkoff():
    '''
    :return: Акция "Тинькофф Банк"
    '''
    return tinkoff_bank_rub

mkb_data = 'https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao'
mkb_page = requests.get(mkb_data, headers=HEADERS).text
mkb_soup = BeautifulSoup(mkb_page, 'html.parser')
mkb_convert = mkb_soup.findAll('span', {'class': 'text-2xl'})
mkb_rub = mkb_convert[0].text + RUB
mkb_name = 'МКБ ➡'

def show_mkb_name():
    '''
    :return: Название акции МКБ
    '''
    return mkb_name

def show_mkb():
    '''
    :return: Акция "МКБ"
    '''
    return mkb_rub

sber_data = 'https://ru.investing.com/equities/sberbank_rts'
sber_page = requests.get(sber_data, headers=HEADERS).text
sber_soup = BeautifulSoup(sber_page, 'html.parser')
sber_convert = sber_soup.findAll('span', {'class': 'text-2xl'})
sber_rub = sber_convert[0].text + RUB
sber_name = 'СБЕР ➡'

def show_sber_name():
    '''
    :return: Название акции СБЕР
    '''
    return sber_name

def show_sber():
    '''
    :return: Акция "Сбер"
    '''
    return sber_rub

sber_prevs_data = 'https://ru.investing.com/equities/sberbank-p_rts'
sber_prevs_page = requests.get(sber_prevs_data, headers=HEADERS).text
sber_prevs_soup = BeautifulSoup(sber_prevs_page, 'html.parser')
sber_prevs_convert = sber_prevs_soup.findAll('span', {'class': 'text-2xl'})
sber_prevs_rub = sber_prevs_convert[0].text + RUB
sber_prevs_name = 'СБЕР - привилегированные акции ➡'

def show_sber_prevs_name():
    '''
    :return: Название акции СБЕР прев.
    '''
    return sber_prevs_name

def show_sber_prevs():
    '''
    :return: Акция "Сбер - превелегированные акции"
    '''
    return sber_prevs_rub

afk_data = 'https://ru.investing.com/equities/afk-sistema_rts'
afk_page = requests.get(afk_data, headers=HEADERS).text
afk_soup = BeautifulSoup(afk_page, 'html.parser')
afk_convert = afk_soup.findAll('span', {'class': 'text-2xl'})
afk_rub = afk_convert[0].text + RUB
afk_name = 'АФК Система ➡'

def show_afk_name():
    '''
    :return: Название акции АФК Системы
    '''
    return afk_name

def show_afk():
    '''
    :return: Акция "АФК-ситсема"
    '''
    return afk_rub

spb_bank_data = 'https://ru.investing.com/equities/bank-st-petersbr_rts'
spb_bank_page = requests.get(spb_bank_data, headers=HEADERS).text
spb_bank_soup = BeautifulSoup(spb_bank_page, 'html.parser')
spb_bank_convert = spb_bank_soup.findAll('span', {'class': 'text-2xl'})
spb_bank_rub = spb_bank_convert[0].text + RUB
spb_bank_name = 'Банк Санкт-Петербург ➡'

def show_spb_bank_name():
    '''
    :return: Название акции СПБ биржы
    '''
    return spb_bank_name

def show_spb_bank():
    '''
    :return: Акция "СПБ Биржа"
    '''
    return spb_bank_rub