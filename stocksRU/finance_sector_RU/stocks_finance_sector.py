import requests
from bs4 import BeautifulSoup

stocks_finance_rub = {}
stocks_finance_name = []
# Парсинг данных о котировках акций финансового сектора фондового рынка России
vtb_data = 'https://ru.investing.com/equities/vtb_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
vtb_page = requests.get(vtb_data, headers=headers).text
vtb_soup = BeautifulSoup(vtb_page, 'html.parser')
vtb_convert = vtb_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
vtb_rub = vtb_convert[0].text

vtb_name_data = 'https://ru.investing.com/equities/vtb_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
vtb_name_page = requests.get(vtb_name_data, headers=headers).text
vtb_name_soup = BeautifulSoup(vtb_name_page, 'html.parser')
vtb_name_convert = vtb_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
vtb_name = vtb_name_convert[0].text

stocks_finance_name.append(vtb_name)
stocks_finance_rub[vtb_name] = vtb_rub
'''===================================================================================='''
tinkoffBank_data = 'https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tinkoffBank_page = requests.get(tinkoffBank_data, headers=headers).text
tinkoffBank_soup = BeautifulSoup(tinkoffBank_page, 'html.parser')
tinkoffBank_convert = tinkoffBank_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
tinkoffBank_rub = tinkoffBank_convert[0].text

tinkoffBank_name_data = 'https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tinkoffBank_name_page = requests.get(tinkoffBank_name_data, headers=headers).text
tinkoffBank_name_soup = BeautifulSoup(tinkoffBank_name_page, 'html.parser')
tinkoffBank_name_convert = tinkoffBank_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
tinkoffBank_name = tinkoffBank_name_convert[0].text

stocks_finance_name.append(tinkoffBank_name)
stocks_finance_rub[stocks_finance_name] = tinkoffBank_rub
'''========================================================================'''
mkb_data = 'https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
mkb_page = requests.get(mkb_data, headers=headers).text
mkb_soup = BeautifulSoup(mkb_page, 'html.parser')
mkb_convert = mkb_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mkb_rub = mkb_convert[0].text

mkb_name_data = 'https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
mkb_name_page = requests.get(mkb_name_data, headers=headers).text
mkb_name_soup = BeautifulSoup(mkb_name_page, 'html.parser')
mkb_name_convert = mkb_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
mkb_name = mkb_name_convert[0].text

stocks_finance_name.append(mkb_name)
stocks_finance_name[mkb_name] = mkb_rub
'''==================================================================='''
MOEX_data = 'https://ru.investing.com/equities/moskovskaya-birzha-oao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MOEX_page = requests.get(MOEX_data, headers=headers).text
MOEX_soup = BeautifulSoup(MOEX_page, 'html.parser')
MOEX_convert = MOEX_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
MOEX_rub = MOEX_convert[0].text

MOEX_name_data = 'https://ru.investing.com/equities/moskovskaya-birzha-oao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MOEX_name_page = requests.get(MOEX_name_data, headers=headers).text
MOEX_name_soup = BeautifulSoup(MOEX_name_page, 'html.parser')
MOEX_name_convert = MOEX_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
MOEX_name = MOEX_name_convert[0].text

stocks_finance_name.append(MOEX_name)
stocks_finance_rub[MOEX_name] = MOEX_rub
'''=============================================================='''
SBER_data = 'https://ru.investing.com/equities/sberbank_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SBER_page = requests.get(SBER_data, headers=headers).text
SBER_soup = BeautifulSoup(SBER_page, 'html.parser')
SBER_convert = SBER_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
SBER_rub = SBER_convert[0].text

SBER_name_data = 'https://ru.investing.com/equities/sberbank_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SBER_name_page = requests.get(SBER_name_data, headers=headers).text
SBER_name_soup = BeautifulSoup(SBER_name_page, 'html.parser')
SBER_name_convert = SBER_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
SBER_name = SBER_name_convert[0].text

stocks_finance_name.append(SBER_name)
stocks_finance_rub[SBER_name] = SBER_rub
'''================================================================'''
SBERprev_data = 'https://ru.investing.com/equities/sberbank-p_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SBERprev_page = requests.get(SBERprev_data, headers=headers).text
SBERprev_soup = BeautifulSoup(SBERprev_page, 'html.parser')
SBERprev_convert = SBERprev_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
SBERprev_rub = SBERprev_convert[0].text

SBERprev_name_data = 'https://ru.investing.com/equities/sberbank-p_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SBERprev_name_page = requests.get(SBERprev_name_data, headers=headers).text
SBERprev_name_soup = BeautifulSoup(SBERprev_name_page, 'html.parser')
SBERprev_name_convert = SBERprev_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
SBERprev_name = SBERprev_name_convert[0].text

stocks_finance_name.append(SBERprev_name)
stocks_finance_rub[SBERprev_name] = SBERprev_rub
'''============================================================='''
afk_data = 'https://ru.investing.com/equities/afk-sistema_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
afk_page = requests.get(afk_data, headers=headers).text
afk_soup = BeautifulSoup(afk_page, 'html.parser')
afk_convert = afk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
afk_rub = afk_convert[0].text

afk_name_data = 'https://ru.investing.com/equities/afk-sistema_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
afk_name_page = requests.get(afk_name_data, headers=headers).text
afk_name_soup = BeautifulSoup(afk_name_page, 'html.parser')
afk_name_convert = afk_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
afk_name = afk_name_convert[0].text

stocks_finance_name.append(afk_name)
stocks_finance_rub[afk_name] = afk_rub
'''================================================================='''
BSPB_data = 'https://ru.investing.com/equities/bank-st-petersbr_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
BSPB_page = requests.get(BSPB_data, headers=headers).text
BSPB_soup = BeautifulSoup(BSPB_page, 'html.parser')
BSPB_convert = BSPB_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
BSPB_rub = BSPB_convert[0].text

BSPB_name_data = 'https://ru.investing.com/equities/bank-st-petersbr_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
BSPB_name_page = requests.get(BSPB_name_data, headers=headers).text
BSPB_name_soup = BeautifulSoup(BSPB_name_page, 'html.parser')
BSPB_name_convert = BSPB_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
BSPB_name = BSPB_name_convert[0].text

stocks_finance_name.append(BSPB_name)
stocks_finance_name[BSPB_name] = BSPB_rub
'''========================================'''

stocks_finance_name.sort()