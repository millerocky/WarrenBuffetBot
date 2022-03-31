import requests
from bs4 import BeautifulSoup
from WarrenBuffetBot.core_class.core_class import Parsing


class stocksItSectorRus(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'


hhru = stocksItSectorRus('https://ru.investing.com/equities/headhunter-group-plc?cid=1166764', html_class_parsing={'class': 'text-2xl'},
                         name='HeadHunter ➡ ')
yandex = stocksItSectorRus('https://ru.investing.com/equities/yandex?cid=102063', html_class_parsing={'class': 'text-2xl'},
                           name='Яндекс ➡ ')
vk = stocksItSectorRus('https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363', html_class_parsing={'class': 'text-2xl'},
                       name='Vk ➡ ')
mts = stocksItSectorRus('https://ru.investing.com/equities/mts_rts', html_class_parsing={'class': 'text-2xl'},
                        name='МТС ➡ ')
ozon = stocksItSectorRus('https://ru.investing.com/equities/ozon-holdings-plc?cid=1167498', html_class_parsing={'class': 'text-2xl'},
                         name='Ozon Holdings ➡ ')
qiwi = stocksItSectorRus('https://ru.investing.com/equities/qiwi-plc?cid=960754', html_class_parsing={'class': 'text-2xl'},
                         name='Qiwi ➡ ')
rosseti = stocksItSectorRus('https://ru.investing.com/equities/rosseti-ao', html_class_parsing={'class': 'text-2xl'},
                            name='Россети ➡ ')
rostelecom = stocksItSectorRus('https://ru.investing.com/equities/rostelecom', html_class_parsing={'class': 'text-2xl'},
                               name='Ростелеком ➡ ')