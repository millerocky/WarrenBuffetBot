import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
RUB = 'RUB'
# Парсинг данных о котировках акций IT-сектора экономики Росиии
hhru_data = 'https://ru.investing.com/equities/headhunter-group-plc?cid=1166764'
hhru_page = requests.get(hhru_data, headers=HEADERS).text
hhru_soup = BeautifulSoup(hhru_page, 'html.parser')
hhru_convert = hhru_soup.findAll('span', {'class': 'text-2xl'})
hhru_rub = hhru_convert[0].text + RUB
hhru_name = 'HeadHunter ➡'

def show_hhru_name():
    '''
    :return: Название акции hhru
    '''
    return hhru_name

def show_headhunter():
    '''
    :return: Акция "HeadHunter"
    '''
    return hhru_rub

yandex_data = 'https://ru.investing.com/equities/yandex?cid=102063'
yandex_page = requests.get(yandex_data, headers=HEADERS).text
yandex_soup = BeautifulSoup(yandex_page, 'html.parser')
yandex_convert = yandex_soup.findAll('span', {'class': 'text-2xl'})
yandex_rub = yandex_convert[0].text + RUB
yandex_name = 'Яндекс ➡'

def show_yandex_name():
    '''
    :return: Название акции Яндекс
    '''
    return yandex_name

def show_yandex():
    '''
    :return: Акция "Яндекс"
    '''
    return yandex_rub

mailru_data = 'https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363'
mailru_page = requests.get(mailru_data, headers=HEADERS).text
mailru_soup = BeautifulSoup(mailru_page, 'html.parser')
mailru_convert = mailru_soup.findAll('span', {'class': 'text-2xl'})
mailru_rub = mailru_convert[0].text + RUB
mailru_name = 'Mail.ru ➡'

def show_mailru_name():
    '''
    :return: Название акции Mail.ru Group
    '''
    return mailru_name

def show_mailru():
    '''
    :return: Акция "Mail.ru"
    '''
    return mailru_rub

mts_data = 'https://ru.investing.com/equities/mts_rts'
mts_page = requests.get(mts_data, headers=HEADERS).text
mts_soup = BeautifulSoup(mts_page, 'html.parser')
mts_convert = mts_soup.findAll('span', {'class': 'text-2xl'})
mts_rub = mts_convert[0].text + RUB
mts_name = 'МТС ➡'

def show_mts_name():
    '''
    :return: Название акции МТС
    '''
    return mts_name

def show_mts():
    '''
    :return: Акция "МТС"
    '''
    return mts_rub

ozon_date = 'https://ru.investing.com/equities/ozon-holdings-plc?cid=1167498'
ozon_page = requests.get(ozon_date, headers=HEADERS).text
ozon_soup = BeautifulSoup(ozon_page, 'html.parser')
ozon_convert = ozon_soup.findAll('span', {'class': 'text-2xl'})
ozon_rub = ozon_convert[0].text + RUB
ozon_name = 'Ozon Holdings ➡'

def show_ozon_name():
    '''
    :return: Название акции Ozon Holding
    '''
    return ozon_name

def show_ozon():
    '''
    :return: Акция "Ozon Holdings"
    '''
    return ozon_rub

qiwi_data = 'https://ru.investing.com/equities/qiwi-plc?cid=960754'
qiwi_page = requests.get(qiwi_data, headers=HEADERS).text
qiwi_soup = BeautifulSoup(qiwi_page, 'html.parser')
qiwi_convert = qiwi_soup.findAll('span', {'class': 'text-2xl'})
qiwi_rub = qiwi_convert[0].text + RUB
qiwi_name = 'Qiwi ➡'

def show_qiwi_name():
    '''
    :return: Название акции QIWI
    '''
    return qiwi_name

def show_qiwi():
    '''
    :return: "Акция QIWI"
    '''
    return qiwi_rub

rosseti_data = 'https://ru.investing.com/equities/rosseti-ao'
rosseti_page = requests.get(rosseti_data, headers=HEADERS).text
rosseti_soup = BeautifulSoup(rosseti_page, 'html.parser')
rosseti_convert = rosseti_soup.findAll('span', {'class': 'text-2xl'})
rosseti_rub = rosseti_convert[0].text + RUB
rosseti_name = 'Россети ➡'

def show_rosseti_name():
    '''
    :return: Название акции Россети
    '''
    return rosseti_name

def show_rosseti():
    '''
    :return: Акция "Россети"
    '''
    return rosseti_rub

rostelecom_data = 'https://ru.investing.com/equities/rostelecom'
rostelecom_page = requests.get(rostelecom_data, headers=HEADERS).text
rostelecom_soup = BeautifulSoup(rostelecom_page, 'html.parser')
rostelecom_convert = rostelecom_soup.findAll('span', {'class': 'text-2xl'})
rostelecom_rub = rostelecom_convert[0].text + RUB
rostelecom_name = 'Ростелеком ➡'

def show_rostelecom_name():
    '''
    :return: Название акции Ростелеком
    '''
    return rostelecom_name

def show_rostelecom():
    '''
    :return: Акция "Ростелеком"
    '''
    return rostelecom_rub