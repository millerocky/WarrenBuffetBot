import requests
from bs4 import BeautifulSoup
from WarrenBuffetBot.core_class.core_class import Parsing


class stocksChina(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'

liauto = stocksChina('https://ru.investing.com/equities/li-auto-inc', html_class_parsing={'class': 'text-2xl'},
                     name='Li Auto ➡ ')
baidu = stocksChina('https://ru.investing.com/equities/baidu.com', html_class_parsing={'class': 'text-2xl'},
                    name='Baidu ➡ ')
jd = stocksChina('https://ru.investing.com/equities/jd.com-inc-adr', html_class_parsing={'class': 'text-2xl'},
                 name='JD ➡ ')
bilibili = stocksChina('https://ru.investing.com/equities/bilibili-inc', html_class_parsing={'class': 'text-2xl'},
                       name='Bilibili Inc. ➡ ')
tencent = stocksChina('https://ru.investing.com/equities/tencent-holdings-pk', html_class_parsing={'class': 'text-2xl'},
                      name='Tencent Holdings ➡ ')
nio = stocksChina('https://ru.investing.com/equities/nio-inc', html_class_parsing={'class': 'text-2xl'},
                  name='Nio Inc. ➡ ')
xpeng = stocksChina('https://ru.investing.com/equities/xpeng-inc', html_class_parsing={'class': 'text-2xl'},
                    name='Xpeng Inc. ➡ ')