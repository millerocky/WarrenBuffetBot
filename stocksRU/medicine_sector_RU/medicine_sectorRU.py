import requests
from bs4 import BeautifulSoup

# Создаю словарь с данными о котировках компаний-эмитентов
medicine_sector_rub = {}

# Создаю массив с данными о названиях компаний-эмитентов для того чтобы осуществить вывод сортировку по алфавиту
medicine_sector_name = []

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

# Парсинг данных о котировках акций медицинского сектора фондового рынка России
life_data = 'https://ru.investing.com/equities/pharmsynthez'
life_page = requests.get(life_data, headers=HEADERS).text
life_soup = BeautifulSoup(life_page, 'html.parser')
life_convert = life_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
life_rub = life_convert[0].text
life_name = 'Life'
medicine_sector_name.append(life_name)
medicine_sector_rub[life_name] = life_rub


iskj_data = 'https://ru.investing.com/equities/human-stem-cells-institute'
iskj_page = requests.get(iskj_data, headers=HEADERS).text
iskj_soup = BeautifulSoup(iskj_page, 'html.parser')
iskj_convert = iskj_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
iskj_rub = iskj_convert[0].text
iskj_name = 'ISKJ'
medicine_sector_name.append(iskj_name)
medicine_sector_rub[iskj_name] = iskj_rub


mdmg_data = 'https://ru.investing.com/equities/md-medical-drc?cid=1167487'
mdmg_page = requests.get(mdmg_data, headers=HEADERS).text
mdmg_soup = BeautifulSoup(mdmg_page, 'html.parser')
mdmg_convert = mdmg_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mdmg_rub = mdmg_convert[0].text
mdmg_name = 'MDMG'
medicine_sector_name.append(mdmg_name)
medicine_sector_rub[mdmg_name] = mdmg_rub


gemc_data = 'https://ru.investing.com/equities/united-medical-group-drc'
gemc_page = requests.get(gemc_data, headers=HEADERS).text
gemc_soup = BeautifulSoup(gemc_page, 'html.parser')
gemc_convert = gemc_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
gemc_rub = gemc_convert[0].text
gemc_name = 'GEMC'
medicine_sector_name.append(gemc_name)
medicine_sector_rub[gemc_name] = gemc_rub


medicine_sector_name.sort()