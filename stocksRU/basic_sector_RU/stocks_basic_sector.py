import requests
from bs4 import BeautifulSoup

# Создаю словарь с данными о котировках компаний-эмитентов
stocksBasic_data = {}

# Создаю массив с данными о названиях компаний-эмитентов для того чтобы осуществить вывод сортировку по алфавиту
stocksBasic_name = []

# Парсинг данных о котировках акций реального сектора экономики Росиии
Magnit_data = 'https://ru.investing.com/equities/magnit_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Magnit_page = requests.get(Magnit_data, headers=headers).text
Magnit_soup = BeautifulSoup(Magnit_page, 'html.parser')
Magnit_convert = Magnit_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Magnit_rub = Magnit_convert[0].text

Magnit_name_data = 'https://ru.investing.com/equities/magnit_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Magnit_name_page = requests.get(Magnit_name_data, headers=headers).text
Magnit_name_soup = BeautifulSoup(Magnit_name_page, 'html.parser')
Magnit_name_convert = Magnit_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Magnit_name = Magnit_name_convert[0].text

stocksBasic_name.append(Magnit_name)
stocksBasic_data[Magnit_name] = Magnit_rub
'''==============================================='''
X5Retail_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+x5+retail+group&sxsrf=AOaemvLwRxHyMWNc6mUNNgJxnHp_vUwzxA%3A1633129031397&ei=R5JXYa7QF83HrgTjyJvIAQ&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+x5+retail+group&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEMkDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6DAgjECcQnQIQRhD6AToKCAAQgAQQhwIQFDoECAAQQzoECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQgAQQsQM6CAgAELEDEIMBOgcIABCABBAKOggIABAWEAoQHjoGCAAQFhAeSgQIQRgAUIuwB1jF3Qdgo-cHaARwAngAgAHvAogBygeSAQU5LjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
X5Retail_page = requests.get(X5Retail_data, headers=headers).text
X5Retail_soup = BeautifulSoup(X5Retail_page, 'html.parser')
X5Retail_convert = X5Retail_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
X5Retail_rub = X5Retail_convert[0].text

X5Retail_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+x5+retail+group&sxsrf=AOaemvLwRxHyMWNc6mUNNgJxnHp_vUwzxA%3A1633129031397&ei=R5JXYa7QF83HrgTjyJvIAQ&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+x5+retail+group&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEMkDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6DAgjECcQnQIQRhD6AToKCAAQgAQQhwIQFDoECAAQQzoECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQgAQQsQM6CAgAELEDEIMBOgcIABCABBAKOggIABAWEAoQHjoGCAAQFhAeSgQIQRgAUIuwB1jF3Qdgo-cHaARwAngAgAHvAogBygeSAQU5LjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
X5Retail_name_page = requests.get(X5Retail_name_data, headers=headers).text
X5Retail_name_soup = BeautifulSoup(X5Retail_name_page, 'html.parser')
X5Retail_name_convert = X5Retail_name_soup.findAll('div', {'class': 'oPhL2e'})
X5Retail_name = X5Retail_name_convert[0].text

stocksBasic_name.append(X5Retail_name)
stocksBasic_data[X5Retail_name] = X5Retail_rub
'''==================================================================='''
Detskiy_mir_data = 'https://ru.investing.com/equities/detskiy-mir-pao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Detskiy_mir_page = requests.get(Detskiy_mir_data, headers=headers).text
Detskiy_mir_soup = BeautifulSoup(Detskiy_mir_page, 'html.parser')
Detskiy_mir_convert = Detskiy_mir_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Detskiy_mir_rub = Detskiy_mir_convert[0].text

Detskiy_mir_name_data = 'https://ru.investing.com/equities/detskiy-mir-pao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Detskiy_mir_name_page = requests.get(Detskiy_mir_name_data, headers=headers).text
Detskiy_mir_name_soup = BeautifulSoup(Detskiy_mir_name_page, 'html.parser')
Detskiy_mir_name_convert = Detskiy_mir_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Detskiy_mir_name = Detskiy_mir_name_convert[0].text

