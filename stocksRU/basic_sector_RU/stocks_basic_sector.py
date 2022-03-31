import requests
from bs4 import BeautifulSoup

from WarrenBuffetBot.core_class.core_class import Parsing


class stocksBasicSectorRus(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'


magnit = stocksBasicSectorRus('https://ru.investing.com/equities/magnit_rts', html_class_parsing={'class': 'text-2xl'},
                              name='Магнит ➡ ')
x5retail = stocksBasicSectorRus('https://ru.investing.com/equities/x5-retail-grp?cid=1061926', html_class_parsing={'class': 'text-2xl'},
                                name='X5 Retail Group ➡ ')
detskiymir = stocksBasicSectorRus('https://ru.investing.com/equities/detskiy-mir-pao', html_class_parsing={'class': 'text-2xl'},
                                  name='Детский мир ➡ ')
fixprice = stocksBasicSectorRus('https://ru.investing.com/equities/fix-price-group-drc?cid=1171256', html_class_parsing={'class': 'text-2xl'},
                                name='Fix Price Group ➡ ')
mvideo = stocksBasicSectorRus('https://ru.investing.com/equities/mvideo_rts', html_class_parsing={'class': 'text-2xl'},
                              name='МВидео ➡ ')
cherkizovo = stocksBasicSectorRus('https://ru.investing.com/equities/gruppa-cherkizovo', html_class_parsing={'class': 'text-2xl'},
                                  name='Черкизово ➡ ')