import requests
from bs4 import BeautifulSoup

usa_prices = {}
usa_names = []
# Парсинг данных о котировках акций - лидеров торгов фондового рынка США
'================================================================================================================'
'USA лидер торгов №1'
stock_USA_1_data = 'https://ru.investing.com/equities/alibaba'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_1_page = requests.get(stock_USA_1_data, headers=headers).text
stock_USA_1_soup = BeautifulSoup(stock_USA_1_page, 'html.parser')
stock_USA_1_convert = stock_USA_1_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_1_dollar = stock_USA_1_convert[0].text

stock_USA_1_name_data = 'https://ru.investing.com/equities/alibaba'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_1_name_page = requests.get(stock_USA_1_name_data, headers=headers).text
stock_USA_1_name_soup = BeautifulSoup(stock_USA_1_name_page, 'html.parser')
stock_USA_1_name_convert = stock_USA_1_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_1_name = stock_USA_1_name_convert[0].text

usa_names.append(stock_USA_1_name)
usa_prices[stock_USA_1_name] = stock_USA_1_dollar
'=============================================================================================================================='
'USA лидер торгов №2'
stock_USA_2_data = 'https://ru.investing.com/equities/amazon-com-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_2_page = requests.get(stock_USA_2_data, headers=headers).text
stock_USA_2_soup = BeautifulSoup(stock_USA_2_page, 'html.parser')
stock_USA_2_convert = stock_USA_2_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_2_dollar = stock_USA_2_convert[0].text

stock_USA_2_name_data = 'https://ru.investing.com/equities/amazon-com-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_2_name_page = requests.get(stock_USA_2_name_data, headers=headers).text
stock_USA_2_name_soup = BeautifulSoup(stock_USA_2_name_page, 'html.parser')
stock_USA_2_name_convert = stock_USA_2_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_2_name = stock_USA_2_name_convert[0].text

usa_names.append(stock_USA_2_name)
usa_prices[stock_USA_2_name] = stock_USA_2_dollar
'================================================================================================================================'
'USA лидер торгов №3'
stock_USA_3_data = 'https://ru.investing.com/equities/apple-computer-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_3_page = requests.get(stock_USA_3_data, headers=headers).text
stock_USA_3_soup = BeautifulSoup(stock_USA_3_page, 'html.parser')
stock_USA_3_convert = stock_USA_3_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_3_dollar = stock_USA_3_convert[0].text

stock_USA_3_name_data = 'https://ru.investing.com/equities/apple-computer-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_3_name_page = requests.get(stock_USA_3_name_data, headers=headers).text
stock_USA_3_name_soup = BeautifulSoup(stock_USA_3_name_page, 'html.parser')
stock_USA_3_name_convert = stock_USA_3_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_3_name = stock_USA_3_name_convert[0].text

usa_names.append(stock_USA_3_name)
usa_prices[stock_USA_3_name] = stock_USA_3_dollar
'==================================================================================================================================='
'USA лидер торгов №4'
stock_USA_4_data = 'https://ru.investing.com/equities/exxon-mobil'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_4_page = requests.get(stock_USA_4_data, headers=headers).text
stock_USA_4_soup = BeautifulSoup(stock_USA_4_page, 'html.parser')
stock_USA_4_convert = stock_USA_4_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_4_dollar = stock_USA_4_convert[0].text

stock_USA_4_name_data = 'https://ru.investing.com/equities/exxon-mobil'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_4_name_page = requests.get(stock_USA_4_name_data, headers=headers).text
stock_USA_4_name_soup = BeautifulSoup(stock_USA_4_name_page, 'html.parser')
stock_USA_4_name_convert = stock_USA_4_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_4_name = stock_USA_4_name_convert[0].text

usa_names.append(stock_USA_4_name)
usa_prices[stock_USA_4_name] = stock_USA_4_dollar
'==================================================================================================================================='
'USA лидер торгов №5'
stock_USA_5_data = 'https://ru.investing.com/equities/netflix,-inc.'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_5_page = requests.get(stock_USA_5_data, headers=headers).text
stock_USA_5_soup = BeautifulSoup(stock_USA_5_page, 'html.parser')
stock_USA_5_convert = stock_USA_5_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_5_dollar = stock_USA_5_convert[0].text

