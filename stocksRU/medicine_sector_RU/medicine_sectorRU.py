import requests
from bs4 import BeautifulSoup

# Парсинг данных о котировках акций медицинского сектора фондового рынка России

medicine_sector_rub = {}
medicine_sector_name = []
'======================================================================================================================'
life_data = 'https://ru.investing.com/equities/pharmsynthez'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
life_page = requests.get(life_data, headers=headers).text
life_soup = BeautifulSoup(life_page, 'html.parser')
life_convert = life_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
life_rub = life_convert[0].text

life_name_data = 'https://ru.investing.com/equities/pharmsynthez'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
life_name_page = requests.get(life_name_data, headers=headers).text
life_name_soup = BeautifulSoup(life_name_page, 'html.parser')
life_name_convert = life_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
life_name = life_name_convert[0].text

medicine_sector_name.append(life_name)
medicine_sector_rub[life_name] = life_rub
'====================================================================================='
iskj_data = 'https://ru.investing.com/equities/human-stem-cells-institute'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
iskj_page = requests.get(iskj_data, headers=headers).text
iskj_soup = BeautifulSoup(iskj_page, 'html.parser')
iskj_convert = iskj_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
iskj_rub = iskj_convert[0].text

iskj_name_data = 'https://ru.investing.com/equities/human-stem-cells-institute'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
iskj_name_page = requests.get(iskj_name_data, headers=headers).text
iskj_name_soup = BeautifulSoup(iskj_name_page, 'html.parser')
iskj_name_convert = iskj_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
iskj_name = iskj_name_convert[0].text

medicine_sector_name.append(iskj_name)
medicine_sector_rub[iskj_name] = iskj_rub
'======================================================================================================================================='
mdmg_data = 'https://ru.investing.com/equities/md-medical-drc?cid=1167487'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
mdmg_page = requests.get(mdmg_data, headers=headers).text
mdmg_soup = BeautifulSoup(mdmg_page, 'html.parser')
mdmg_convert = mdmg_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mdmg_rub = mdmg_convert[0].text

mdmg_name_data = 'https://ru.investing.com/equities/md-medical-drc?cid=1167487'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
mdmg_name_page = requests.get(mdmg_name_data, headers=headers).text
mdmg_name_soup = BeautifulSoup(mdmg_name_page, 'html.parser')
mdmg_name_convert = mdmg_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
mdmg_name = mdmg_name_convert[0].text

medicine_sector_name.append(mdmg_name)
medicine_sector_rub[mdmg_name] = mdmg_rub
'==========================================================================================================================='
gemc_data = 'https://ru.investing.com/equities/united-medical-group-drc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
gemc_page = requests.get(gemc_data, headers=headers).text
gemc_soup = BeautifulSoup(gemc_page, 'html.parser')
gemc_convert = gemc_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
gemc_rub = gemc_convert[0].text

gemc_name_data = 'https://ru.investing.com/equities/united-medical-group-drc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
gemc_name_page = requests.get(gemc_name_data, headers=headers).text
gemc_name_soup = BeautifulSoup(gemc_name_page, 'html.parser')
gemc_name_convert = gemc_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
gemc_name = gemc_name_convert[0].text

medicine_sector_name.append(gemc_name)
medicine_sector_rub[gemc_name] = gemc_rub

medicine_sector_name.sort()