import requests
from bs4 import BeautifulSoup


# Парсинг данных о котировках акций - лидеров торгов фондового рынка Китая
'China лидер торгов №1'
li_auto_data = 'https://ru.investing.com/equities/li-auto-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
li_auto_page = requests.get(li_auto_data, headers=headers).text
li_auto_soup = BeautifulSoup(li_auto_page, 'html.parser')
li_auto_convert = li_auto_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
li_auto_usd = li_auto_convert[0].text

li_auto_name_data = 'https://ru.investing.com/equities/li-auto-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
li_auto_name_page = requests.get(li_auto_name_data, headers=headers).text
li_auto_name_soup = BeautifulSoup(li_auto_name_page, 'html.parser')
li_auto_name_convert = li_auto_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
li_auto_name = li_auto_name_convert[0].text


'China лидер торгов №2'
baidu_data = 'https://ru.investing.com/equities/baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
baidu_page = requests.get(baidu_data, headers=headers).text
baidu_soup = BeautifulSoup(baidu_page, 'html.parser')
baidu_convert = baidu_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
baidu_usd = baidu_convert[0].text

baidu_name_data = 'https://ru.investing.com/equities/baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
baidu_name_page = requests.get(baidu_name_data, headers=headers).text
baidu_name_soup = BeautifulSoup(baidu_name_page, 'html.parser')
baidu_name_convert = baidu_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv mobile:mb-2'})
baidu_name = baidu_name_convert[0].text


'China лидер торгов №3'
JD_data = 'https://ru.investing.com/equities/jd.com-inc-adr'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
JD_page = requests.get(JD_data, headers=headers).text
JD_soup = BeautifulSoup(JD_page, 'html.parser')
JD_convert = JD_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
JD_usd = JD_convert[0].text

JD_name_data = 'https://ru.investing.com/equities/jd.com-inc-adr'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
JD_name_page = requests.get(JD_name_data, headers=headers).text
JD_name_soup = BeautifulSoup(JD_name_page, 'html.parser')
JD_name_convert = JD_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
JD_name = JD_name_convert[0].text



'China лидер торгов №4'
bilibili_data = 'https://ru.investing.com/equities/bilibili-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
bilibili_page = requests.get(bilibili_data, headers=headers).text
bilibili_soup = BeautifulSoup(bilibili_page, 'html.parser')
bilibili_convert = bilibili_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
bilibili_usd = bilibili_convert[0].text


bilibili_name_data = 'https://ru.investing.com/equities/bilibili-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
bilibili_name_page = requests.get(bilibili_name_data, headers=headers).text
bilibili_name_soup = BeautifulSoup(bilibili_name_page, 'html.parser')
bilibili_name_convert = bilibili_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
bilibili_name = bilibili_name_convert[0].text



'China лидер торгов №5'
tencent_data = 'https://ru.investing.com/equities/tencent-holdings-pk'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tencent_page = requests.get(tencent_data, headers=headers).text
tencent_soup = BeautifulSoup(tencent_page, 'html.parser')
tencent_convert = tencent_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
tencent_usd = tencent_convert[0].text


tencent_name_data = 'https://ru.investing.com/equities/tencent-holdings-pk'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tencent_name_page = requests.get(tencent_name_data, headers=headers).text
tencent_name_soup = BeautifulSoup(tencent_name_page, 'html.parser')
tencent_name_convert = tencent_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
tencent_name = tencent_name_convert[0].text


'China лидер торгов №6'
nio_data = 'https://ru.investing.com/equities/nio-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
nio_page = requests.get(nio_data, headers=headers).text
nio_soup = BeautifulSoup(nio_page, 'html.parser')
nio_convert = nio_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
nio_usd = nio_convert[0].text

nio_name_data = 'https://ru.investing.com/equities/nio-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
nio_name_page = requests.get(nio_name_data, headers=headers).text
nio_name_soup = BeautifulSoup(nio_name_page, 'html.parser')
nio_name_convert = nio_name_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
nio_name = nio_name_convert[0].text


'China лидер торгов №7'
xpeng_data = 'https://ru.investing.com/equities/xpeng-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
xpeng_page = requests.get(xpeng_data, headers=headers).text
xpeng_soup = BeautifulSoup(xpeng_page, 'html.parser')
xpeng_convert = xpeng_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
xpeng_usd = xpeng_convert[0].text


xpeng_name_data = 'https://ru.investing.com/equities/xpeng-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
xpeng_name_page = requests.get(xpeng_name_data, headers=headers).text
xpeng_name_soup = BeautifulSoup(xpeng_name_page, 'html.parser')
xpeng_name_convert = xpeng_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
xpeng_name = xpeng_name_convert[0].text