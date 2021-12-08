import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
RUB = 'RUB'

# Парсинг данных о котировках акций промышленного сектора фондового рынка России
globaltrans_data = 'https://ru.investing.com/equities/globaltrans-inv?cid=1167212'
globaltrans_page = requests.get(globaltrans_data, headers=HEADERS).text
globaltrans_soup = BeautifulSoup(globaltrans_page, 'html.parser')
globaltrans_convert = globaltrans_soup.findAll('span', {'class': 'text-2xl'})
globaltrans_rub = globaltrans_convert[0].text + RUB
globaltrans_name = 'Globaltrans Investment ➡'

def show_globaltrans_name():
    '''
    :return: Название акции Globaltrans
    '''
    return globaltrans_name

def show_globaltrans():
    '''
    :return: Акция "Глобалтранс"
    '''
    return globaltrans_rub

petropavlovsk_data = 'https://ru.investing.com/equities/petropavlovsk?cid=1163242'
petropavlovsk_page = requests.get(petropavlovsk_data, headers=HEADERS).text
petropavlovsk_soup = BeautifulSoup(petropavlovsk_page, 'html.parser')
petropavlovsk_convert = petropavlovsk_soup.findAll('span', {'class': 'text-2xl'})
petropavlovsk_rub = petropavlovsk_convert[0].text + RUB
petropavlovsk_name = 'Petropavlovsk ➡'

def show_petropavlovsk_name():
    '''
    :return: Название акции Petropavlovsk
    '''
    return petropavlovsk_name

def show_petropavlovsk():
    '''
    :return: Акция "Петропавловск"
    '''
    return petropavlovsk_rub

polymetal_data = 'https://ru.investing.com/equities/polymetal?cid=44465'
polymetal_page = requests.get(polymetal_data, headers=HEADERS).text
polymetal_soup = BeautifulSoup(polymetal_page, 'html.parser')
polymetal_convert = polymetal_soup.findAll('span', {'class': 'text-2xl'})
polymetal_rub = polymetal_convert[0].text + RUB
polymetal_name = 'Polymetal ➡'

def show_polymetal_name():
    '''
    :return: Название акции Polymetal
    '''
    return polymetal_name

def show_polymetal():
    '''
    :return: Акция "Polymetal"
    '''
    return polymetal_rub

alrosa_data = 'https://ru.investing.com/equities/alrosa-ao'
alrosa_page = requests.get(alrosa_data, headers=HEADERS).text
alrosa_soup = BeautifulSoup(alrosa_page, 'html.parser')
alrosa_convert = alrosa_soup.findAll('span', {'class': 'text-2xl'})
alrosa_rub = alrosa_convert[0].text + RUB
alrosa_name = 'АК АЛРОСА ➡'

def show_alrosa_name():
    '''
    :return: Название акции Алроса
    '''
    return alrosa_name

def show_alrosa():
    '''
    :return: Акция "АК Алроса"
    '''
    return alrosa_rub

aeroflot_data = 'https://ru.investing.com/equities/aeroflot'
aeroflot_page = requests.get(aeroflot_data, headers=HEADERS).text
aeroflot_soup = BeautifulSoup(aeroflot_page, 'html.parser')
aeroflot_convert = aeroflot_soup.findAll('span', {'class': 'text-2xl'})
aeroflot_rub = aeroflot_convert[0].text + RUB
aeroflot_name = 'АЭРОФЛОТ ➡'

def show_aeroflot_name():
    '''
    :return: Название акции Аэрофлот
    '''
    return aeroflot_name

def show_aeroflot():
    '''
    :return: Акция "Аэрофлот"
    '''
    return aeroflot_rub

gazprom_data = 'https://ru.investing.com/equities/gazprom_rts'
gazprom_page = requests.get(gazprom_data, headers=HEADERS).text
gazprom_soup = BeautifulSoup(gazprom_page, 'html.parser')
gazprom_convert = gazprom_soup.findAll('span', {'class': 'text-2xl'})
gazprom_rub = gazprom_convert[0].text + RUB
gazprom_name = 'ГАЗПРОМ ➡'

def show_gazprom_name():
    '''
    :return: Название акции Газпром
    '''
    return gazprom_name

def show_gazprom():
    '''
    :return: Акция "Газпром"
    '''
    return gazprom_rub

inter_rao_data = 'https://ru.investing.com/equities/inter-rao-ees_mm'
inter_rao_page = requests.get(inter_rao_data, headers=HEADERS).text
inter_rao_soup = BeautifulSoup(inter_rao_page, 'html.parser')
inter_rao_convert = inter_rao_soup.findAll('span', {'class': 'text-2xl'})
inter_rao_rub = inter_rao_convert[0].text + RUB
inter_rao_name = 'ИнтерРАО ➡'

def show_inter_rao_name():
    '''
    :return: Название акции ИнтерРао
    '''
    return inter_rao_name

