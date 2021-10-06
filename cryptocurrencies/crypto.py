import requests
from bs4 import BeautifulSoup



# Парсинг данных о котировках криптовалют
bitcoin_data = 'https://www.google.com/search?q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&oq=%D0%B1%D0%B8%D1%82&aqs=chrome.1.69i57j0i20i131i263i433i512j0i131i433i512l2j0i433i512j0i512j0i433i512j0i131i433i512j0i512j46i131i433i512.2258j0j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
bitcoin_page = requests.get(bitcoin_data, headers=headers).text
bitcoin_soup = BeautifulSoup(bitcoin_page, 'html.parser')
bitcoin_convert = bitcoin_soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
bitcoin_dollar = bitcoin_convert[0].text


ethereum_data = 'https://ru.investing.com/crypto/ethereum/eth-usd'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
ethereum_page = requests.get(ethereum_data, headers=headers).text
ethereum_soup = BeautifulSoup(ethereum_page, 'html.parser')
ethereum_convert = ethereum_soup.findAll('span', {'class': 'arial_26', 'class': 'inlineblock', 'class': 'pid-1058142-last'})
ethereum_dollar = ethereum_convert[0].text


litecoin_data = 'https://www.google.com/search?q=litecoin+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&sxsrf=AOaemvIIcmwppFpuvfa12RPnq-835FNkYw%3A1632608184860&ei=uJ9PYc_xM-qnrgTTtrCQDw&oq=li+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgYIABAHEB4yCggAEAgQBxAKEB4yCAgAEAgQBxAeMggIABAIEAcQHjoHCAAQRxCwAzoHCAAQsAMQQzoQCC4QxwEQowIQyAMQsAMQQzoQCC4QxwEQ0QMQyAMQsAMQQzoHCCMQsQIQJzoECCMQJzoHCAAQsQMQQzoECAAQQzoKCAAQsQMQgwEQQzoJCCMQJxBGEIICOggIABAHEAUQHkoFCDgSATFKBAhBGABQ7f8ZWLWPGmDEnBpoAXACeACAAUyIAZQEkgEBOJgBAKABAcgBC8ABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
litecoin_page = requests.get(litecoin_data, headers=headers).text
litecoin_soup = BeautifulSoup(litecoin_page, 'html.parser')
litecoin_convert = litecoin_soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
litecoin_dollar = litecoin_convert[0].text


cardano_data = 'https://ru.investing.com/crypto/cardano/ada-usd'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
cardano_page = requests.get(cardano_data, headers=headers).text
cardano_soup = BeautifulSoup(cardano_page, 'html.parser')
cardano_convert = cardano_soup.findAll('span', {'class': 'arial_26', 'class': 'inlineblock', 'class': 'pid-1073899-last'})
cardano_dollar = cardano_convert[0].text


xrp_data = 'https://ru.investing.com/crypto/xrp/xrp-usd'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
xrp_page = requests.get(xrp_data, headers=headers).text
xrp_soup = BeautifulSoup(xrp_page, 'html.parser')
xrp_convert = xrp_soup.findAll('span', {'class': 'arial_26', 'class': 'inlineblock', 'class': 'pid-1118146-last'})
xrp_dollar = xrp_convert[0].text

doge_data = 'https://ru.investing.com/crypto/dogecoin/doge-usd'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
doge_page = requests.get(doge_data, headers=headers).text
doge_soup = BeautifulSoup(doge_page, 'html.parser')
doge_convert = doge_soup.findAll('span', {'class': 'arial_26', 'class': 'inlineblock', 'class': 'pid-1158819-last'})
doge_dollar = doge_convert[0].text



bnb_data = 'https://ru.investing.com/crypto/binance-coin'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
bnb_page = requests.get(bnb_data, headers=headers).text
bnb_soup = BeautifulSoup(bnb_page, 'html.parser')
bnb_convert = bnb_soup.findAll('span', {'class': 'pid-1061448-last'})
bnb_usd = bnb_convert[0].text


bnb_name_data = 'https://ru.investing.com/crypto/binance-coin'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
bnb_name_page = requests.get(bnb_name_data, headers=headers).text
bnb_name_soup = BeautifulSoup(bnb_name_page, 'html.parser')
bnb_name_convert = bnb_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
bnb_name = bnb_name_convert[0].text



tether_data = 'https://ru.investing.com/crypto/tether'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tether_page = requests.get(tether_data, headers=headers).text
tether_soup = BeautifulSoup(tether_page, 'html.parser')
tether_convert = tether_soup.findAll('span', {'class': 'pid-1061453-last'})
tether_usd = tether_convert[0].text

tether_name_data = 'https://ru.investing.com/crypto/tether'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tether_name_page = requests.get(tether_name_data, headers=headers).text
tether_name_soup = BeautifulSoup(tether_name_page, 'html.parser')
tether_name_convert = tether_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
tether_name = tether_name_convert[0].text



solana_data = 'https://ru.investing.com/crypto/solana'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
solana_page = requests.get(solana_data, headers=headers).text
solana_soup = BeautifulSoup(solana_page, 'html.parser')
solana_convert = solana_soup.findAll('span', {'class': 'pid-1177183-last'})
solana_usd = solana_convert[0].text


