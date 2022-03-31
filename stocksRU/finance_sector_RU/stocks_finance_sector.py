import requests
from bs4 import BeautifulSoup
from WarrenBuffetBot.core_class.core_class import Parsing


class stocksFinancialSectorRus(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'

vtb = stocksFinancialSectorRus('https://ru.investing.com/equities/vtb_rts', html_class_parsing={'class': 'text-2xl'},
                               name='ВТБ ➡ ')
tinkoffbank = stocksFinancialSectorRus('https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662', html_class_parsing={'class': 'text-2xl'},
                                       name='TCS Group ➡ ')
mkb = stocksFinancialSectorRus('https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao', html_class_parsing={'class': 'text-2xl'},
                               name='МКБ ➡ ')
sber = stocksFinancialSectorRus('https://ru.investing.com/equities/sberbank_rts', html_class_parsing={'class': 'text-2xl'},
                                name='Сбер Банк ➡ ')
sberprevs = stocksFinancialSectorRus('https://ru.investing.com/equities/sberbank-p_rts', html_class_parsing={'class': 'text-2xl'},
                                     name='Сбер Банк - привилегированные акции ➡ ')
afk = stocksFinancialSectorRus('https://ru.investing.com/equities/afk-sistema_rts', html_class_parsing={'class': 'text-2xl'},
                               name='АФК Система ➡ ')
spbbank = stocksFinancialSectorRus('https://ru.investing.com/equities/bank-st-petersbr_rts', html_class_parsing={'class': 'text-2xl'},
                                   name='Банк Санкт-Петербург ➡ ')