def show_inter_rao():
    '''
    :return: Акция "ИнтерРАО"
    '''
    return inter_rao_rub

lukoil_data = 'https://ru.investing.com/equities/lukoil_rts'
lukoil_page = requests.get(lukoil_data, headers=HEADERS).text
lukoil_soup = BeautifulSoup(lukoil_page, 'html.parser')
lukoil_convert = lukoil_soup.findAll('span', {'class': 'text-2xl'})
lukoil_rub = lukoil_convert[0].text + RUB
lukoil_name = 'ЛУКОЙЛ ➡'

def show_lukoil_name():
    '''
    :return: Название акции Лукойл
    '''
    return lukoil_name

def show_lukoil():
    '''
    :return: Акция "Лукойл"
    '''
    return lukoil_rub

mmk_data = 'https://ru.investing.com/equities/mmk_rts'
mmk_page = requests.get(mmk_data, headers=HEADERS).text
mmk_soup = BeautifulSoup(mmk_page, 'html.parser')
mmk_convert = mmk_soup.findAll('span', {'class': 'text-2xl'})
mmk_rub = mmk_convert[0].text + RUB
mmk_name = 'ММК ➡'

def show_mmk_name():
    '''
    :return: Название акции ММК
    '''
    return mmk_name

def show_mmk():
    '''
    :return: Акция "ММК"
    '''
    return mmk_rub

nlmk_data = 'https://ru.investing.com/equities/nlmk_rts'
nlmk_page = requests.get(nlmk_data, headers=HEADERS).text
nlmk_soup = BeautifulSoup(nlmk_page, 'html.parser')
nlmk_convert = nlmk_soup.findAll('span', {'class': 'text-2xl'})
nlmk_rub = nlmk_convert[0].text + RUB
nlmk_name = 'НЛМК ➡'

def show_nlmk_name():
    '''
    :return: Название акции НЛМК
    '''
    return nlmk_name

def show_nlmk():
    '''
    :return: Акция "НЛМК"
    '''
    return nlmk_rub

novatek_data = 'https://ru.investing.com/equities/novatek_rts'
novatek_page = requests.get(novatek_data, headers=HEADERS).text
novatek_soup = BeautifulSoup(novatek_page, 'html.parser')
novatek_convert = novatek_soup.findAll('span', {'class': 'text-2xl'})
novatek_rub = novatek_convert[0].text + RUB
novatek_name = 'НОВАТЕК ➡'

def show_novatek_name():
    '''
    :return: Название акции НОВАТЕК
    '''
    return novatek_name

def show_novatek():
    '''
    :return: Акция "НОВАТЕК"
    '''
    return novatek_rub

nornikel_data = 'https://ru.investing.com/equities/gmk-noril-nickel_rts'
nornikel_page = requests.get(nornikel_data, headers=HEADERS).text
nornikel_soup = BeautifulSoup(nornikel_page, 'html.parser')
nornikel_convert = nornikel_soup.findAll('span', {'class': 'text-2xl'})
nornikel_rub = nornikel_convert[0].text + RUB
nornikel_name = 'НОРНИКЕЛЬ ➡'

def show_nornikel_name():
    '''
    :return: Название акции НОРНИКЕЛЬ
    '''
    return nornikel_name

def show_nornikel():
    '''
    :return: Акция "НОРНИКЕЛЬ"
    '''
    return nornikel_rub

polyus_data = 'https://ru.investing.com/equities/polyus-zoloto_rts'
polyus_page = requests.get(polyus_data, headers=HEADERS).text
polyus_soup = BeautifulSoup(polyus_page, 'html.parser')
polyus_convert = polyus_soup.findAll('span', {'class': 'text-2xl'})
polyus_rub = polyus_convert[0].text + RUB
polyus_name = 'Polyus ➡'

def show_polyus_name():
    '''
    :return: Название акции Polyus
    '''
    return polyus_name

def show_polyus():
    '''
    :return: Акция "Polyus"
    '''
    return polyus_rub

rosneft_data = 'https://ru.investing.com/equities/rosneft_rts'
rosneft_page = requests.get(rosneft_data, headers=HEADERS).text
rosneft_soup = BeautifulSoup(rosneft_page, 'html.parser')
rosneft_convert = rosneft_soup.findAll('span', {'class': 'text-2xl'})
rosneft_rub = rosneft_convert[0].text + RUB
rosneft_name = 'Роснефть ➡'

def show_rosneft_name():
    '''
    :return: Название акции Роснефть
    '''
    return rosneft_name

def show_rosneft():
    '''
    :return: Акция "Роснефть"
    '''
    return rosneft_rub

rusal_data = 'https://ru.investing.com/equities/united-company-rusal-plc%60'
rusal_page = requests.get(rusal_data, headers=HEADERS).text
rusal_soup = BeautifulSoup(rusal_page, 'html.parser')
rusal_convert = rusal_soup.findAll('span', {'class': 'text-2xl'})
rusal_rub = rusal_convert[0].text + RUB
rusal_name = 'РУСАЛ ➡'

