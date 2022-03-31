import requests
from bs4 import BeautifulSoup
from WarrenBuffetBot.core_class.core_class import Parsing


class Cryptocurrencies(Parsing):
    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'

bitcoin = Cryptocurrencies('https://ru.investing.com/crypto/bitcoin', html_class_parsing={'class': 'pid-1057391-last'},
                           name='Bitcoin ➡ ')
ethereum = Cryptocurrencies('https://ru.investing.com/crypto/ethereum/eth-usd', html_class_parsing={'class': 'text-2xl'},
                            name='Ethereum ➡ ')
litecoin = Cryptocurrencies('https://ru.investing.com/crypto/litecoin', html_class_parsing={'class': 'pid-1061445-last'},
                            name='Litecoin ➡ ')
cardano = Cryptocurrencies('https://ru.investing.com/crypto/cardano/ada-usd', html_class_parsing={'class': 'text-2xl'},
                           name='Cardano ➡ ')
xrp = Cryptocurrencies('https://ru.investing.com/crypto/xrp/xrp-usd', html_class_parsing={'class': 'text-2xl'},
                       name='XRP ➡ ')
doge = Cryptocurrencies('https://ru.investing.com/crypto/dogecoin/doge-usd', html_class_parsing={'class': 'text-2xl'},
                        name='DOGE ➡ ')
bnb = Cryptocurrencies('https://ru.investing.com/crypto/binance-coin', html_class_parsing={'class': 'pid-1061448-last'},
                       name='BNB ➡ ')
tether = Cryptocurrencies('https://ru.investing.com/crypto/tether', html_class_parsing={'class': 'pid-1061453-last'},
                          name='Tether ➡ ')
solana = Cryptocurrencies('https://ru.investing.com/crypto/solana', html_class_parsing={'class': 'pid-1177183-last'},
                          name='Solana ➡ ')
luna = Cryptocurrencies('https://ru.investing.com/crypto/terra-luna', html_class_parsing={'class': 'pid-1177187-last'},
                        name='Luna ➡ ')
uniswap = Cryptocurrencies('https://ru.investing.com/crypto/uniswap', html_class_parsing={'class': 'pid-1177189-last'},
                           name='UniSwap ➡ ')
polkadot = Cryptocurrencies('https://ru.investing.com/crypto/polkadot-new', html_class_parsing={'class': 'pid-1177185-last'},
                            name='Polkadot ➡ ')
avalanche = Cryptocurrencies('https://ru.investing.com/crypto/avalanche', html_class_parsing={'class': 'pid-1177190-last'},
                             name='Avalanche ➡ ')
chainlink = Cryptocurrencies('https://ru.investing.com/crypto/chainlink', html_class_parsing={'class': 'pid-1061794-last'},
                             name='Chainlink ➡ ')
tron = Cryptocurrencies('https://ru.investing.com/crypto/tron', html_class_parsing={'class': 'pid-1061450-last'},
                        name='Tron ➡ ')
shiba = Cryptocurrencies('https://ru.investing.com/crypto/shiba-inu', html_class_parsing={'class': 'pid-1177506-last'},
                         name='SHIBA ➡ ')