import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
USD = 'USD'

# Парсинг данных о котировках акций - лидеров торгов фондового рынка США
'USA лидер торгов №1'
stock_USA_1_data = 'https://ru.investing.com/equities/alibaba'
stock_USA_1_page = requests.get(stock_USA_1_data, headers=HEADERS).text
stock_USA_1_soup = BeautifulSoup(stock_USA_1_page, 'html.parser')
stock_USA_1_convert = stock_USA_1_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_1_dollar = stock_USA_1_convert[0].text + USD
stock_USA_1_name = 'Alibaba ➡'

def show_stock_USA_1_name():
    '''
    :return: Название акции "Alibaba Group"
    '''
    return stock_USA_1_name

def show_alibaba():
    '''
    :return: Акция "Alibaba Group"
    '''
    return stock_USA_1_dollar

'USA лидер торгов №2'
stock_USA_2_data = 'https://ru.investing.com/equities/amazon-com-inc'
stock_USA_2_page = requests.get(stock_USA_2_data, headers=HEADERS).text
stock_USA_2_soup = BeautifulSoup(stock_USA_2_page, 'html.parser')
stock_USA_2_convert = stock_USA_2_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_2_dollar = stock_USA_2_convert[0].text + USD
stock_USA_2_name = 'Amazon.com ➡'

def show_stock_USA_2_name():
    '''
    :return: Название акции "Amazon.com"
    '''
    return stock_USA_2_name

def show_amazon():
    '''
    :return: Акция "Amazon.com"
    '''
    return stock_USA_2_dollar


'USA лидер торгов №3'
stock_USA_3_data = 'https://ru.investing.com/equities/apple-computer-inc'
stock_USA_3_page = requests.get(stock_USA_3_data, headers=HEADERS).text
stock_USA_3_soup = BeautifulSoup(stock_USA_3_page, 'html.parser')
stock_USA_3_convert = stock_USA_3_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_3_dollar = stock_USA_3_convert[0].text + USD
stock_USA_3_name = 'Apple ➡'

def show_stock_USA_3_name():
    '''
    :return: Название акции "Apple"
    '''
    return stock_USA_3_name

def show_apple():
    '''
    :return: Акция "Apple"
    '''
    return stock_USA_3_dollar

'USA лидер торгов №4'
stock_USA_4_data = 'https://ru.investing.com/equities/exxon-mobil'
stock_USA_4_page = requests.get(stock_USA_4_data, headers=HEADERS).text
stock_USA_4_soup = BeautifulSoup(stock_USA_4_page, 'html.parser')
stock_USA_4_convert = stock_USA_4_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_4_dollar = stock_USA_4_convert[0].text + USD
stock_USA_4_name = 'Exxon Mobil ➡'

def show_stock_USA_4_name():
    '''
    :return: Название акции "Exxon Mobil"
    '''
    return stock_USA_4_name

def show_exxonmobil():
    '''
    :return: Акция "Exxon Mobil"
    '''
    return stock_USA_4_dollar


'USA лидер торгов №5'
stock_USA_5_data = 'https://ru.investing.com/equities/netflix,-inc.'
stock_USA_5_page = requests.get(stock_USA_5_data, headers=HEADERS).text
stock_USA_5_soup = BeautifulSoup(stock_USA_5_page, 'html.parser')
stock_USA_5_convert = stock_USA_5_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_5_dollar = stock_USA_5_convert[0].text + USD
stock_USA_5_name = 'Netflix ➡'

def show_stock_USA_5_name():
    '''
    :return: Название Акция "Netflix Inc."
    '''
    return stock_USA_5_name

def show_netflix():
    '''
    :return: Акция "Netflix Inc."
    '''
    return stock_USA_5_dollar

'USA лидер торгов №6'
stock_USA_6_data = 'https://ru.investing.com/equities/facebook-inc'
stock_USA_6_page = requests.get(stock_USA_6_data, headers=HEADERS).text
stock_USA_6_soup = BeautifulSoup(stock_USA_6_page, 'html.parser')
stock_USA_6_convert = stock_USA_6_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_6_dollar = stock_USA_6_convert[0].text + USD
stock_USA_6_name = 'Meta Platforms ➡'

def show_stock_USA_6_name():
    '''
    :return: Название Акция "Meta Platforms"
    '''
    return stock_USA_6_name

def show_metaplatforms():
    '''
    :return: Акция "Meta Platforms"
    '''
    return stock_USA_6_dollar

'USA лидер торгов №7'
stock_USA_7_data = 'https://ru.investing.com/equities/nvidia-corp'
stock_USA_7_page = requests.get(stock_USA_7_data, headers=HEADERS).text
stock_USA_7_soup = BeautifulSoup(stock_USA_7_page, 'html.parser')
stock_USA_7_convert = stock_USA_7_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_7_dollar = stock_USA_7_convert[0].text + USD
stock_USA_7_name = 'NVIDIA ➡'

def show_stock_USA_7_name():
    '''
    :return: Название Акция "NVIDIA"
    '''
    return stock_USA_7_name

def show_nvidia():
    '''
    :return: Акция "NVIDIA"
    '''
    return stock_USA_7_dollar

