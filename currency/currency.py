import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML

# Основной класс
class Currency:
	# Заголовки для передачи вместе с URL
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

	def __init__(self, link_to_currency):
		# Установка курса валюты при создании объекта
		self.link_to_currency = link_to_currency
		self.current_converted_price = float(self.get_currency_value().replace(",", "."))

	# Метод для получения курса валюты
	def get_currency_value(self):
		# Парсим всю страницу
		full_page = requests.get(self.link_to_currency, headers=self.headers)

		# Разбираем через BeautifulSoup
		soup = BeautifulSoup(full_page.content, 'html.parser')

		# Получаем нужное для нас значение и возвращаем его
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text



# Создание объекта и вызов метода
link_to_usd_rub = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
usd_rub = Currency(link_to_currency=link_to_usd_rub)

link_to_euro_rub = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B5%D0%B2%D1%80%D0%BE+&aqs=chrome.0.69i59l2j69i57j0i433i512j0i131i433i512j0i433i512j0i131i433i512l3j46i512.2140j1j15&sourceid=chrome&ie=UTF-8'
euro_rub = Currency(link_to_currency=link_to_euro_rub)
