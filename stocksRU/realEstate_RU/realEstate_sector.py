import requests
from bs4 import BeautifulSoup
from WarrenBuffetBot.core_class.core_class import Parsing


class stocksRealEstate(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'

pik = stocksRealEstate('https://ru.investing.com/equities/pik_rts', html_class_parsing={'class': 'text-2xl'},
                       name='Группа ПИК ➡ ')
lsr = stocksRealEstate('https://ru.investing.com/equities/lsr-group_rts', html_class_parsing={'class': 'text-2xl'},
                       name='ЛСР ➡ ')