'USA лидер торгов №8'
stock_USA_8_data = 'https://ru.investing.com/equities/general-electric'
stock_USA_8_page = requests.get(stock_USA_8_data, headers=HEADERS).text
stock_USA_8_soup = BeautifulSoup(stock_USA_8_page, 'html.parser')
stock_USA_8_convert = stock_USA_8_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_8_dollar = stock_USA_8_convert[0].text + USD
stock_USA_8_name = 'General Electric ➡'

def show_stock_USA_8_name():
    '''
    :return: Название Акция "General Electric"
    '''
    return stock_USA_8_name

def show_ge():
    '''
    :return: Акция "General Electric"
    '''
    return stock_USA_8_dollar

'USA лидер торгов №9'
stock_USA_9_data = 'https://ru.investing.com/equities/google-inc'
stock_USA_9_page = requests.get(stock_USA_9_data, headers=HEADERS).text
stock_USA_9_soup = BeautifulSoup(stock_USA_9_page, 'html.parser')
stock_USA_9_convert = stock_USA_9_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_9_dollar = stock_USA_9_convert[0].text + USD
stock_USA_9_name = 'Alpabet A(Google) ➡️'

def show_stock_USA_9_name():
    '''
    :return: Название Акция "Google"
    '''
    return stock_USA_9_name

def show_google():
    '''
    :return: Акция "Google"
    '''
    return stock_USA_9_dollar

'USA лидер торгов №10'
stock_USA_10_data = 'https://ru.investing.com/equities/jp-morgan-chase'
stock_USA_10_page = requests.get(stock_USA_10_data, headers=HEADERS).text
stock_USA_10_soup = BeautifulSoup(stock_USA_10_page, 'html.parser')
stock_USA_10_convert = stock_USA_10_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_10_dollar = stock_USA_10_convert[0].text + USD
stock_USA_10_name = 'JPMorgan Chase & Co ➡'

def show_stock_USA_10_name():
    '''
    :return: Название Акция "JPMorgan Chase & Co"
    '''
    return stock_USA_10_name

def show_jp():
    '''
    :return: Акция "JPMorgan Chase & Co"
    '''
    return stock_USA_10_dollar

'USA лидер торгов №11'
stock_USA_11_data = 'https://ru.investing.com/equities/microsoft-corp'
stock_USA_11_page = requests.get(stock_USA_11_data, headers=HEADERS).text
stock_USA_11_soup = BeautifulSoup(stock_USA_11_page, 'html.parser')
stock_USA_11_convert = stock_USA_11_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_11_dollar = stock_USA_11_convert[0].text + USD
stock_USA_11_name = 'Microsoft Corporation ➡'

def show_stock_USA_11_name():
    '''
    :return: Название Акция "Microsoft Corporation"
    '''
    return stock_USA_11_name

def show_microsoft():
    '''
    :return: Акция "Microsoft Corporation"
    '''
    return stock_USA_11_dollar

'USA лидер торгов №12'
stock_USA_12_data = 'https://ru.investing.com/equities/tesla-motors'
stock_USA_12_page = requests.get(stock_USA_12_data, headers=HEADERS).text
stock_USA_12_soup = BeautifulSoup(stock_USA_12_page, 'html.parser')
stock_USA_12_convert = stock_USA_12_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_12_dollar = stock_USA_12_convert[0].text + USD
stock_USA_12_name = 'Tesla Inc ➡'

def show_stock_USA_12_name():
    '''
    :return: Название Акция "Tesla Inc."
    '''
    return stock_USA_12_name

def show_tesla():
    '''
    :return: Акция "Tesla Inc."
    '''
    return stock_USA_12_dollar

'USA лидер торгов №13'
stock_USA_13_data = 'https://ru.investing.com/equities/wal-mart-stores'
stock_USA_13_page = requests.get(stock_USA_13_data, headers=HEADERS).text
stock_USA_13_soup = BeautifulSoup(stock_USA_13_page, 'html.parser')
stock_USA_13_convert = stock_USA_13_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_13_dollar = stock_USA_13_convert[0].text + USD
stock_USA_13_name = 'Walmart ➡'

def show_stock_USA_13_name():
    '''
    :return: Название Акция "Walmart"
    '''
    return stock_USA_13_name

def show_walmart():
    '''
    :return: Акция "Walmart"
    '''
    return stock_USA_13_dollar

'USA лидер торгов №14'
stock_USA_14_data = 'https://ru.investing.com/equities/palantir-technologies-inc'
stock_USA_14_page = requests.get(stock_USA_14_data, headers=HEADERS).text
stock_USA_14_soup = BeautifulSoup(stock_USA_14_page, 'html.parser')
stock_USA_14_convert = stock_USA_14_soup.findAll('span', {'class': 'text-2xl'})
stock_USA_14_dollar = stock_USA_14_convert[0].text + USD
stock_USA_14_name = 'Palantir Technologies Inc ➡'

def show_stock_USA_14_name():
    '''
    :return: Название Акция "Palantir Technologies Inc."
    '''
    return stock_USA_14_name

def show_palantir():
    '''
    :return: Акция "Palantir Technologies Inc."
    '''
    return stock_USA_14_dollar