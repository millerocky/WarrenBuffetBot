import requests
from bs4 import BeautifulSoup

# Создаю словарь с данными о котировках компаний-эмитентов
stocks_industrial_rub = {}

# Создаю массив с данными о названиях компаний-эмитентов для того чтобы осуществить вывод сортировку по алфавиту
stocks_industrial_name = []

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

# Парсинг данных о котировках акций промышленного сектора фондового рынка России
globaltrans_data = 'https://ru.investing.com/equities/globaltrans-inv?cid=1167212'
globaltrans_page = requests.get(globaltrans_data, headers=HEADERS).text
globaltrans_soup = BeautifulSoup(globaltrans_page, 'html.parser')
globaltrans_convert = globaltrans_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
globaltrans_rub = globaltrans_convert[0].text
globaltrans_name = 'Globaltrans Investment'
stocks_industrial_name.append(globaltrans_name)
stocks_industrial_rub[globaltrans_name] = globaltrans_rub


petropavlovsk_data = 'https://ru.investing.com/equities/petropavlovsk?cid=1163242'
petropavlovsk_page = requests.get(petropavlovsk_data, headers=HEADERS).text
petropavlovsk_soup = BeautifulSoup(petropavlovsk_page, 'html.parser')
petropavlovsk_convert = petropavlovsk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
petropavlovsk_rub = petropavlovsk_convert[0].text
petropavlovsk_name = 'Petropavlovsk'
stocks_industrial_name.append(petropavlovsk_name)
stocks_industrial_rub[petropavlovsk_name] = petropavlovsk_rub


polymetal_data = 'https://ru.investing.com/equities/polymetal?cid=44465'
polymetal_page = requests.get(polymetal_data, headers=HEADERS).text
polymetal_soup = BeautifulSoup(polymetal_page, 'html.parser')
polymetal_convert = polymetal_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
polymetal_rub = polymetal_convert[0].text
polymetal_name = 'Polymetal'
stocks_industrial_name.append(polymetal_name)
stocks_industrial_rub[polymetal_name] = polymetal_rub


alrosa_data = 'https://ru.investing.com/equities/alrosa-ao'
alrosa_page = requests.get(alrosa_data, headers=HEADERS).text
alrosa_soup = BeautifulSoup(alrosa_page, 'html.parser')
alrosa_convert = alrosa_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
alrosa_rub = alrosa_convert[0].text
alrosa_name = 'АК АЛРОСА'
stocks_industrial_name.append(alrosa_name)
stocks_industrial_rub[alrosa_name] = alrosa_rub


aeroflot_data = 'https://ru.investing.com/equities/aeroflot'
aeroflot_page = requests.get(aeroflot_data, headers=HEADERS).text
aeroflot_soup = BeautifulSoup(aeroflot_page, 'html.parser')
aeroflot_convert = aeroflot_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
aeroflot_rub = aeroflot_convert[0].text
aeroflot_name = 'АЭРОФЛОТ'
stocks_industrial_name.append(aeroflot_name)
stocks_industrial_rub[aeroflot_name] = aeroflot_rub


gazprom_data = 'https://ru.investing.com/equities/gazprom_rts'
gazprom_page = requests.get(gazprom_data, headers=HEADERS).text
gazprom_soup = BeautifulSoup(gazprom_page, 'html.parser')
gazprom_convert = gazprom_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
gazprom_rub = gazprom_convert[0].text
gazprom_name = 'ГАЗПРОМ'
stocks_industrial_name.append(gazprom_name)
stocks_industrial_rub[gazprom_name] = gazprom_rub


inter_rao_data = 'https://ru.investing.com/equities/inter-rao-ees_mm'
inter_rao_page = requests.get(inter_rao_data, headers=HEADERS).text
inter_rao_soup = BeautifulSoup(inter_rao_page, 'html.parser')
inter_rao_convert = inter_rao_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
inter_rao_rub = inter_rao_convert[0].text
inter_rao_name = 'ИнтерРАО'
stocks_industrial_name.append(inter_rao_name)
stocks_industrial_rub[inter_rao_name] = inter_rao_rub


lukoil_data = 'https://ru.investing.com/equities/lukoil_rts'
lukoil_page = requests.get(lukoil_data, headers=HEADERS).text
lukoil_soup = BeautifulSoup(lukoil_page, 'html.parser')
lukoil_convert = lukoil_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
lukoil_rub = lukoil_convert[0].text
lukoil_name = 'ЛУКОЙЛ'
stocks_industrial_name.append(lukoil_name)
stocks_industrial_rub[lukoil_name] = lukoil_rub


mmk_data = 'https://ru.investing.com/equities/mmk_rts'
mmk_page = requests.get(mmk_data, headers=HEADERS).text
mmk_soup = BeautifulSoup(mmk_page, 'html.parser')
mmk_convert = mmk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
mmk_rub = mmk_convert[0].text
mmk_name = 'ММК'
stocks_industrial_name.append(mmk_name)
stocks_industrial_rub[mmk_name] = mmk_rub


nlmk_data = 'https://ru.investing.com/equities/nlmk_rts'
nlmk_page = requests.get(nlmk_data, headers=HEADERS).text
nlmk_soup = BeautifulSoup(nlmk_page, 'html.parser')
nlmk_convert = nlmk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
nlmk_rub = nlmk_convert[0].text
nlmk_name = 'НЛМК'
stocks_industrial_name.append(nlmk_name)
stocks_industrial_rub[nlmk_name] = nlmk_rub


