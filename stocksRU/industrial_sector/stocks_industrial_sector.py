import requests
from bs4 import BeautifulSoup
from WarrenBuffetBot.core_class.core_class import Parsing


class stocksIndustrialSectorRus(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'

globaltrans = stocksIndustrialSectorRus('https://ru.investing.com/equities/globaltrans-inv?cid=1167212', html_class_parsing={'class': 'text-2xl'},
                                        name='Globaltrans Investment ➡ ')
petropavlovsk = stocksIndustrialSectorRus('https://ru.investing.com/equities/petropavlovsk?cid=1163242', html_class_parsing={'class': 'text-2xl'},
                                          name='Petropavlovsk ➡ ')
polymetal = stocksIndustrialSectorRus('https://ru.investing.com/equities/polymetal?cid=44465', html_class_parsing={'class': 'text-2xl'},
                                      name='Polymetal ➡ ')
alrosa = stocksIndustrialSectorRus('https://ru.investing.com/equities/alrosa-ao', html_class_parsing={'class': 'text-2xl'},
                                   name='АК АЛРОСА ➡ ')
aeroflot = stocksIndustrialSectorRus('https://ru.investing.com/equities/aeroflot', html_class_parsing={'class': 'text-2xl'},
                                     name='АЭРОФЛОТ ➡ ')
gazprom = stocksIndustrialSectorRus('https://ru.investing.com/equities/gazprom_rts', html_class_parsing={'class': 'text-2xl'},
                                    name='ГАЗПРОМ ➡ ')
interrao = stocksIndustrialSectorRus('https://ru.investing.com/equities/inter-rao-ees_mm', html_class_parsing={'class': 'text-2xl'},
                                     name='ИнтерРАО ➡ ')
lukoil = stocksIndustrialSectorRus('https://ru.investing.com/equities/lukoil_rts', html_class_parsing={'class': 'text-2xl'},
                                   name='ЛУКОЙЛ ➡ ')
mmk = stocksIndustrialSectorRus('https://ru.investing.com/equities/mmk_rts', html_class_parsing={'class': 'text-2xl'},
                                name='ММК ➡ ')
nlmk = stocksIndustrialSectorRus('https://ru.investing.com/equities/nlmk_rts', html_class_parsing={'class': 'text-2xl'},
                                 name='НЛМК ➡ ')
novatek = stocksIndustrialSectorRus('https://ru.investing.com/equities/novatek_rts', html_class_parsing={'class': 'text-2xl'},
                                    name='НОВАТЕК ➡ ')
nornikel = stocksIndustrialSectorRus('https://ru.investing.com/equities/gmk-noril-nickel_rts', html_class_parsing={'class': 'text-2xl'},
                                     name='НОРНИКЕЛЬ ➡ ')
polyus = stocksIndustrialSectorRus('https://ru.investing.com/equities/polyus-zoloto_rts', html_class_parsing={'class': 'text-2xl'},
                                   name='Polyus ➡ ')
rosneft = stocksIndustrialSectorRus('https://ru.investing.com/equities/rosneft_rts', html_class_parsing={'class': 'text-2xl'},
                                    name='Роснефть ➡ ')
rusal = stocksIndustrialSectorRus('https://ru.investing.com/equities/united-company-rusal-plc%60', html_class_parsing={'class': 'text-2xl'},
                                  name='РУСАЛ ➡ ')
rushydro = stocksIndustrialSectorRus('https://ru.investing.com/equities/gidroogk-011d', html_class_parsing={'class': 'text-2xl'},
                                     name='РусГидро ➡ ')
severstal = stocksIndustrialSectorRus('https://ru.investing.com/equities/severstal_rts', html_class_parsing={'class': 'text-2xl'},
                                      name='Северсталь ➡ ')
surgutneft = stocksIndustrialSectorRus('https://ru.investing.com/equities/surgutneftegas_rts', html_class_parsing={'class': 'text-2xl'},
                                       name='Сургутнефтегаз ➡ ')
tatneft = stocksIndustrialSectorRus('https://ru.investing.com/equities/tatneft_rts', html_class_parsing={'class': 'text-2xl'},
                                    name='Татнефть ➡ ')
transneft = stocksIndustrialSectorRus('https://ru.investing.com/equities/transneft-p_rts', html_class_parsing={'class': 'text-2xl'},
                                      name='Трансненфть ➡ ')
phosagro = stocksIndustrialSectorRus('https://ru.investing.com/equities/phosagro', html_class_parsing={'class': 'text-2xl'},
                                     name='ФосАгро ➡ ')
fsk = stocksIndustrialSectorRus('https://ru.investing.com/equities/fsk-ees_rts', html_class_parsing={'class': 'text-2xl'},
                                name='ФСК ➡ ')