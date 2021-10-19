import requests
from bs4 import BeautifulSoup

# Парсинг данных о котировках акций IT сектора фондового рынка России
IT_rub = {}
IT_name = []
'''=================================================================================================================================================='''
hhru_data = 'https://ru.investing.com/equities/headhunter-group-plc?cid=1166764'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
hhru_page = requests.get(hhru_data, headers=headers).text
hhru_soup = BeautifulSoup(hhru_page, 'html.parser')
hhru_convert = hhru_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
hhru_rub = hhru_convert[0].text

hhru_name_data = 'https://ru.investing.com/equities/headhunter-group-plc?cid=1166764'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
hhru_name_page = requests.get(hhru_name_data, headers=headers).text
hhru_name_soup = BeautifulSoup(hhru_name_page, 'html.parser')
hhru_name_convert = hhru_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
hhru_name = hhru_name_convert[0].text

IT_name.append(hhru_name)
IT_rub[hhru_name] = hhru_rub
'''==========================================================================================================================================='''
yandex_data = 'https://ru.investing.com/equities/yandex?cid=102063'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
yandex_page = requests.get(yandex_data, headers=headers).text
yandex_soup = BeautifulSoup(yandex_page, 'html.parser')
yandex_convert = yandex_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
yandex_rub = yandex_convert[0].text

yandex_name_data = 'https://ru.investing.com/equities/yandex?cid=102063'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
yandex_name_page = requests.get(yandex_name_data, headers=headers).text
yandex_name_soup = BeautifulSoup(yandex_name_page, 'html.parser')
yandex_name_convert = yandex_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
yandex_name = yandex_name_convert[0].text

IT_name.append(yandex_name)
IT_rub[yandex_name] = yandex_rub
'''===================================================================================================================================================='''
mailru_data = 'https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
mailru_page = requests.get(mailru_data, headers=headers).text
mailru_soup = BeautifulSoup(mailru_page, 'html.parser')
mailru_convert = mailru_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mailru_rub = mailru_convert[0].text

mailru_name_data = 'https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
mailru_name_page = requests.get(mailru_name_data, headers=headers).text
mailru_name_soup = BeautifulSoup(mailru_name_page, 'html.parser')
mailru_name_convert = mailru_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
mailru_name = mailru_name_convert[0].text

IT_name.append(mailru_name)
IT_rub[mailru_name] = mailru_rub
'''============================================================================================================================='''
mts_data = 'https://ru.investing.com/equities/mts_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
mts_page = requests.get(mts_data, headers=headers).text
mts_soup = BeautifulSoup(mts_page, 'html.parser')
mts_convert = mts_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mts_rub = mts_convert[0].text

mts_name_data = 'https://ru.investing.com/equities/mts_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
mts_name_page = requests.get(mts_name_data, headers=headers).text
mts_name_soup = BeautifulSoup(mts_name_page, 'html.parser')
mts_name_convert = mts_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
mts_name = mts_name_convert[0].text

IT_name.append(mts_name)
IT_rub[mts_name] = mts_rub
'''=========================================================================='''
ozon_date = 'https://ru.investing.com/equities/ozon-holdings-plc?cid=1167498'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
ozon_page = requests.get(ozon_date, headers=headers).text
ozon_soup = BeautifulSoup(ozon_page, 'html.parser')
ozon_convert = ozon_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
ozon_rub = ozon_convert[0].text

ozon_name_data = 'https://ru.investing.com/equities/ozon-holdings-plc?cid=1167498'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
ozon_name_page = requests.get(ozon_name_data, headers=headers).text
ozon_name_soup = BeautifulSoup(ozon_name_page, 'html.parser')
ozon_name_convert = ozon_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
ozon_name = ozon_name_convert[0].text

IT_name.append(ozon_name)
IT_rub[ozon_name] = ozon_rub
'''================================================================='''
qiwi_data = 'https://ru.investing.com/equities/qiwi-plc?cid=960754'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
qiwi_page = requests.get(qiwi_data, headers=headers).text
qiwi_soup = BeautifulSoup(qiwi_page, 'html.parser')
qiwi_convert = qiwi_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
qiwi_rub = qiwi_convert[0].text

qiwi_name_data = 'https://ru.investing.com/equities/qiwi-plc?cid=960754'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
qiwi_name_page = requests.get(qiwi_name_data, headers=headers).text
qiwi_name_soup = BeautifulSoup(qiwi_name_page, 'html.parser')
qiwi_name_convert = qiwi_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
qiwi_name = qiwi_name_convert[0].text

IT_name.append(qiwi_name)
IT_rub[qiwi_name] = qiwi_rub
'''============================================================================'''
rosseti_data = 'https://ru.investing.com/equities/rosseti-ao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rosseti_page = requests.get(rosseti_data, headers=headers).text
rosseti_soup = BeautifulSoup(rosseti_page, 'html.parser')
rosseti_convert = rosseti_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rosseti_rub = rosseti_convert[0].text

rosseti_name_data = 'https://ru.investing.com/equities/rosseti-ao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rosseti_name_page = requests.get(rosseti_name_data, headers=headers).text
rosseti_name_soup = BeautifulSoup(rosseti_name_page, 'html.parser')
rosseti_name_convert = rosseti_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
rosseti_name = rosseti_name_convert[0].text

IT_name.append(rosseti_name)
IT_rub[rosseti_name] = rosseti_rub
'''============================================================'''
rostelecom_data = 'https://ru.investing.com/equities/rostelecom'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rostelecom_page = requests.get(rostelecom_data, headers=headers).text
rostelecom_soup = BeautifulSoup(rostelecom_page, 'html.parser')
rostelecom_convert = rostelecom_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rostelecom_rub = rostelecom_convert[0].text

rostelecom_name_data = 'https://ru.investing.com/equities/rostelecom'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rostelecom_name_page = requests.get(rostelecom_name_data, headers=headers).text
rostelecom_name_soup = BeautifulSoup(rostelecom_name_page, 'html.parser')
rostelecom_name_convert = rostelecom_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
rostelecom_name = rostelecom_name_convert[0].text

IT_name.append(rostelecom_name)
IT_rub[rostelecom_name] = rostelecom_rub
'''==================================================='''


IT_name.sort()