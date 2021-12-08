import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
RUB = 'RUB'

# Парсинг данных о котировках акций реального сектора экономики Росиии
magnit_data = 'https://ru.investing.com/equities/magnit_rts'
magnit_page = requests.get(magnit_data, headers=HEADERS).text
magnit_soup = BeautifulSoup(magnit_page, 'html.parser')
magnit_convert = magnit_soup.findAll('span', {'class': 'text-2xl'})
magnit_rub = magnit_convert[0].text + RUB
magnit_name = 'Магнит ➡'

def show_magnit_name():
    '''
    :return: Название акции Магнит
    '''
    return magnit_name

def show_magnit():
    '''
    :return: Акция "Магнит"
    '''
    return magnit_rub

x5group_data = 'https://ru.investing.com/equities/x5-retail-grp?cid=1061926'
x5group_page = requests.get(x5group_data, headers=HEADERS).text
x5group_soup = BeautifulSoup(x5group_page, 'html.parser')
x5group_convert = x5group_soup.findAll('span', {'class': 'text-2xl'})
x5group_rub = x5group_convert[0].text + RUB
x5group_name = 'X5 Retail Group ➡'

def show_x5group_name():
    '''
    :return: Название акции X5 Group
    '''
    return x5group_name

def show_x5group():
    '''
    :return: Акция "X5Retail Group"
    '''
    return x5group_rub

detskiy_mir_data = 'https://ru.investing.com/equities/detskiy-mir-pao'
detskiy_mir_page = requests.get(detskiy_mir_data, headers=HEADERS).text
detskiy_mir_soup = BeautifulSoup(detskiy_mir_page, 'html.parser')
detskiy_mir_convert = detskiy_mir_soup.findAll('span', {'class': 'text-2xl'})
detskiy_mir_rub = detskiy_mir_convert[0].text + RUB
detskiy_mir_name = 'Детский мир ➡'

def show_detskiy_mir_name():
    '''
    :return: Название акции Детский мир
    '''
    return detskiy_mir_name

def show_detskiy_mir():
    '''
    :return: Акция "Деский мир"
    '''
    return detskiy_mir_rub

fix_price_data = 'https://ru.investing.com/equities/fix-price-group-drc?cid=1171256'
fix_price_page = requests.get(fix_price_data, headers=HEADERS).text
fix_price_soup = BeautifulSoup(fix_price_page, 'html.parser')
fix_price_convert = fix_price_soup.findAll('span', {'class': 'text-2xl'})
fix_price_rub = fix_price_convert[0].text + RUB
fix_price_name = 'Fix Price Group ➡'

def show_fix_price_name():
    '''
    :return: Название акции Fix Price
    '''
    return fix_price_name

def show_fix_price():
    '''
    :return: Акция "Fix Price"
    '''
    return fix_price_rub

mvideo_data = 'https://ru.investing.com/equities/mvideo_rts'
mvideo_page = requests.get(mvideo_data, headers=HEADERS).text
mvideo_soup = BeautifulSoup(mvideo_page, 'html.parser')
mvideo_convert = mvideo_soup.findAll('span', {'class': 'text-2xl'})
mvideo_rub = mvideo_convert[0].text + RUB
mvideo_name = 'МВидео ➡'

def show_mvideo_name():
    '''
    :return: Название акции МВидео
    '''
    return mvideo_name

def show_mvideo():
    '''
    :return: Акция "МВидео"
    '''
    return mvideo_rub

cherkizovo_data = 'https://ru.investing.com/equities/gruppa-cherkizovo'
cherkizovo_page = requests.get(cherkizovo_data, headers=HEADERS).text
cherkizovo_soup = BeautifulSoup(cherkizovo_page, 'html.parser')
cherkizovo_convert = cherkizovo_soup.findAll('span', {'class': 'text-2xl'})
cherkizovo_rub = cherkizovo_convert[0].text + RUB
cherkizovo_name = 'Черкизово ➡'

def show_cherkizovo_name():
    '''
    :return: Название акции ОАО Черкизово
    '''
    return cherkizovo_name

def show_cherkizovo():
    '''
    :return: Акция "ОАО Группа Черкизово"
    '''
    return cherkizovo_rub