import requests
from bs4 import BeautifulSoup

# Создаю словарь с данными о котировках компаний-эмитентов
stocks_finance_rub = {}

# Создаю массив с данными о названиях компаний-эмитентов для того чтобы осуществить вывод сортировку по алфавиту
stocks_finance_name = []

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

# Парсинг данных о котировках акций финансового сектора экономики Росиии
vtb_data = 'https://ru.investing.com/equities/vtb_rts'
vtb_page = requests.get(vtb_data, headers=HEADERS).text
vtb_soup = BeautifulSoup(vtb_page, 'html.parser')
vtb_convert = vtb_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
vtb_rub = vtb_convert[0].text
vtb_name = 'ВТБ'
stocks_finance_name.append(vtb_name)
stocks_finance_rub[vtb_name] = vtb_rub


tinkoff_bank_data = 'https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662'
tinkoff_bank_page = requests.get(tinkoff_bank_data, headers=HEADERS).text
tinkoff_bank_soup = BeautifulSoup(tinkoff_bank_page, 'html.parser')
tinkoff_bank_convert = tinkoff_bank_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
tinkoff_bank_rub = tinkoff_bank_convert[0].text
tinkoff_bank_name = 'TCS Group Holding'
stocks_finance_name.append(tinkoff_bank_name)
stocks_finance_rub[tinkoff_bank_name] = tinkoff_bank_rub


mkb_data = 'https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao'
mkb_page = requests.get(mkb_data, headers=HEADERS).text
mkb_soup = BeautifulSoup(mkb_page, 'html.parser')
mkb_convert = mkb_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mkb_rub = mkb_convert[0].text
mkb_name = 'МКБ'
stocks_finance_name.append(mkb_name)
stocks_finance_rub[mkb_name] = mkb_rub


MOEX_data = 'https://ru.investing.com/equities/moskovskaya-birzha-oao'
MOEX_page = requests.get(MOEX_data, headers=HEADERS).text
MOEX_soup = BeautifulSoup(MOEX_page, 'html.parser')
MOEX_convert = MOEX_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
MOEX_rub = MOEX_convert[0].text
MOEX_name = 'Московская биржа'
stocks_finance_name.append(MOEX_name)
stocks_finance_rub[MOEX_name] = MOEX_rub


sber_data = 'https://ru.investing.com/equities/sberbank_rts'
sber_page = requests.get(sber_data, headers=HEADERS).text
sber_soup = BeautifulSoup(sber_page, 'html.parser')
sber_convert = sber_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
sber_rub = sber_convert[0].text
sber_name = 'СБЕР'
stocks_finance_name.append(sber_name)
stocks_finance_rub[sber_name] = sber_rub


sber_prevs_data = 'https://ru.investing.com/equities/sberbank-p_rts'
sber_prevs_page = requests.get(sber_prevs_data, headers=HEADERS).text
sber_prevs_soup = BeautifulSoup(sber_prevs_page, 'html.parser')
sber_prevs_convert = sber_prevs_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
sber_prevs_rub = sber_prevs_convert[0].text
sber_prevs_name = 'СБЕР - привилегированные акции'
stocks_finance_name.append(sber_prevs_name)
stocks_finance_rub[sber_prevs_name] = sber_prevs_rub


afk_data = 'https://ru.investing.com/equities/afk-sistema_rts'
afk_page = requests.get(afk_data, headers=HEADERS).text
afk_soup = BeautifulSoup(afk_page, 'html.parser')
afk_convert = afk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
afk_rub = afk_convert[0].text
afk_name = 'АФК Система'
stocks_finance_name.append(afk_name)
stocks_finance_rub[afk_name] = afk_rub


spb_bank_data = 'https://ru.investing.com/equities/bank-st-petersbr_rts'
spb_bank_page = requests.get(spb_bank_data, headers=HEADERS).text
spb_bank_soup = BeautifulSoup(spb_bank_page, 'html.parser')
spb_bank_convert = spb_bank_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
spb_bank_rub = spb_bank_convert[0].text
spb_bank_name = 'Банк Санкт-Петербург'
stocks_finance_name.append(spb_bank_name)
stocks_finance_rub[spb_bank_name] = spb_bank_rub


stocks_finance_name.sort()