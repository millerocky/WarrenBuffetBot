import requests
from bs4 import BeautifulSoup

# Создаю словарь с данными о котировках компаний-эмитентов
stocks_industrial_rub = {}

# Создаю массив с данными о названиях компаний-эмитентов для того чтобы осуществить вывод сортировку по алфавиту
stocks_industrial_name = []

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

# Парсинг данных о котировках акций промышленного сектора фондового рынка России
pik_data = 'https://ru.investing.com/equities/pik_rts'
pik_page = requests.get(pik_data, headers=HEADERS).text
pik_soup = BeautifulSoup(pik_page, 'html.parser')
pik_convert = pik_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
pik_rub = pik_convert[0].text
pik_name = 'Группа ПИК'
stocks_industrial_name.append(pik_name)
stocks_industrial_rub[pik_name] = pik_rub


lsr_data = 'https://ru.investing.com/equities/lsr-group_rts'
lsr_page = requests.request(lsr_data, headers=HEADERS).text
lsr_soup = BeautifulSoup(lsr_page, 'html.parser')
lsr_convert = lsr_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
lsr_rub = lsr_convert[0].text
lsr_name = 'ЛСР'
stocks_industrial_name.append(lsr_name)
stocks_industrial_rub[lsr_name] = lsr_rub


