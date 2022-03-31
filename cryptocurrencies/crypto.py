import requests
from bs4 import BeautifulSoup


class Cryptocurrencies:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

    def __init__(self, link_to_cryptocurrency, html_class_parsing, name_cryptocurrency):
        self.link_to_cryptocurrency = link_to_cryptocurrency
        self.html_class_parsing = html_class_parsing
        self.name_cryptocurrency = name_cryptocurrency

    def get_cryptocurrency_value(self):
        # Парсим всю страницу
        full_page = requests.get(self.link_to_cryptocurrency, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name_cryptocurrency}{convert[0].text}'

bitcoin = Cryptocurrencies('https://ru.investing.com/crypto/bitcoin', html_class_parsing={'class': 'pid-1057391-last'},
                           name_cryptocurrency='Bitcoin ➡ ')
ethereum = Cryptocurrencies('https://ru.investing.com/crypto/ethereum/eth-usd', html_class_parsing={'class': 'text-2xl'},
                            name_cryptocurrency='Ethereum ➡ ')
litecoin = Cryptocurrencies('https://ru.investing.com/crypto/litecoin', html_class_parsing={'class': 'pid-1061445-last'},
                            name_cryptocurrency='Litecoin ➡ ')
cardano = Cryptocurrencies('https://ru.investing.com/crypto/cardano/ada-usd', html_class_parsing={'class': 'text-2xl'},
                           name_cryptocurrency='Cardano ➡ ')
xrp = Cryptocurrencies('https://ru.investing.com/crypto/xrp/xrp-usd', html_class_parsing={'class': 'text-2xl'},
                       name_cryptocurrency='XRP ➡ ')
doge = Cryptocurrencies('https://ru.investing.com/crypto/dogecoin/doge-usd', html_class_parsing={'class': 'text-2xl'},
                        name_cryptocurrency='DOGE ➡ ')
bnb = Cryptocurrencies('https://ru.investing.com/crypto/binance-coin', html_class_parsing={'class': 'pid-1061448-last'},
                       name_cryptocurrency='BNB ➡ ')
tether = Cryptocurrencies('https://ru.investing.com/crypto/tether', html_class_parsing={'class': 'pid-1061453-last'},
                          name_cryptocurrency='Tether ➡ ')
solana = Cryptocurrencies('https://ru.investing.com/crypto/solana', html_class_parsing={'class': 'pid-1177183-last'},
                          name_cryptocurrency='Solana ➡ ')
luna = Cryptocurrencies('https://ru.investing.com/crypto/terra-luna', html_class_parsing={'class': 'pid-1177187-last'},
                        name_cryptocurrency='Luna ➡ ')
uniswap = Cryptocurrencies('https://ru.investing.com/crypto/uniswap', html_class_parsing={'class': 'pid-1177189-last'},
                           name_cryptocurrency='UniSwap ➡ ')
polkadot = Cryptocurrencies('https://ru.investing.com/crypto/polkadot-new', html_class_parsing={'class': 'pid-1177185-last'},
                            name_cryptocurrency='Polkadot ➡ ')
avalanche = Cryptocurrencies('https://ru.investing.com/crypto/avalanche', html_class_parsing={'class': 'pid-1177190-last'},
                             name_cryptocurrency='Avalanche ➡ ')
chainlink = Cryptocurrencies('https://ru.investing.com/crypto/chainlink', html_class_parsing={'class': 'pid-1061794-last'},
                             name_cryptocurrency='Chainlink ➡ ')
tron = Cryptocurrencies('https://ru.investing.com/crypto/tron', html_class_parsing={'class': 'pid-1061450-last'},
                        name_cryptocurrency='Tron ➡ ')
shiba = Cryptocurrencies('https://ru.investing.com/crypto/shiba-inu', html_class_parsing={'class': 'pid-1177506-last'},
                         name_cryptocurrency='SHIBA ➡ ')