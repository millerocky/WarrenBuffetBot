import requests
from bs4 import BeautifulSoup

# Создаю словарь с данными о котировках компаний-эмитентов
IT_rub = {}

# Создаю массив с данными о названиях компаний-эмитентов для того чтобы осуществить вывод сортировку по алфавиту
IT_name = []

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

# Парсинг данных о котировках акций IT-сектора экономики Росиии
hhru_data = 'https://ru.investing.com/equities/headhunter-group-plc?cid=1166764'
hhru_page = requests.get(hhru_data, headers=HEADERS).text
hhru_soup = BeautifulSoup(hhru_page, 'html.parser')
hhru_convert = hhru_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
hhru_rub = hhru_convert[0].text
hhru_name = 'HeadHunter'
IT_name.append(hhru_name)
IT_rub[hhru_name] = hhru_rub


yandex_data = 'https://ru.investing.com/equities/yandex?cid=102063'
yandex_page = requests.get(yandex_data, headers=HEADERS).text
yandex_soup = BeautifulSoup(yandex_page, 'html.parser')
yandex_convert = yandex_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
yandex_rub = yandex_convert[0].text
yandex_name = 'Яндекс'
IT_name.append(yandex_name)
IT_rub[yandex_name] = yandex_rub


mailru_data = 'https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363'
mailru_page = requests.get(mailru_data, headers=HEADERS).text
mailru_soup = BeautifulSoup(mailru_page, 'html.parser')
mailru_convert = mailru_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mailru_rub = mailru_convert[0].text
mailru_name = 'Mail.ru'
IT_name.append(mailru_name)
IT_rub[mailru_name] = mailru_rub


mts_data = 'https://ru.investing.com/equities/mts_rts'
mts_page = requests.get(mts_data, headers=HEADERS).text
mts_soup = BeautifulSoup(mts_page, 'html.parser')
mts_convert = mts_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mts_rub = mts_convert[0].text
mts_name = 'МТС'
IT_name.append(mts_name)
IT_rub[mts_name] = mts_rub


ozon_date = 'https://ru.investing.com/equities/ozon-holdings-plc?cid=1167498'
ozon_page = requests.get(ozon_date, headers=HEADERS).text
ozon_soup = BeautifulSoup(ozon_page, 'html.parser')
ozon_convert = ozon_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
ozon_rub = ozon_convert[0].text
ozon_name = 'Ozon Holdings'
IT_name.append(ozon_name)
IT_rub[ozon_name] = ozon_rub


qiwi_data = 'https://ru.investing.com/equities/qiwi-plc?cid=960754'
qiwi_page = requests.get(qiwi_data, headers=HEADERS).text
qiwi_soup = BeautifulSoup(qiwi_page, 'html.parser')
qiwi_convert = qiwi_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
qiwi_rub = qiwi_convert[0].text
qiwi_name = 'Qiwi'
IT_name.append(qiwi_name)
IT_rub[qiwi_name] = qiwi_rub


rosseti_data = 'https://ru.investing.com/equities/rosseti-ao'
rosseti_page = requests.get(rosseti_data, headers=HEADERS).text
rosseti_soup = BeautifulSoup(rosseti_page, 'html.parser')
rosseti_convert = rosseti_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rosseti_rub = rosseti_convert[0].text
rosseti_name = 'Россети'
IT_name.append(rosseti_name)
IT_rub[rosseti_name] = rosseti_rub


rostelecom_data = 'https://ru.investing.com/equities/rostelecom'
rostelecom_page = requests.get(rostelecom_data, headers=HEADERS).text
rostelecom_soup = BeautifulSoup(rostelecom_page, 'html.parser')
rostelecom_convert = rostelecom_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rostelecom_rub = rostelecom_convert[0].text
rostelecom_name = 'Ростелеком'
IT_name.append(rostelecom_name)
IT_rub[rostelecom_name] = rostelecom_rub


IT_name.sort()