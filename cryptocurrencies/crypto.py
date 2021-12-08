import requests
from bs4 import BeautifulSoup

# Ключ суперюзера моего пк
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
USD = 'USD'

# Парсинг данных о котировках криптовалют
bitcoin_data = 'https://ru.investing.com/crypto/bitcoin'
bitcoin_page = requests.get(bitcoin_data, headers=HEADERS).text
bitcoin_soup = BeautifulSoup(bitcoin_page, 'html.parser')
bitcoin_convert = bitcoin_soup.findAll('span', {'class': 'pid-1057391-last'})
bitcoin_usd = bitcoin_convert[0].text + USD
bitcoin_name = 'Bitcoin ➡'

def show_bitcoin_name():
    '''
    :return: Название Bitcoin
    '''
    return bitcoin_name

def show_bitcoin():
    '''
    :return: Bitcoin
    '''
    return bitcoin_usd

ethereum_data = 'https://ru.investing.com/crypto/ethereum/eth-usd'
ethereum_page = requests.get(ethereum_data, headers=HEADERS).text
ethereum_soup = BeautifulSoup(ethereum_page, 'html.parser')
ethereum_convert = ethereum_soup.findAll('span', {'class': 'text-2xl'})
ethereum_usd = ethereum_convert[0].text + USD
ethereum_name = 'Ethereum ➡'

def show_ethereum_name():
    '''
    :return: Название Ethereum
    '''
    return ethereum_name

def show_ethereum():
    '''
    :return: Ethereum
    '''
    return ethereum_usd

litecoin_data = 'https://ru.investing.com/crypto/litecoin'
litecoin_page = requests.get(litecoin_data, headers=HEADERS).text
litecoin_soup = BeautifulSoup(litecoin_page, 'html.parser')
litecoin_convert = litecoin_soup.findAll('span', {'class': 'pid-1061445-last'})
litecoin_usd = litecoin_convert[0].text + USD
litecoin_name = 'Litecoin ➡'

def show_litecoin_name():
    '''
    :return: Название Litecoin
    '''
    return litecoin_name

def show_litecoin():
    '''
    :return: Litecoin
    '''
    return litecoin_usd

cardano_data = 'https://ru.investing.com/crypto/cardano/ada-usd'
cardano_page = requests.get(cardano_data, headers=HEADERS).text
cardano_soup = BeautifulSoup(cardano_page, 'html.parser')
cardano_convert = cardano_soup.findAll('span', {'class': 'text-2xl'})
cardano_usd = cardano_convert[0].text + USD
cardano_name = 'Cardano ➡'

def show_cardano_name():
    '''
    :return: Название Cardano
    '''
    return cardano_name

def show_cardano():
    '''
    :return: Cardano
    '''
    return cardano_usd

xrp_data = 'https://ru.investing.com/crypto/xrp/xrp-usd'
xrp_page = requests.get(xrp_data, headers=HEADERS).text
xrp_soup = BeautifulSoup(xrp_page, 'html.parser')
xrp_convert = xrp_soup.findAll('span', {'class': 'text-2xl'})
xrp_usd = xrp_convert[0].text + USD
xrp_name = 'XRP ➡'

def show_xrp_name():
    '''
    :return: Название XRP
    '''
    return xrp_name

def show_xrp():
    '''
    :return: XRP
    '''
    return xrp_usd

doge_data = 'https://ru.investing.com/crypto/dogecoin/doge-usd'
doge_page = requests.get(doge_data, headers=HEADERS).text
doge_soup = BeautifulSoup(doge_page, 'html.parser')
doge_convert = doge_soup.findAll('span', {'class': 'text-2xl'})
doge_usd = doge_convert[0].text + USD
doge_name = 'DOGE ➡'

def show_doge_name():
    '''
    :return: Название Doge Coin
    '''
    return doge_name

def show_doge():
    '''
    :return: Doge Coin
    '''
    return doge_usd

bnb_data = 'https://ru.investing.com/crypto/binance-coin'
bnb_page = requests.get(bnb_data, headers=HEADERS).text
bnb_soup = BeautifulSoup(bnb_page, 'html.parser')
bnb_convert = bnb_soup.findAll('span', {'class': 'pid-1061448-last'})
bnb_usd = bnb_convert[0].text + USD
bnb_name = 'BNB ➡'

def show_bnb_name():
    '''
    :return: Название BNB Coin
    '''
    return bnb_name

def show_bnb():
    '''
    :return: BNB Coin
    '''
    return bnb_usd

tether_data = 'https://ru.investing.com/crypto/tether'
tether_page = requests.get(tether_data, headers=HEADERS).text
tether_soup = BeautifulSoup(tether_page, 'html.parser')
tether_convert = tether_soup.findAll('span', {'class': 'pid-1061453-last'})
tether_usd = tether_convert[0].text + USD
tether_name = 'Tether ➡'

def show_tether_name():
    '''
    :return: Название Tether dollar
    '''
    return tether_name

