import requests
from bs4 import BeautifulSoup

# Создаю словарь с данными о котировках компаний-эмитентов
stocksBasic_data = {}

# Создаю массив с данными о названиях компаний-эмитентов для того чтобы осуществить вывод сортировку по алфавиту
stocksBasic_name = []

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

# Парсинг данных о котировках акций реального сектора экономики Росиии
magnit_data = 'https://ru.investing.com/equities/magnit_rts'
magnit_page = requests.get(magnit_data, headers=HEADERS).text
magnit_soup = BeautifulSoup(magnit_page, 'html.parser')
magnit_convert = magnit_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
magnit_rub = magnit_convert[0].text
magnit_name = 'Магнит'
stocksBasic_name.append(magnit_name)
stocksBasic_data[magnit_name] = magnit_rub


x5group_data = 'https://ru.investing.com/equities/x5-retail-grp?cid=1061926'
x5group_page = requests.get(x5group_data, headers=HEADERS).text
x5group_soup = BeautifulSoup(x5group_page, 'html.parser')
x5group_convert = x5group_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
x5group_rub = x5group_convert[0].text
x5group_name = 'X5 Retail Group'
stocksBasic_name.append(x5group_name)
stocksBasic_data[x5group_name] = x5group_rub


detskiy_mir_data = 'https://ru.investing.com/equities/detskiy-mir-pao'
detskiy_mir_page = requests.get(detskiy_mir_data, headers=HEADERS).text
detskiy_mir_soup = BeautifulSoup(detskiy_mir_page, 'html.parser')
detskiy_mir_convert = detskiy_mir_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
detskiy_mir_rub = detskiy_mir_convert[0].text
detskiy_mir_name = 'Детский мир'
stocksBasic_name.append(detskiy_mir_name)
stocksBasic_data[detskiy_mir_name] = detskiy_mir_rub


lenta_data = 'https://finance.yahoo.com/quote/LNTA.ME?p=LNTA.ME'
lenta_page = requests.get(lenta_data, headers=HEADERS).text
lenta_soup = BeautifulSoup(lenta_page, 'html.parser')
lenta_convert = lenta_soup.findAll('span', {'class': 'Trsdu(0.3s)', 'class': 'Fw(b)', 'class': ' Fz(36px)', 'class': 'Mb(-4px)', 'class': 'D(ib)'})
lenta_rub = lenta_convert[1].text
lenta_name = 'Лента'
stocksBasic_name.append(lenta_name)
stocksBasic_data[lenta_name] = lenta_rub


fix_price_data = 'https://ru.investing.com/equities/fix-price-group-drc?cid=1171256'
fix_price_page = requests.get(fix_price_data, headers=HEADERS).text
fix_price_soup = BeautifulSoup(fix_price_page, 'html.parser')
fix_price_convert = fix_price_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
fix_price_rub = fix_price_convert[0].text
fix_price_name = 'Fix Price Group'
stocksBasic_name.append(fix_price_name)
stocksBasic_data[fix_price_name] = fix_price_rub


mvideo_data = 'https://ru.investing.com/equities/mvideo_rts'
mvideo_page = requests.get(mvideo_data, headers=HEADERS).text
mvideo_soup = BeautifulSoup(mvideo_page, 'html.parser')
mvideo_convert = mvideo_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mvideo_rub = mvideo_convert[0].text
mvideo_name = 'МВидео'
stocksBasic_name.append(mvideo_name)
stocksBasic_data[mvideo_name] = mvideo_rub


cherkizovo_data = 'https://ru.investing.com/equities/gruppa-cherkizovo'
cherkizovo_page = requests.get(cherkizovo_data, headers=HEADERS).text
cherkizovo_soup = BeautifulSoup(cherkizovo_page, 'html.parser')
cherkizovo_convert = cherkizovo_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
cherkizovo_rub = cherkizovo_convert[0].text
cherkizovo_name = 'Черкизово'
stocksBasic_name.append(cherkizovo_name)
stocksBasic_data[cherkizovo_name] = cherkizovo_rub


stocksBasic_name.sort()