solana_name_data = 'https://ru.investing.com/crypto/solana'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
solana_name_page = requests.get(solana_name_data, headers=headers).text
solana_name_soup = BeautifulSoup(solana_name_page, 'html.parser')
solana_name_convert = solana_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
solana_name = solana_name_convert[0].text



terra_data = 'https://ru.investing.com/crypto/terra-luna'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
terra_page = requests.get(terra_data, headers=headers).text
terra_soup = BeautifulSoup(terra_page, 'html.parser')
terra_convert = terra_soup.findAll('span', {'class': 'pid-1177187-last'})
terra_usd = terra_convert[0].text

terra_name_data = 'https://ru.investing.com/crypto/terra-luna'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
terra_name_page = requests.get(terra_name_data, headers=headers).text
terra_name_soup = BeautifulSoup(terra_name_page, 'html.parser')
terra_name_convert = terra_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
terra_name = terra_name_convert[0].text



uniswap_data = 'https://ru.investing.com/crypto/uniswap'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
uniswap_page = requests.get(uniswap_data, headers=headers).text
uniswap_soup = BeautifulSoup(uniswap_page, 'html.parser')
uniswap_convert = uniswap_soup.findAll('span', {'class': 'pid-1177189-last'})
uniswap_usd = uniswap_convert[0].text


uniswap_name_data = 'https://ru.investing.com/crypto/uniswap'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
uniswap_name_page = requests.get(uniswap_name_data, headers=headers).text
uniswap_name_soup = BeautifulSoup(uniswap_name_page, 'html.parser')
uniswap_name_convert = uniswap_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
uniswap_name = uniswap_name_convert[0].text



polkadot_data = 'https://ru.investing.com/crypto/polkadot-new'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
polkadot_page = requests.get(polkadot_data, headers=headers).text
polkadot_soup = BeautifulSoup(polkadot_page, 'html.parser')
polkadot_convert = polkadot_soup.findAll('span', {'class': 'pid-1177185-last'})
polkadot_usd = polkadot_convert[0].text


polkadot_name_data = 'https://ru.investing.com/crypto/polkadot-new'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
polkadot_name_page = requests.get(polkadot_name_data, headers=headers).text
polkadot_name_soup = BeautifulSoup(polkadot_name_page, 'html.parser')
polkadot_name_convert = polkadot_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
polkadot_name = polkadot_name_convert[0].text



avalanche_data = 'https://ru.investing.com/crypto/avalanche'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
avalanche_page = requests.get(avalanche_data, headers=headers).text
avalanche_soup = BeautifulSoup(avalanche_page, 'html.parser')
avalanche_convert = avalanche_soup.findAll('span', {'class': 'pid-1177190-last'})
avalanche_usd = avalanche_convert[0].text


avalanche_name_data = 'https://ru.investing.com/crypto/avalanche'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
avalanche_name_page = requests.get(avalanche_name_data, headers=headers).text
avalanche_name_soup = BeautifulSoup(avalanche_name_page, 'html.parser')
avalanche_name_convert = avalanche_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
avalanche_name = avalanche_name_convert[0].text


chainlink_data = 'https://ru.investing.com/crypto/chainlink'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
chainlink_page = requests.get(chainlink_data, headers=headers).text
chainlink_soup = BeautifulSoup(chainlink_page, 'html.parser')
chainlink_convert = chainlink_soup.findAll('span', {'class': 'pid-1061794-last'})
chainlink_usd = chainlink_convert[0].text


chainlink_name_data = 'https://ru.investing.com/crypto/chainlink'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
chainlink_name_page = requests.get(chainlink_name_data, headers=headers).text
chainlink_name_soup = BeautifulSoup(chainlink_name_page, 'html.parser')
chainlink_name_convert = chainlink_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
chainlink_name = chainlink_name_convert[0].text



tron_data = 'https://ru.investing.com/crypto/tron'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tron_page = requests.get(tron_data, headers=headers).text
tron_soup = BeautifulSoup(tron_page, 'html.parser')
tron_convert = tron_soup.findAll('span', {'class': 'pid-1061450-last'})
tron_usd = tron_convert[0].text

tron_name_data = 'https://ru.investing.com/crypto/tron'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
tron_name_page = requests.get(tron_name_data, headers=headers).text
tron_name_soup = BeautifulSoup(tron_name_page, 'html.parser')
tron_name_convert = tron_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
tron_name = tron_name_convert[0].text



shiba_data = 'https://ru.investing.com/crypto/shiba-inu'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
shiba_page = requests.get(shiba_data, headers=headers).text
shiba_soup = BeautifulSoup(shiba_page, 'html.parser')
shiba_convert = shiba_soup.findAll('span', {'class': 'pid-1177506-last'})
shiba_usd = shiba_convert[0].text

shiba_name_data = 'https://ru.investing.com/crypto/shiba-inu'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
shiba_name_page = requests.get(shiba_name_data, headers=headers).text
shiba_name_soup = BeautifulSoup(shiba_name_page, 'html.parser')
shiba_name_convert = shiba_name_soup.findAll('h1', {'class': 'float_lang_base_1', 'class': 'relativeAttr'})
shiba_name = shiba_name_convert[0].text