import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

# Получение данных о курсе валют, используя парсинг данных с помощью BeautifulSoup
dollar_data = 'https://ru.investing.com/currencies/usd-rub'
dollar_page = requests.get(dollar_data, headers=HEADERS).text
dollar_soup = BeautifulSoup(dollar_page, 'html.parser')
dollar_convert = dollar_soup.findAll('span', {'class': 'arial_26', 'class': 'inlineblock', 'class': 'pid-2186-last'})
dollar_rub = dollar_convert[0].text

euro_data = 'https://ru.investing.com/currencies/eur-rub'
euro_page = requests.get(euro_data, headers=HEADERS).text
euro_soup = BeautifulSoup(euro_page, 'html.parser')
euro_convert = euro_soup.findAll('span', {'class': 'arial_26', 'class': 'inlineblock', 'class': 'pid-1691-last'})
euro_rub = euro_convert[0].text