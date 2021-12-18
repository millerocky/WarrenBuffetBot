import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
USD = 'USD'

# Парсинг данных о котировках акций - лидеров торгов фондового рынка Китая
'China лидер торгов №1'
li_auto_data = 'https://ru.investing.com/equities/li-auto-inc'
li_auto_page = requests.get(li_auto_data, headers=HEADERS).text
li_auto_soup = BeautifulSoup(li_auto_page, 'html.parser')
li_auto_convert = li_auto_soup.findAll('span', {'class': 'text-2xl'})
li_auto_usd = li_auto_convert[0].text + USD
li_auto_name = 'Li Auto ➡'

def show_li_name():
    '''
    :return: Название акции "Li Auto"
    '''
    return li_auto_name

def show_li():
    '''
    :return: Акция "Li Auto"
    '''
    return li_auto_usd

'China лидер торгов №2'
baidu_data = 'https://ru.investing.com/equities/baidu.com'
baidu_page = requests.get(baidu_data, headers=HEADERS).text
baidu_soup = BeautifulSoup(baidu_page, 'html.parser')
baidu_convert = baidu_soup.findAll('span', {'class': 'text-2xl'})
baidu_usd = baidu_convert[0].text + USD
baidu_name = 'Baidu ➡'

def show_baidu_name():
    '''
    :return: Название  Акция "Baidu"
    '''
    return baidu_name

def show_baidu():
    '''
    :return: Акция "Baidu"
    '''
    return baidu_usd

'China лидер торгов №3'
JD_data = 'https://ru.investing.com/equities/jd.com-inc-adr'
JD_page = requests.get(JD_data, headers=HEADERS).text
JD_soup = BeautifulSoup(JD_page, 'html.parser')
JD_convert = JD_soup.findAll('span', {'class': 'text-2xl'})
JD_usd = JD_convert[0].text + USD
JD_name = 'JD ➡'

def show_JD_name():
    '''
    :return: Название акции "JD.com"
    '''
    return JD_name

def show_jd():
    '''
    :return: Акция "JD.com"
    '''
    return JD_usd

'China лидер торгов №4'
bilibili_data = 'https://ru.investing.com/equities/bilibili-inc'
bilibili_page = requests.get(bilibili_data, headers=HEADERS).text
bilibili_soup = BeautifulSoup(bilibili_page, 'html.parser')
bilibili_convert = bilibili_soup.findAll('span', {'class': 'text-2xl'})
bilibili_usd = bilibili_convert[0].text + USD
bilibili_name = 'Bilibili Inc. ➡'

def show_bilibili_name():
    '''
    :return: Название Акция "Bilibili"
    '''
    return bilibili_name

def show_bilibili():
    '''
    :return: Акция "Bilibili"
    '''
    return bilibili_usd

'China лидер торгов №5'
tencent_data = 'https://ru.investing.com/equities/tencent-holdings-pk'
tencent_page = requests.get(tencent_data, headers=HEADERS).text
tencent_soup = BeautifulSoup(tencent_page, 'html.parser')
tencent_convert = tencent_soup.findAll('span', {'class': 'text-2xl'})
tencent_usd = tencent_convert[0].text + USD
tencent_name = 'Tencent Holdings ➡'

def show_tencent_name():
    '''
    :return: Название Акция "Tencent Holdings"
    '''
    return tencent_name

def show_tencent():
    '''
    :return: Акция "Tencent Holdings"
    '''
    return tencent_usd

'China лидер торгов №6'
nio_data = 'https://ru.investing.com/equities/nio-inc'
nio_page = requests.get(nio_data, headers=HEADERS).text
nio_soup = BeautifulSoup(nio_page, 'html.parser')
nio_convert = nio_soup.findAll('span', {'class': 'text-2xl'})
nio_usd = nio_convert[0].text + USD
nio_name = 'Nio Inc. ➡'

def show_nio_name():
    '''
    :return: Название Акция "Nio Inc."
    '''
    return nio_name

def show_nio():
    '''
    :return: Акция "Nio Inc."
    '''
    return nio_usd

'China лидер торгов №7'
xpeng_data = 'https://ru.investing.com/equities/xpeng-inc'
xpeng_page = requests.get(xpeng_data, headers=HEADERS).text
xpeng_soup = BeautifulSoup(xpeng_page, 'html.parser')
xpeng_convert = xpeng_soup.findAll('span', {'class': 'text-2xl'})
xpeng_usd = xpeng_convert[0].text + USD
xpeng_name = 'Xpeng Inc. ➡'

def show_xpeng_name():
    '''
    :return: Название акции "Xpeng Inc."
    '''
    return xpeng_name

def show_xpeng():
    '''
    :return: Акция "Xpeng Inc."
    '''
    return xpeng_usd