stock_USA_5_name_data = 'https://ru.investing.com/equities/netflix,-inc.'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_5_name_page = requests.get(stock_USA_5_name_data, headers=headers).text
stock_USA_5_name_soup = BeautifulSoup(stock_USA_5_name_page, 'html.parser')
stock_USA_5_name_convert = stock_USA_5_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_5_name = stock_USA_5_name_convert[0].text

usa_names.append(stock_USA_5_name)
usa_prices[stock_USA_5_name] = stock_USA_5_dollar
'=========================================================================================================================================='
'USA лидер торгов №6'
stock_USA_6_data = 'https://ru.investing.com/equities/facebook-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_6_page = requests.get(stock_USA_6_data, headers=headers).text
stock_USA_6_soup = BeautifulSoup(stock_USA_6_page, 'html.parser')
stock_USA_6_convert = stock_USA_6_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_6_dollar = stock_USA_6_convert[0].text

stock_USA_6_name_data = 'https://ru.investing.com/equities/facebook-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_6_name_page = requests.get(stock_USA_6_name_data, headers=headers).text
stock_USA_6_name_soup = BeautifulSoup(stock_USA_6_name_page, 'html.parser')
stock_USA_6_name_convert = stock_USA_6_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_6_name = stock_USA_6_name_convert[0].text

usa_names.append(stock_USA_6_name)
usa_prices[stock_USA_6_name] = stock_USA_6_dollar
'======================================================================================================================================='
'USA лидер торгов №7'
stock_USA_7_data = 'https://ru.investing.com/equities/nvidia-corp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_7_page = requests.get(stock_USA_7_data, headers=headers).text
stock_USA_7_soup = BeautifulSoup(stock_USA_7_page, 'html.parser')
stock_USA_7_convert = stock_USA_7_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_7_dollar = stock_USA_7_convert[0].text

stock_USA_7_name_data = 'https://ru.investing.com/equities/nvidia-corp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_7_name_page = requests.get(stock_USA_7_name_data, headers=headers).text
stock_USA_7_name_soup = BeautifulSoup(stock_USA_7_name_page, 'html.parser')
stock_USA_7_name_convert = stock_USA_7_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_7_name = stock_USA_7_name_convert[0].text

usa_names.append(stock_USA_7_name)
usa_prices[stock_USA_7_name] = stock_USA_7_dollar
'=========================================================================================================================='
'USA лидер торгов №8'
stock_USA_8_data = 'https://ru.investing.com/equities/general-electric'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_8_page = requests.get(stock_USA_8_data, headers=headers).text
stock_USA_8_soup = BeautifulSoup(stock_USA_8_page, 'html.parser')
stock_USA_8_convert = stock_USA_8_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_8_dollar = stock_USA_8_convert[0].text

stock_USA_8_name_data = 'https://ru.investing.com/equities/general-electric'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_8_name_page = requests.get(stock_USA_8_name_data, headers=headers).text
stock_USA_8_name_soup = BeautifulSoup(stock_USA_8_name_page, 'html.parser')
stock_USA_8_name_convert = stock_USA_8_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_8_name = stock_USA_8_name_convert[0].text

usa_names.append(stock_USA_8_name)
usa_prices[stock_USA_8_name] = stock_USA_8_dollar
'============================================================================================================================='
'USA лидер торгов №9'
stock_USA_9_data = 'https://ru.investing.com/equities/google-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_9_page = requests.get(stock_USA_9_data, headers=headers).text
stock_USA_9_soup = BeautifulSoup(stock_USA_9_page, 'html.parser')
stock_USA_9_convert = stock_USA_9_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_9_dollar = stock_USA_9_convert[0].text

stock_USA_9_name_data = 'https://ru.investing.com/equities/google-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_9_name_page = requests.get(stock_USA_9_name_data, headers=headers).text
stock_USA_9_name_soup = BeautifulSoup(stock_USA_9_name_page, 'html.parser')
stock_USA_9_name_convert = stock_USA_9_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_9_name = stock_USA_9_name_convert[0].text

usa_names.append(stock_USA_9_name)
usa_prices[stock_USA_9_name] = stock_USA_9_dollar
'=================================================================================================================================================='
'USA лидер торгов №10'
stock_USA_10_data = 'https://ru.investing.com/equities/jp-morgan-chase'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_10_page = requests.get(stock_USA_10_data, headers=headers).text
stock_USA_10_soup = BeautifulSoup(stock_USA_10_page, 'html.parser')
stock_USA_10_convert = stock_USA_10_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_10_dollar = stock_USA_10_convert[0].text

