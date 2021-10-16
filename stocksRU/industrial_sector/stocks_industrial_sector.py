import requests
from bs4 import BeautifulSoup

# Парсинг данных о котировках акций промышленного сектора фондового рынка России
stocks_industrial_rub = {}
stocks_industrial_name = []
'''=============================================================================='''
Globaltrans_data = 'https://ru.investing.com/equities/globaltrans-inv?cid=1167212'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Globaltrans_page = requests.get(Globaltrans_data, headers=headers).text
Globaltrans_soup = BeautifulSoup(Globaltrans_page, 'html.parser')
Globaltrans_convert = Globaltrans_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Globaltrans_rub = Globaltrans_convert[0].text

Globaltrans_name_data = 'https://ru.investing.com/equities/globaltrans-inv?cid=1167212'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Globaltrans_name_page = requests.get(Globaltrans_name_data, headers=headers).text
Globaltrans_name_soup = BeautifulSoup(Globaltrans_name_page, 'html.parser')
Globaltrans_name_convert = Globaltrans_name_soup.findAll('h1', {'class': 'text-2xl ', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Globaltrans_name = Globaltrans_name_convert[0].text

stocks_industrial_name.append(Globaltrans_name)
stocks_industrial_rub[Globaltrans_name] = Globaltrans_rub
'''==============================================================================='''
Petropavlovsk_data = 'https://ru.investing.com/equities/petropavlovsk?cid=1163242'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Petropavlovsk_page = requests.get(Petropavlovsk_data, headers=headers).text
Petropavlovsk_soup = BeautifulSoup(Petropavlovsk_page, 'html.parser')
Petropavlovsk_convert = Petropavlovsk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Petropavlovsk_rub = Petropavlovsk_convert[0].text

Petropavlovsk_name_data = 'https://ru.investing.com/equities/petropavlovsk?cid=1163242'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Petropavlovsk_name_page = requests.get(Petropavlovsk_name_data, headers=headers).text
Petropavlovsk_name_soup = BeautifulSoup(Petropavlovsk_name_page, 'html.parser')
Petropavlovsk_name_convert = Petropavlovsk_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Petropavlovsk_name = Petropavlovsk_name_convert[0].text

stocks_industrial_name.append(Petropavlovsk_name)
stocks_industrial_rub[Petropavlovsk_name] = Petropavlovsk_rub
'''====================================================================='''
Polymetal_data = 'https://ru.investing.com/equities/polymetal?cid=44465'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Polymetal_page = requests.get(Polymetal_data, headers=headers).text
Polymetal_soup = BeautifulSoup(Polymetal_page, 'html.parser')
Polymetal_convert = Polymetal_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Polymetal_rub = Polymetal_convert[0].text

Polymetal_name_data = 'https://ru.investing.com/equities/polymetal?cid=44465'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Polymetal_name_page = requests.get(Polymetal_name_data, headers=headers).text
Polymetal_name_soup = BeautifulSoup(Polymetal_name_page, 'html.parser')
Polymetal_name_convert = Polymetal_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Polymetal_name = Polymetal_name_convert[0].text

stocks_industrial_name.append(Polymetal_name)
stocks_industrial_rub[Polymetal_name] = Polymetal_rub
'''====================================================='''
Alrosa_data = 'https://ru.investing.com/equities/alrosa-ao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Alrosa_page = requests.get(Alrosa_data, headers=headers).text
Alrosa_soup = BeautifulSoup(Alrosa_page, 'html.parser')
Alrosa_convert = Alrosa_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Alrosa_rub = Alrosa_convert[0].text

Alrosa_name_data = 'https://ru.investing.com/equities/alrosa-ao'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Alrosa_name_page = requests.get(Alrosa_name_data, headers=headers).text
Alrosa_name_soup = BeautifulSoup(Alrosa_name_page, 'html.parser')
Alrosa_name_convert = Alrosa_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Alrosa_name = Alrosa_name_convert[0].text

stocks_industrial_name.append(Alrosa_name)
stocks_industrial_rub[Alrosa_name] = Alrosa_rub
'====================================================='
Aeroflot_data = 'https://ru.investing.com/equities/aeroflot'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Aeroflot_page = requests.get(Aeroflot_data, headers=headers).text
Aeroflot_soup = BeautifulSoup(Aeroflot_page, 'html.parser')
Aeroflot_convert = Aeroflot_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Aeroflot_rub = Aeroflot_convert[0].text

Aeroflot_name_data = 'https://ru.investing.com/equities/aeroflot'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Aeroflot_name_page = requests.get(Aeroflot_name_data, headers=headers).text
Aeroflot_name_soup = BeautifulSoup(Aeroflot_name_page, 'html.parser')
Aeroflot_name_convert = Aeroflot_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Aeroflot_name = Aeroflot_name_convert[0].text

stocks_industrial_name.append(Aeroflot_name)
stocks_industrial_rub[Aeroflot_name] = Aeroflot_rub
'========================================================================'
Gazprom_data = 'https://ru.investing.com/equities/gazprom_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Gazprom_page = requests.get(Gazprom_data, headers=headers).text
Gazprom_soup = BeautifulSoup(Gazprom_page, 'html.parser')
Gazprom_convert = Gazprom_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
Gazprom_rub = Gazprom_convert[0].text

Gazprom_name_data = 'https://ru.investing.com/equities/gazprom_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
Gazprom_name_page = requests.get(Gazprom_name_data, headers=headers).text
Gazprom_name_soup = BeautifulSoup(Gazprom_name_page, 'html.parser')
Gazprom_name_convert = Gazprom_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
Gazprom_name = Gazprom_name_convert[0].text

stocks_industrial_name.append(Gazprom_name)
stocks_industrial_rub[Gazprom_name] = Gazprom_rub
'==============================================================================='
interRao_data = 'https://ru.investing.com/equities/inter-rao-ees_mm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
interRao_page = requests.get(interRao_data, headers=headers).text
interRao_soup = BeautifulSoup(interRao_page, 'html.parser')
interRao_convert = interRao_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
interRao_rub = interRao_convert[0].text

interRao_name_data = 'https://ru.investing.com/equities/inter-rao-ees_mm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
interRao_name_page = requests.get(interRao_name_data, headers=headers).text
interRao_name_soup = BeautifulSoup(interRao_name_page, 'html.parser')
interRao_name_convert = interRao_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
interRao_name = interRao_name_convert[0].text

stocks_industrial_name.append(interRao_name)
stocks_industrial_rub[interRao_name] = interRao_rub
'================================================================================================='
lukoil_data = 'https://ru.investing.com/equities/lukoil_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
lukoil_page = requests.get(lukoil_data, headers=headers).text
lukoil_soup = BeautifulSoup(lukoil_page, 'html.parser')
lukoil_convert = lukoil_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
lukoil_rub = lukoil_convert[0].text

lukoil_name_data = 'https://ru.investing.com/equities/lukoil_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
lukoil_name_page = requests.get(lukoil_name_data, headers=headers).text
lukoil_name_soup = BeautifulSoup(lukoil_name_page, 'html.parser')
lukoil_name_convert = lukoil_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
lukoil_name = lukoil_name_convert[0].text

stocks_industrial_name.append(lukoil_name)
stocks_industrial_rub[lukoil_name] = lukoil_rub
'==============================================================================='
MMK_data = 'https://ru.investing.com/equities/mmk_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MMK_page = requests.get(MMK_data, headers=headers).text
MMK_soup = BeautifulSoup(MMK_page, 'html.parser')
MMK_convert = MMK_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
MMK_rub = MMK_convert[0].text

MMK_name_data = 'https://ru.investing.com/equities/mmk_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MMK_name_page = requests.get(MMK_name_data, headers=headers).text
MMK_name_soup = BeautifulSoup(MMK_name_page, 'html.parser')
MMK_name_convert = MMK_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
MMK_name = MMK_name_convert[0].text

stocks_industrial_name.append(MMK_name)
stocks_industrial_rub[MMK_name] = MMK_rub
'=========================================================================================='
nlmk_data = 'https://ru.investing.com/equities/nlmk_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
nlmk_page = requests.get(nlmk_data, headers=headers).text
nlmk_soup = BeautifulSoup(nlmk_page, 'html.parser')
nlmk_convert = nlmk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
nlmk_rub = nlmk_convert[0].text

nlmk_name_data = 'https://ru.investing.com/equities/nlmk_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
nlmk_name_page = requests.get(nlmk_name_data, headers=headers).text
nlmk_name_soup = BeautifulSoup(nlmk_name_page, 'html.parser')
nlmk_name_convert = nlmk_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
nlmk_name = nlmk_name_convert[0].text

stocks_industrial_name.append(nlmk_name)
stocks_industrial_rub[nlmk_name] = nlmk_rub
'=========================================================================================='
novatek_data = 'https://ru.investing.com/equities/novatek_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
novatek_page = requests.get(novatek_data, headers=headers).text
novatek_soup = BeautifulSoup(novatek_page, 'html.parser')
novatek_convert = novatek_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
novatek_rub = novatek_convert[0].text

novatek_name_data = 'https://ru.investing.com/equities/novatek_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
novatek_name_page = requests.get(novatek_name_data, headers=headers).text
novatek_name_soup = BeautifulSoup(novatek_name_page, 'html.parser')
novatek_name_convert = novatek_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
novatek_name = novatek_name_convert[0].text

stocks_industrial_name.append(novatek_name)
stocks_industrial_rub[novatek_name] = novatek_rub
'========================================================================='
nornikel_data = 'https://ru.investing.com/equities/gmk-noril-nickel_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
nornikel_page = requests.get(nornikel_data, headers=headers).text
nornikel_soup = BeautifulSoup(nornikel_page, 'html.parser')
nornikel_convert = nornikel_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
nornikel_rub = nornikel_convert[0].text

nornikel_name_data = 'https://ru.investing.com/equities/gmk-noril-nickel_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
nornikel_name_page = requests.get(nornikel_name_data, headers=headers).text
nornikel_name_soup = BeautifulSoup(nornikel_name_page, 'html.parser')
nornikel_name_convert = nornikel_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
nornikel_name = nornikel_name_convert[0].text

stocks_industrial_name.append(nornikel_name)
stocks_industrial_rub[nornikel_name] = nornikel_rub
'====================================================================================================================='
polyus_data = 'https://ru.investing.com/equities/polyus-zoloto_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
polyus_page = requests.get(polyus_data, headers=headers).text
polyus_soup = BeautifulSoup(polyus_page, 'html.parser')
polyus_convert = polyus_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
polyus_rub = polyus_convert[0].text

polyus_name_data = 'https://ru.investing.com/equities/polyus-zoloto_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
polyus_name_page = requests.get(polyus_name_data, headers=headers).text
polyus_name_soup = BeautifulSoup(polyus_name_page, 'html.parser')
polyus_name_convert = polyus_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
polyus_name = polyus_name_convert[0].text

stocks_industrial_name.append(polyus_name)
stocks_industrial_rub[polyus_name] = polyus_rub
'==============================================================================================='
rosneft_data = 'https://ru.investing.com/equities/rosneft_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rosneft_page = requests.get(rosneft_data, headers=headers).text
rosneft_soup = BeautifulSoup(rosneft_page, 'html.parser')
rosneft_convert = rosneft_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rosneft_rub = rosneft_convert[0].text

rosneft_name_data = 'https://ru.investing.com/equities/rosneft_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rosneft_name_page = requests.get(rosneft_name_data, headers=headers).text
rosneft_name_soup = BeautifulSoup(rosneft_name_page, 'html.parser')
rosneft_name_convert = rosneft_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
rosneft_name = rosneft_name_convert[0].text

stocks_industrial_name.append(rosneft_name)
stocks_industrial_rub[rosneft_name] = rosneft_rub
'======================================================================================================='
rusal_data = 'https://ru.investing.com/equities/united-company-rusal-plc%60'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rusal_page = requests.get(rusal_data, headers=headers).text
rusal_soup = BeautifulSoup(rusal_page, 'html.parser')
rusal_convert = rusal_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rusal_rub = rusal_convert[0].text

rusal_name_data = 'https://ru.investing.com/equities/united-company-rusal-plc%60'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rusal_name_page = requests.get(rusal_name_data, headers=headers).text
rusal_name_soup = BeautifulSoup(rusal_name_page, 'html.parser')
rusal_name_convert = rusal_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
rusal_name = rusal_name_convert[0].text

stocks_industrial_name.append(rusal_name)
stocks_industrial_rub[rusal_name] = rusal_rub
'===================================================================================================='
rushydro_data = 'https://ru.investing.com/equities/gidroogk-011d'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rushydro_page = requests.get(rushydro_data, headers=headers).text
rushydro_soup = BeautifulSoup(rushydro_page, 'html.parser')
rushydro_convert = rushydro_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
rushydro_rub = rushydro_convert[0].text

rushydro_name_data = 'https://ru.investing.com/equities/gidroogk-011d'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
rushydro_name_page = requests.get(rushydro_name_data, headers=headers).text
rushydro_name_soup = BeautifulSoup(rushydro_name_page, 'html.parser')
rushydro_name_convert = rushydro_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
rushydro_name = rushydro_name_convert[0].text

stocks_industrial_name.append(rushydro_name)
stocks_industrial_rub[rushydro_name] = rushydro_rub
'========================================================================================='
severstal_data = 'https://ru.investing.com/equities/severstal_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
severstal_page = requests.get(severstal_data, headers=headers).text
severstal_soup = BeautifulSoup(severstal_page, 'html.parser')
severstal_convert = severstal_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
severstal_rub = severstal_convert[0].text

severstal_name_data = 'https://ru.investing.com/equities/severstal_rts'
severstal_data = 'https://ru.investing.com/equities/severstal_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
severstal_name_page = requests.get(severstal_name_data, headers=headers).text
severstal_name_soup = BeautifulSoup(severstal_name_page, 'html.parser')
severstal_name_convert = severstal_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
severstal_name = severstal_name_convert[0].text

stocks_industrial_name.append(severstal_name)
stocks_industrial_rub[severstal_name] = severstal_rub
'============================================================================================================='
surgutneft_data = 'https://ru.investing.com/equities/surgutneftegas_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
surgutneft_page = requests.get(surgutneft_data, headers=headers).text
surgutneft_soup = BeautifulSoup(surgutneft_page, 'html.parser')
surgutneft_convert = surgutneft_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
surgutneft_rub = surgutneft_convert[0].text

surgutneft_name_data = 'https://ru.investing.com/equities/surgutneftegas_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
surgutneft_name_page = requests.get(surgutneft_name_data, headers=headers).text
surgutneft_name_soup = BeautifulSoup(surgutneft_name_page, 'html.parser')
surgutneft_name_convert = surgutneft_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
surgutneft_name = surgutneft_name_convert[0].text

stocks_industrial_name.append(surgutneft_name)
stocks_industrial_rub[surgutneft_name] = surgutneft_rub
'=============================================================================================================='
tatneft_data = 'https://ru.investing.com/equities/tatneft_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tatneft_page = requests.get(tatneft_data, headers=headers).text
tatneft_soup = BeautifulSoup(tatneft_page, 'html.parser')
tatneft_convert = tatneft_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
tatneft_rub = tatneft_convert[0].text

tatneft_name_data = 'https://ru.investing.com/equities/tatneft_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tatneft_name_page = requests.get(tatneft_name_data, headers=headers).text
tatneft_name_soup = BeautifulSoup(tatneft_name_page, 'html.parser')
tatneft_name_convert = tatneft_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
tatneft_name = tatneft_name_convert[0].text

stocks_industrial_name.append(tatneft_name)
stocks_industrial_rub[tatneft_name] = tatneft_rub
'===================================================================================================='
transneft_data = 'https://ru.investing.com/equities/transneft-p_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
transneft_page = requests.get(transneft_data, headers=headers).text
transneft_soup = BeautifulSoup(transneft_page, 'html.parser')
transneft_convert = transneft_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
transneft_rub = transneft_convert[0].text

transneft_name_data = 'https://ru.investing.com/equities/transneft-p_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
transneft_name_page = requests.get(transneft_name_data, headers=headers).text
transneft_name_soup = BeautifulSoup(transneft_name_page, 'html.parser')
transneft_name_convert = transneft_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
transneft_name = transneft_name_convert[0].text

stocks_industrial_name.append(transneft_name)
stocks_industrial_rub[transneft_name] = transneft_rub
'======================================================================================================='
phosagro_data = 'https://ru.investing.com/equities/phosagro'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
phosagro_page = requests.get(phosagro_data, headers=headers).text
phosagro_soup = BeautifulSoup(phosagro_page, 'html.parser')
phosagro_convert = phosagro_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
phosagro_rub = phosagro_convert[0].text

phosagro_name_data = 'https://ru.investing.com/equities/phosagro'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
phosagro_name_page = requests.get(phosagro_name_data, headers=headers).text
phosagro_name_soup = BeautifulSoup(phosagro_name_page, 'html.parser')
phosagro_name_convert = phosagro_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
phosagro_name = phosagro_name_convert[0].text

stocks_industrial_name.append(phosagro_name)
stocks_industrial_rub[phosagro_name] = phosagro_rub
'=============================================================================================='
fsk_data = 'https://ru.investing.com/equities/fsk-ees_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
fsk_page = requests.get(fsk_data, headers=headers).text
fsk_soup = BeautifulSoup(fsk_page, 'html.parser')
fsk_convert = fsk_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
fsk_rub = fsk_convert[0].text

fsk_name_data = 'https://ru.investing.com/equities/fsk-ees_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
fsk_name_page = requests.get(fsk_name_data, headers=headers).text
fsk_name_soup = BeautifulSoup(fsk_name_page, 'html.parser')
fsk_name_convert = fsk_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
fsk_name = fsk_name_convert[0].text

stocks_industrial_name.append(fsk_name)
stocks_industrial_rub[fsk_name] = fsk_rub
'==========================================================================='