stocksBasic_name.append(Detskiy_mir_name)
stocksBasic_data[Detskiy_mir_name] = Detskiy_mir_rub
'''============================================================'''
Lenta_data = 'https://finance.yahoo.com/quote/LNTA.ME?p=LNTA.ME'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Lenta_page = requests.get(Lenta_data, headers=headers).text
Lenta_soup = BeautifulSoup(Lenta_page, 'html.parser')
Lenta_convert = Lenta_soup.findAll('span', {'class': 'Trsdu(0.3s)', 'class': 'Fw(b)', 'class': ' Fz(36px)', 'class': 'Mb(-4px)', 'class': 'D(ib)'})
Lenta_rub = Lenta_convert[1].text

Lenta_name_data = 'https://finance.yahoo.com/quote/LNTA.ME?p=LNTA.ME'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Lenta_name_page = requests.get(Lenta_name_data, headers=headers).text
Lenta_name_soup = BeautifulSoup(Lenta_name_page, 'html.parser')
Lenta_name_convert = Lenta_name_soup.findAll('h1', {'class': 'D(ib)', 'class': 'Fz(18px)'})
Lenta_name = Lenta_name_convert[0].text

stocksBasic_name.append(Lenta_name)
stocksBasic_data[Lenta_name] = Lenta_rub
'''==============================================================================='''
FixPrice_data = 'https://ru.investing.com/equities/fix-price-group-drc?cid=1171256'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
FixPrice_page = requests.get(FixPrice_data, headers=headers).text
FixPrice_soup = BeautifulSoup(FixPrice_page, 'html.parser')
FixPrice_convert = FixPrice_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
FixPrice_rub = FixPrice_convert[0].text

FixPrice_name_data = 'https://ru.investing.com/equities/fix-price-group-drc?cid=1171256'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
FixPrice_name_page = requests.get(FixPrice_name_data, headers=headers).text
FixPrice_name_soup = BeautifulSoup(FixPrice_name_page, 'html.parser')
FixPrice_name_convert = FixPrice_name_soup.findAll('h1', {'class': 'text-2xl', 'class': ' font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
FixPrice_name = FixPrice_name_convert[0].text

stocksBasic_name.append(FixPrice_name)
stocksBasic_data[FixPrice_name] = FixPrice_rub
'''======================================================='''
MVID_data = 'https://ru.investing.com/equities/mvideo_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MVID_page = requests.get(MVID_data, headers=headers).text
MVID_soup = BeautifulSoup(MVID_page, 'html.parser')
MVID_convert = MVID_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
MVID_rub = MVID_convert[0].text

MVID_name_data = 'https://ru.investing.com/equities/mvideo_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MVID_name_page = requests.get(MVID_name_data, headers=headers).text
MVID_name_soup = BeautifulSoup(MVID_name_page, 'html.parser')
MVID_name_convert = MVID_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
MVID_name = MVID_name_convert[0].text

stocksBasic_name.append(MVID_name)
stocksBasic_data[MVID_name] = MVID_rub
'''====================================================================='''
Cherkizovo_data = 'https://ru.investing.com/equities/gruppa-cherkizovo'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Cherkizovo_page = requests.get(Cherkizovo_data, headers=headers).text
Cherkizovo_soup = BeautifulSoup(Cherkizovo_page, 'html.parser')
Cherkizovo_convert = Cherkizovo_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Cherkizovo_rub = Cherkizovo_convert[0].text

Cherkizovo_name_data = 'https://ru.investing.com/equities/gruppa-cherkizovo'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Cherkizovo_name_page = requests.get(Cherkizovo_name_data, headers=headers).text
Cherkizovo_name_soup = BeautifulSoup(Cherkizovo_name_page, 'html.parser')
Cherkizovo_name_convert = Cherkizovo_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Cherkizovo_name = Cherkizovo_name_convert[0].text

stocksBasic_name.append(Cherkizovo_name)
stocksBasic_data[Cherkizovo_name] = Cherkizovo_rub
'''================================================='''

stocksBasic_name.sort()