novatek_data = 'https://ru.investing.com/equities/novatek_rts'
novatek_page = requests.get(novatek_data, headers=HEADERS).text
novatek_soup = BeautifulSoup(novatek_page, 'html.parser')
novatek_convert = novatek_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
novatek_rub = novatek_convert[0].text
novatek_name = 'НОВАТЕК'
stocks_industrial_name.append(novatek_name)
stocks_industrial_rub[novatek_name] = novatek_rub


nornikel_data = 'https://ru.investing.com/equities/gmk-noril-nickel_rts'
nornikel_page = requests.get(nornikel_data, headers=HEADERS).text
nornikel_soup = BeautifulSoup(nornikel_page, 'html.parser')
nornikel_convert = nornikel_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
nornikel_rub = nornikel_convert[0].text
nornikel_name = 'НОРНИКЕЛЬ'
stocks_industrial_name.append(nornikel_name)
stocks_industrial_rub[nornikel_name] = nornikel_rub


polyus_data = 'https://ru.investing.com/equities/polyus-zoloto_rts'
polyus_page = requests.get(polyus_data, headers=HEADERS).text
polyus_soup = BeautifulSoup(polyus_page, 'html.parser')
polyus_convert = polyus_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
polyus_rub = polyus_convert[0].text
polyus_name = 'Полюс'
stocks_industrial_name.append(polyus_name)
stocks_industrial_rub[polyus_name] = polyus_rub


rosneft_data = 'https://ru.investing.com/equities/rosneft_rts'
rosneft_page = requests.get(rosneft_data, headers=HEADERS).text
rosneft_soup = BeautifulSoup(rosneft_page, 'html.parser')
rosneft_convert = rosneft_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rosneft_rub = rosneft_convert[0].text
rosneft_name = 'Роснефть'
stocks_industrial_name.append(rosneft_name)
stocks_industrial_rub[rosneft_name] = rosneft_rub


rusal_data = 'https://ru.investing.com/equities/united-company-rusal-plc%60'
rusal_page = requests.get(rusal_data, headers=HEADERS).text
rusal_soup = BeautifulSoup(rusal_page, 'html.parser')
rusal_convert = rusal_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rusal_rub = rusal_convert[0].text
rusal_name = 'РУСАЛ'
stocks_industrial_name.append(rusal_name)
stocks_industrial_rub[rusal_name] = rusal_rub


rushydro_data = 'https://ru.investing.com/equities/gidroogk-011d'
rushydro_page = requests.get(rushydro_data, headers=HEADERS).text
rushydro_soup = BeautifulSoup(rushydro_page, 'html.parser')
rushydro_convert = rushydro_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rushydro_rub = rushydro_convert[0].text
rushydro_name = 'РусГидро'
stocks_industrial_name.append(rushydro_name)
stocks_industrial_rub[rushydro_name] = rushydro_rub


severstal_data = 'https://ru.investing.com/equities/severstal_rts'
severstal_page = requests.get(severstal_data, headers=HEADERS).text
severstal_soup = BeautifulSoup(severstal_page, 'html.parser')
severstal_convert = severstal_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
severstal_rub = severstal_convert[0].text
severstal_name = 'Северсталь'
stocks_industrial_name.append(severstal_name)
stocks_industrial_rub[severstal_name] = severstal_rub


surgutneft_data = 'https://ru.investing.com/equities/surgutneftegas_rts'
surgutneft_page = requests.get(surgutneft_data, headers=HEADERS).text
surgutneft_soup = BeautifulSoup(surgutneft_page, 'html.parser')
surgutneft_convert = surgutneft_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
surgutneft_rub = surgutneft_convert[0].text
surgutneft_name = 'Сургутнефтегаз'
stocks_industrial_name.append(surgutneft_name)
stocks_industrial_rub[surgutneft_name] = surgutneft_rub


tatneft_data = 'https://ru.investing.com/equities/tatneft_rts'
tatneft_page = requests.get(tatneft_data, headers=HEADERS).text
tatneft_soup = BeautifulSoup(tatneft_page, 'html.parser')
tatneft_convert = tatneft_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
tatneft_rub = tatneft_convert[0].text
tatneft_name = 'Татнефть'
stocks_industrial_name.append(tatneft_name)
stocks_industrial_rub[tatneft_name] = tatneft_rub


transneft_data = 'https://ru.investing.com/equities/transneft-p_rts'
transneft_page = requests.get(transneft_data, headers=HEADERS).text
transneft_soup = BeautifulSoup(transneft_page, 'html.parser')
transneft_convert = transneft_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
transneft_rub = transneft_convert[0].text
transneft_name = 'Трансненфть'
stocks_industrial_name.append(transneft_name)
stocks_industrial_rub[transneft_name] = transneft_rub


phosagro_data = 'https://ru.investing.com/equities/phosagro'
phosagro_page = requests.get(phosagro_data, headers=HEADERS).text
phosagro_soup = BeautifulSoup(phosagro_page, 'html.parser')
phosagro_convert = phosagro_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
phosagro_rub = phosagro_convert[0].text
phosagro_name = 'ФосАгро'
stocks_industrial_name.append(phosagro_name)
stocks_industrial_rub[phosagro_name] = phosagro_rub


fsk_data = 'https://ru.investing.com/equities/fsk-ees_rts'
fsk_page = requests.get(fsk_data, headers=HEADERS).text
fsk_soup = BeautifulSoup(fsk_page, 'html.parser')
fsk_convert = fsk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
fsk_rub = fsk_convert[0].text
fsk_name = 'ФСК'
stocks_industrial_name.append(fsk_name)
stocks_industrial_rub[fsk_name] = fsk_rub


stocks_industrial_name.sort()