def show_tether():
    '''
    :return: Tether dollar
    '''
    return tether_usd

solana_data = 'https://ru.investing.com/crypto/solana'
solana_page = requests.get(solana_data, headers=HEADERS).text
solana_soup = BeautifulSoup(solana_page, 'html.parser')
solana_convert = solana_soup.findAll('span', {'class': 'pid-1177183-last'})
solana_usd = solana_convert[0].text + USD
solana_name = 'Solana ➡'

def show_solana_name():
    '''
    :return: Название Solana
    '''
    return solana_name

def show_solana():
    '''
    :return: Solana
    '''
    return solana_usd

terra_data = 'https://ru.investing.com/crypto/terra-luna'
terra_page = requests.get(terra_data, headers=HEADERS).text
terra_soup = BeautifulSoup(terra_page, 'html.parser')
terra_convert = terra_soup.findAll('span', {'class': 'pid-1177187-last'})
terra_usd = terra_convert[0].text + USD
terra_name = 'Terra ➡'

def show_terra_name():
    '''
    :return: Название Terra Coin
    '''
    return terra_name

def show_terra():
    '''
    :return: Terra Coin
    '''
    return terra_usd

uniswap_data = 'https://ru.investing.com/crypto/uniswap'
uniswap_page = requests.get(uniswap_data, headers=HEADERS).text
uniswap_soup = BeautifulSoup(uniswap_page, 'html.parser')
uniswap_convert = uniswap_soup.findAll('span', {'class': 'pid-1177189-last'})
uniswap_usd = uniswap_convert[0].text + USD
uniswap_name = 'UniSwap ➡'

def show_uniswap_name():
    '''
    :return: Название UniSwap Token
    '''
    return uniswap_name

def show_uniswap():
    '''
    :return: UniSwap Token
    '''
    return uniswap_usd

polkadot_data = 'https://ru.investing.com/crypto/polkadot-new'
polkadot_page = requests.get(polkadot_data, headers=HEADERS).text
polkadot_soup = BeautifulSoup(polkadot_page, 'html.parser')
polkadot_convert = polkadot_soup.findAll('span', {'class': 'pid-1177185-last'})
polkadot_usd = polkadot_convert[0].text + USD
polkadot_name = 'Polkadot ➡'

def show_polkadot_name():
    '''
    :return: Название Polkadot Coin
    '''
    return polkadot_name

def show_dot():
    '''
    :return: Polkadot Coin
    '''
    return polkadot_usd

avalanche_data = 'https://ru.investing.com/crypto/avalanche'
avalanche_page = requests.get(avalanche_data, headers=HEADERS).text
avalanche_soup = BeautifulSoup(avalanche_page, 'html.parser')
avalanche_convert = avalanche_soup.findAll('span', {'class': 'pid-1177190-last'})
avalanche_usd = avalanche_convert[0].text + USD
avalanche_name = 'Avalanche ➡️'

def show_avalanche_name():
    '''
    :return: Название Avalanche Coin
    '''
    return avalanche_name

def show_avalanche():
    '''
    :return: Avalanche Coin
    '''
    return avalanche_usd

chainlink_data = 'https://ru.investing.com/crypto/chainlink'
chainlink_page = requests.get(chainlink_data, headers=HEADERS).text
chainlink_soup = BeautifulSoup(chainlink_page, 'html.parser')
chainlink_convert = chainlink_soup.findAll('span', {'class': 'pid-1061794-last'})
chainlink_usd = chainlink_convert[0].text + USD
chainlink_name = 'Chainlink ➡'

def show_chainlink_name():
    '''
    :return: Название Chainlink Coin
    '''
    return chainlink_name

def show_chainlink():
    '''
    :return: Chainlink Coin
    '''
    return chainlink_usd

tron_data = 'https://ru.investing.com/crypto/tron'
tron_page = requests.get(tron_data, headers=HEADERS).text
tron_soup = BeautifulSoup(tron_page, 'html.parser')
tron_convert = tron_soup.findAll('span', {'class': 'pid-1061450-last'})
tron_usd = tron_convert[0].text + USD
tron_name = 'Tron ➡'

def show_tron_name():
    '''
    :return: Название Tron Coin
    '''
    return tron_name

def show_tron():
    '''
    :return: Tron Coin
    '''
    return tron_usd

shiba_data = 'https://ru.investing.com/crypto/shiba-inu'
shiba_page = requests.get(shiba_data, headers=HEADERS).text
shiba_soup = BeautifulSoup(shiba_page, 'html.parser')
shiba_convert = shiba_soup.findAll('span', {'class': 'pid-1177506-last'})
shiba_usd = shiba_convert[0].text + USD
shiba_name = 'SHIBA ➡'

def show_shiba_name():
    '''
    :return:
    '''
    return shiba_name

def show_shiba():
    '''
    :return: Shiba Coin
    '''
    return shiba_usd