stock_USA_10_name_data = 'https://ru.investing.com/equities/jp-morgan-chase'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_10_name_page = requests.get(stock_USA_10_name_data, headers=headers).text
stock_USA_10_name_soup = BeautifulSoup(stock_USA_10_name_page, 'html.parser')
stock_USA_10_name_convert = stock_USA_10_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_10_name = stock_USA_10_name_convert[0].text

usa_names.append(stock_USA_10_name)
usa_prices[stock_USA_10_name] = stock_USA_10_dollar
'==================================================================================================================='
'USA лидер торгов №11'
stock_USA_11_data = 'https://ru.investing.com/equities/microsoft-corp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_11_page = requests.get(stock_USA_11_data, headers=headers).text
stock_USA_11_soup = BeautifulSoup(stock_USA_11_page, 'html.parser')
stock_USA_11_convert = stock_USA_11_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_11_dollar = stock_USA_11_convert[0].text

stock_USA_11_name_data = 'https://ru.investing.com/equities/microsoft-corp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_11_name_page = requests.get(stock_USA_11_name_data, headers=headers).text
stock_USA_11_name_soup = BeautifulSoup(stock_USA_11_name_page, 'html.parser')
stock_USA_11_name_convert = stock_USA_11_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_11_name = stock_USA_11_name_convert[0].text

usa_names.append(stock_USA_11_name)
usa_prices[stock_USA_11_name] = stock_USA_11_dollar
'===================================================================================================================='
'USA лидер торгов №12'
stock_USA_12_data = 'https://ru.investing.com/equities/tesla-motors'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_12_page = requests.get(stock_USA_12_data, headers=headers).text
stock_USA_12_soup = BeautifulSoup(stock_USA_12_page, 'html.parser')
stock_USA_12_convert = stock_USA_12_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_12_dollar = stock_USA_12_convert[0].text

stock_USA_12_name_data = 'https://ru.investing.com/equities/tesla-motors'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_12_name_page = requests.get(stock_USA_12_name_data, headers=headers).text
stock_USA_12_name_soup = BeautifulSoup(stock_USA_12_name_page, 'html.parser')
stock_USA_12_name_convert = stock_USA_12_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_12_name = stock_USA_12_name_convert[0].text

usa_names.append(stock_USA_12_name)
usa_prices[stock_USA_12_name] = stock_USA_12_dollar
'===================================================================================================================================='
'USA лидер торгов №13'
stock_USA_13_data = 'https://ru.investing.com/equities/wal-mart-stores'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_13_page = requests.get(stock_USA_13_data, headers=headers).text
stock_USA_13_soup = BeautifulSoup(stock_USA_13_page, 'html.parser')
stock_USA_13_convert = stock_USA_13_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_13_dollar = stock_USA_13_convert[0].text

stock_USA_13_name_data = 'https://ru.investing.com/equities/wal-mart-stores'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_13_name_page = requests.get(stock_USA_13_name_data, headers=headers).text
stock_USA_13_name_soup = BeautifulSoup(stock_USA_13_name_page, 'html.parser')
stock_USA_13_name_convert = stock_USA_13_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_13_name = stock_USA_13_name_convert[0].text

usa_names.append(stock_USA_13_name)
usa_prices[stock_USA_13_name] = stock_USA_13_dollar
'=============================================================================================================================='
'USA лидер торгов №14'
stock_USA_14_data = 'https://ru.investing.com/equities/palantir-technologies-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_14_page = requests.get(stock_USA_14_data, headers=headers).text
stock_USA_14_soup = BeautifulSoup(stock_USA_14_page, 'html.parser')
stock_USA_14_convert = stock_USA_14_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stock_USA_14_dollar = stock_USA_14_convert[0].text

stock_USA_14_name_data = 'https://ru.investing.com/equities/palantir-technologies-inc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_14_name_page = requests.get(stock_USA_14_name_data, headers=headers).text
stock_USA_14_name_soup = BeautifulSoup(stock_USA_14_name_page, 'html.parser')
stock_USA_14_name_convert = stock_USA_14_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stock_USA_14_name = stock_USA_14_name_convert[0].text

usa_names.append(stock_USA_14_name)
usa_prices[stock_USA_14_name] = stock_USA_14_dollar

usa_names.sort()