import requests
from bs4 import BeautifulSoup


# Создаю класс для получения котировок акций, предварительно наследуя уже созданный корневой класс Parsing
from WarrenBuffetBot.core_class.core_class import Parsing


class stocksUsa(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'

alibaba = stocksUsa('https://ru.investing.com/equities/alibaba', html_class_parsing={'class': 'text-2xl'},
                 name='Alibaba ➡ ')
amazon = stocksUsa('https://ru.investing.com/equities/amazon-com-inc', html_class_parsing={'class': 'text-2xl'},
                name='Amazon ➡ ')
apple = stocksUsa('https://ru.investing.com/equities/apple-computer-inc', html_class_parsing={'class': 'text-2xl'},
               name='Apple ➡')
exxon_mobil = stocksUsa('https://ru.investing.com/equities/exxon-mobil', html_class_parsing={'class': 'text-2xl'},
                     name='Exxon Mobil ➡ ')
netflix = stocksUsa('https://ru.investing.com/equities/netflix,-inc.', html_class_parsing={'class': 'text-2xl'},
                 name='Netflix ➡ ')
meta = stocksUsa('https://ru.investing.com/equities/facebook-inc', html_class_parsing={'class': 'text-2xl'},
              name='Meta Platforms ➡ ')
nvidia = stocksUsa('https://ru.investing.com/equities/nvidia-corp', html_class_parsing={'class': 'text-2xl'},
                name='NVIDIA ➡ ')
gm = stocksUsa('https://ru.investing.com/equities/general-electric', html_class_parsing={'class': 'text-2xl'},
            name='General Electric ➡ ')
alphabet = stocksUsa('https://ru.investing.com/equities/google-inc', html_class_parsing={'class': 'text-2xl'},
                  name='Alpabet A(Google) ➡ ')
jpmorgan = stocksUsa('https://ru.investing.com/equities/jp-morgan-chase', html_class_parsing={'class': 'text-2xl'},
                  name='JPMorgan Chase & Co ➡ ')
microsoft = stocksUsa('https://ru.investing.com/equities/microsoft-corp', html_class_parsing={'class': 'text-2xl'},
                   name='Microsoft ➡ ')
tesla = stocksUsa('https://ru.investing.com/equities/tesla-motors', html_class_parsing={'class': 'text-2xl'},
               name='Tesla ➡ ')
walmart = stocksUsa('https://ru.investing.com/equities/wal-mart-stores', html_class_parsing={'class': 'text-2xl'},
                 name='Walmart ➡ ')
palantir = stocksUsa('https://ru.investing.com/equities/palantir-technologies-inc', html_class_parsing={'class': 'text-2xl'},
                  name='Palantir ➡ ')