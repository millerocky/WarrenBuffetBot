import requests
from bs4 import BeautifulSoup
from WarrenBuffetBot.core_class.core_class import Parsing


class valuesWorldIndecies(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'

moex = valuesWorldIndecies('https://ru.investing.com/indices/mcx', html_class_parsing={'class': 'text-2xl'},
                                name='Московская биржа ➡ ')
snp500 = valuesWorldIndecies('https://ru.investing.com/indices/us-spx-500', html_class_parsing={'class': 'text-2xl'},
                             name='S&P 500 ➡ ')
nasdaq = valuesWorldIndecies('https://ru.investing.com/indices/nq-100', html_class_parsing={'class': 'text-2xl'},
                             name='NASDAQ ➡ ')
shangai = valuesWorldIndecies('https://ru.investing.com/indices/shanghai-composite', html_class_parsing={'class': 'text-2xl'},
                              name='Shanghai Composite ➡ ')