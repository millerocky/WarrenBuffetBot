import unittest
from WarrenBuffetBot.cryptocurrencies.crypto import Cryptocurrencies

class TestCryptocurrencies(unittest.TestCase):
    def setUp(self):
        self.bitcoin = Cryptocurrencies('https://ru.investing.com/crypto/bitcoin', html_class_parsing={'class': 'pid-1057391-last'},
                           name='Bitcoin ➡ ')
        self.ethereum = Cryptocurrencies('https://ru.investing.com/crypto/ethereum/eth-usd', html_class_parsing={'class': 'text-2xl'},
                            name='Ethereum ➡ ')

    def test_init(self):
        self.assertEqual((self.bitcoin.link, self.bitcoin.html_class_parsing, self.bitcoin.name), (str('https://ru.investing.com/crypto/bitcoin'), dict({'class': 'pid-1057391-last'}), str('Bitcoin ➡ ')))
        self.assertEqual((self.ethereum.link, self.ethereum.html_class_parsing, self.ethereum.name), (str('https://ru.investing.com/crypto/ethereum/eth-usd'), dict({'class': 'text-2xl'}), str('Ethereum ➡ ')))

if __name__ == '__main__':
    unittest.main()