def show_rusal_name():
    '''
    :return: Название акции РУСАЛ
    '''
    return rusal_name

def show_rusal():
    '''
    :return: Акция "РУСАЛ"
    '''
    return rusal_rub

rushydro_data = 'https://ru.investing.com/equities/gidroogk-011d'
rushydro_page = requests.get(rushydro_data, headers=HEADERS).text
rushydro_soup = BeautifulSoup(rushydro_page, 'html.parser')
rushydro_convert = rushydro_soup.findAll('span', {'class': 'text-2xl'})
rushydro_rub = rushydro_convert[0].text + RUB
rushydro_name = 'РусГидро ➡'

def show_rushydro_name():
    '''
    :return: Название акции РусГидро
    '''
    return rushydro_name

def show_rushydro():
    '''
    :return: Акция "РусГидро"
    '''
    return rushydro_rub

severstal_data = 'https://ru.investing.com/equities/severstal_rts'
severstal_page = requests.get(severstal_data, headers=HEADERS).text
severstal_soup = BeautifulSoup(severstal_page, 'html.parser')
severstal_convert = severstal_soup.findAll('span', {'class': 'text-2xl'})
severstal_rub = severstal_convert[0].text + RUB
severstal_name = 'Северсталь ➡'

def show_severstal_name():
    '''
    :return: Название акции Северсталь
    '''
    return severstal_name

def show_severstal():
    '''
    :return: Акция "Северсталь"
    '''
    return severstal_rub

surgutneft_data = 'https://ru.investing.com/equities/surgutneftegas_rts'
surgutneft_page = requests.get(surgutneft_data, headers=HEADERS).text
surgutneft_soup = BeautifulSoup(surgutneft_page, 'html.parser')
surgutneft_convert = surgutneft_soup.findAll('span', {'class': 'text-2xl'})
surgutneft_rub = surgutneft_convert[0].text + RUB
surgutneft_name = 'Сургутнефтегаз ➡'

def show_surgutneft_name():
    '''
    :return: Название акции Сургутнефтегаз
    '''
    return surgutneft_name

def show_surgutneft():
    '''
    :return: Акция "Сургутнефтегаз"
    '''
    return surgutneft_rub

tatneft_data = 'https://ru.investing.com/equities/tatneft_rts'
tatneft_page = requests.get(tatneft_data, headers=HEADERS).text
tatneft_soup = BeautifulSoup(tatneft_page, 'html.parser')
tatneft_convert = tatneft_soup.findAll('span', {'class': 'text-2xl'})
tatneft_rub = tatneft_convert[0].text + RUB
tatneft_name = 'Татнефть ➡'

def show_tatneft_name():
    '''
    :return: Название акции Татнефть
    '''
    return tatneft_name

def show_tatneft():
    '''
    :return: Акция "Татнефть"
    '''
    return tatneft_rub

transneft_data = 'https://ru.investing.com/equities/transneft-p_rts'
transneft_page = requests.get(transneft_data, headers=HEADERS).text
transneft_soup = BeautifulSoup(transneft_page, 'html.parser')
transneft_convert = transneft_soup.findAll('span', {'class': 'text-2xl'})
transneft_rub = transneft_convert[0].text + RUB
transneft_name = 'Трансненфть ➡'

def show_transneft_name():
    '''
    :return: Название акции Транснефть
    '''
    return transneft_name

def show_transneft():
    '''
    :return: Акция "Транснефть"
    '''
    return transneft_rub

phosagro_data = 'https://ru.investing.com/equities/phosagro'
phosagro_page = requests.get(phosagro_data, headers=HEADERS).text
phosagro_soup = BeautifulSoup(phosagro_page, 'html.parser')
phosagro_convert = phosagro_soup.findAll('span', {'class': 'text-2xl'})
phosagro_rub = phosagro_convert[0].text + RUB
phosagro_name = 'ФосАгро ➡'

def show_phosagro_name():
    '''
    :return: Название акции ФосАгро
    '''
    return phosagro_name

def show_phosagro():
    '''
    :return: Акция "ФосАгро"
    '''
    return phosagro_rub

fsk_data = 'https://ru.investing.com/equities/fsk-ees_rts'
fsk_page = requests.get(fsk_data, headers=HEADERS).text
fsk_soup = BeautifulSoup(fsk_page, 'html.parser')
fsk_convert = fsk_soup.findAll('span', {'class': 'text-2xl'})
fsk_rub = fsk_convert[0].text + RUB
fsk_name = 'ФСК ➡'

def show_fsk_name():
    '''
    :return: Название акции ФСК
    '''
    return fsk_name

def show_fsk():
    '''
    :return: Акция "ФСК"
    '''
    return fsk_rub