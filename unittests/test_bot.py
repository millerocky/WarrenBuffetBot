import unittest
from WarrenBuffetBot.cryptocurrencies.crypto import Cryptocurrencies
from WarrenBuffetBot.currency.currency import Currency, link_to_usd_rub, link_to_euro_rub
from WarrenBuffetBot.stocksRU.IT_sector_RU.stocks_IT_sector import stocksItSectorRus
from WarrenBuffetBot.stocksRU.basic_sector_RU.stocks_basic_sector import stocksBasicSectorRus
from WarrenBuffetBot.stocksRU.finance_sector_RU.stocks_finance_sector import stocksFinancialSectorRus
from WarrenBuffetBot.stocksRU.industrial_sector.stocks_industrial_sector import stocksIndustrialSectorRus
from WarrenBuffetBot.stocksRU.realEstate_RU.realEstate_sector import stocksRealEstate
from WarrenBuffetBot.stocksUSA.stocks_USA import stocksUsa
from WarrenBuffetBot.stocks_China.stock_China import stocksChina


class TestCryptocurrencies(unittest.TestCase):
    def setUp(self):
        self.bitcoin = Cryptocurrencies('https://ru.investing.com/crypto/bitcoin',
                                        html_class_parsing={'class': 'pid-1057391-last'},
                                        name='Bitcoin ➡ ')
        self.ethereum = Cryptocurrencies('https://ru.investing.com/crypto/ethereum/eth-usd',
                                         html_class_parsing={'class': 'text-2xl'},
                                         name='Ethereum ➡ ')
        self.litecoin = Cryptocurrencies('https://ru.investing.com/crypto/litecoin',
                                         html_class_parsing={'class': 'pid-1061445-last'},
                                         name='Litecoin ➡ ')
        self.cardano = Cryptocurrencies('https://ru.investing.com/crypto/cardano/ada-usd',
                                        html_class_parsing={'class': 'text-2xl'},
                                        name='Cardano ➡ ')
        self.xrp = Cryptocurrencies('https://ru.investing.com/crypto/xrp/xrp-usd',
                                    html_class_parsing={'class': 'text-2xl'},
                                    name='XRP ➡ ')
        self.doge = Cryptocurrencies('https://ru.investing.com/crypto/dogecoin/doge-usd',
                                     html_class_parsing={'class': 'text-2xl'},
                                     name='DOGE ➡ ')
        self.bnb = Cryptocurrencies('https://ru.investing.com/crypto/binance-coin',
                                    html_class_parsing={'class': 'pid-1061448-last'},
                                    name='BNB ➡ ')
        self.tether = Cryptocurrencies('https://ru.investing.com/crypto/tether',
                                       html_class_parsing={'class': 'pid-1061453-last'},
                                       name='Tether ➡ ')
        self.solana = Cryptocurrencies('https://ru.investing.com/crypto/solana',
                                       html_class_parsing={'class': 'pid-1177183-last'},
                                       name='Solana ➡ ')
        self.luna = Cryptocurrencies('https://ru.investing.com/crypto/terra-luna',
                                     html_class_parsing={'class': 'pid-1177187-last'},
                                     name='Luna ➡ ')
        self.uniswap = Cryptocurrencies('https://ru.investing.com/crypto/uniswap',
                                        html_class_parsing={'class': 'pid-1177189-last'},
                                        name='UniSwap ➡ ')
        self.polkadot = Cryptocurrencies('https://ru.investing.com/crypto/polkadot-new',
                                         html_class_parsing={'class': 'pid-1177185-last'},
                                         name='Polkadot ➡ ')
        self.avalanche = Cryptocurrencies('https://ru.investing.com/crypto/avalanche',
                                          html_class_parsing={'class': 'pid-1177190-last'},
                                          name='Avalanche ➡ ')
        self.chainlink = Cryptocurrencies('https://ru.investing.com/crypto/chainlink',
                                          html_class_parsing={'class': 'pid-1061794-last'},
                                          name='Chainlink ➡ ')
        self.tron = Cryptocurrencies('https://ru.investing.com/crypto/tron',
                                     html_class_parsing={'class': 'pid-1061450-last'},
                                     name='Tron ➡ ')
        self.shiba = Cryptocurrencies('https://ru.investing.com/crypto/shiba-inu',
                                      html_class_parsing={'class': 'pid-1177506-last'},
                                      name='SHIBA ➡ ')

    def test_init(self):
        self.assertEqual((self.bitcoin.link, self.bitcoin.html_class_parsing, self.bitcoin.name), (
            str('https://ru.investing.com/crypto/bitcoin'), dict({'class': 'pid-1057391-last'}), str('Bitcoin ➡ ')))
        self.assertEqual((self.ethereum.link, self.ethereum.html_class_parsing, self.ethereum.name), (
            str('https://ru.investing.com/crypto/ethereum/eth-usd'), dict({'class': 'text-2xl'}), str('Ethereum ➡ ')))
        self.assertEqual((self.litecoin.link, self.litecoin.html_class_parsing, self.litecoin.name), (
            str('https://ru.investing.com/crypto/litecoin'), dict({'class': 'pid-1061445-last'}), str('Litecoin ➡ ')))
        self.assertEqual((self.cardano.link, self.cardano.html_class_parsing, self.cardano.name), (
            str('https://ru.investing.com/crypto/cardano/ada-usd'), dict({'class': 'text-2xl'}), str('Cardano ➡ ')))
        self.assertEqual((self.xrp.link, self.xrp.html_class_parsing, self.xrp.name), (
            str('https://ru.investing.com/crypto/xrp/xrp-usd'), dict({'class': 'text-2xl'}), str('XRP ➡ ')))
        self.assertEqual((self.doge.link, self.doge.html_class_parsing, self.doge.name), (
            str('https://ru.investing.com/crypto/dogecoin/doge-usd'), dict({'class': 'text-2xl'}), str('DOGE ➡ ')))
        self.assertEqual((self.bnb.link, self.bnb.html_class_parsing, self.bnb.name), (
            str('https://ru.investing.com/crypto/binance-coin'), dict({'class': 'pid-1061448-last'}), str('BNB ➡ ')))
        self.assertEqual((self.tether.link, self.tether.html_class_parsing, self.tether.name), (
            str('https://ru.investing.com/crypto/tether'), dict({'class': 'pid-1061453-last'}), str('Tether ➡ ')))
        self.assertEqual((self.solana.link, self.solana.html_class_parsing, self.solana.name), (
            str('https://ru.investing.com/crypto/solana'), dict({'class': 'pid-1177183-last'}), str('Solana ➡ ')))
        self.assertEqual((self.luna.link, self.luna.html_class_parsing, self.luna.name), (
            str('https://ru.investing.com/crypto/terra-luna'), dict({'class': 'pid-1177187-last'}), str('Luna ➡ ')))
        self.assertEqual((self.uniswap.link, self.uniswap.html_class_parsing, self.uniswap.name), (
            str('https://ru.investing.com/crypto/uniswap'), dict({'class': 'pid-1177189-last'}), str('UniSwap ➡ ')))
        self.assertEqual((self.polkadot.link, self.polkadot.html_class_parsing, self.polkadot.name), (
            str('https://ru.investing.com/crypto/polkadot-new'), dict({'class': 'pid-1177185-last'}),
            str('Polkadot ➡ ')))
        self.assertEqual((self.avalanche.link, self.avalanche.html_class_parsing, self.avalanche.name), (
            str('https://ru.investing.com/crypto/avalanche'), dict({'class': 'pid-1177190-last'}), str('Avalanche ➡ ')))
        self.assertEqual((self.tron.link, self.tron.html_class_parsing, self.tron.name), (
            str('https://ru.investing.com/crypto/tron'), dict({'class': 'pid-1061450-last'}), str('Tron ➡ ')))
        self.assertEqual((self.shiba.link, self.shiba.html_class_parsing, self.shiba.name), (
            str('https://ru.investing.com/crypto/shiba-inu'), dict({'class': 'pid-1177506-last'}), str('SHIBA ➡ ')))


class TestCurrencies(unittest.TestCase):
    def setUp(self):
        self.usd_rub = Currency(link_to_currency=link_to_usd_rub)
        self.euro_rub = Currency(link_to_currency=link_to_euro_rub)

    def test_init(self):
        self.assertEqual((self.usd_rub.link_to_currency), (str(link_to_usd_rub)))
        self.assertEqual((self.euro_rub.link_to_currency), (str(link_to_euro_rub)))


class TestStocksChina(unittest.TestCase):
    def setUp(self):
        self.liauto = stocksChina('https://ru.investing.com/equities/li-auto-inc',
                                  html_class_parsing={'class': 'text-2xl'},
                                  name='Li Auto ➡ ')
        self.baidu = stocksChina('https://ru.investing.com/equities/baidu.com',
                                 html_class_parsing={'class': 'text-2xl'},
                                 name='Baidu ➡ ')
        self.jd = stocksChina('https://ru.investing.com/equities/jd.com-inc-adr',
                              html_class_parsing={'class': 'text-2xl'},
                              name='JD ➡ ')
        self.bilibili = stocksChina('https://ru.investing.com/equities/bilibili-inc',
                                    html_class_parsing={'class': 'text-2xl'},
                                    name='Bilibili Inc. ➡ ')
        self.tencent = stocksChina('https://ru.investing.com/equities/tencent-holdings-pk',
                                   html_class_parsing={'class': 'text-2xl'},
                                   name='Tencent Holdings ➡ ')
        self.nio = stocksChina('https://ru.investing.com/equities/nio-inc',
                               html_class_parsing={'class': 'text-2xl'},
                               name='Nio Inc. ➡ ')
        self.xpeng = stocksChina('https://ru.investing.com/equities/xpeng-inc',
                                 html_class_parsing={'class': 'text-2xl'},
                                 name='Xpeng Inc. ➡ ')

    def test_init(self):
        self.assertEqual((self.liauto.link, self.liauto.html_class_parsing, self.liauto.name), (
            str('https://ru.investing.com/equities/li-auto-inc'), dict({'class': 'text-2xl'}), str('Li Auto ➡ ')))
        self.assertEqual((self.baidu.link, self.baidu.html_class_parsing, self.baidu.name), (
            str('https://ru.investing.com/equities/baidu.com'), dict({'class': 'text-2xl'}), str('Baidu ➡ ')))
        self.assertEqual((self.jd.link, self.jd.html_class_parsing, self.jd.name), (
            str('https://ru.investing.com/equities/jd.com-inc-adr'), dict({'class': 'text-2xl'}), str('JD ➡ ')))
        self.assertEqual((self.bilibili.link, self.bilibili.html_class_parsing, self.bilibili.name), (
            str('https://ru.investing.com/equities/bilibili-inc'), dict({'class': 'text-2xl'}),
            str('Bilibili Inc. ➡ ')))
        self.assertEqual((self.tencent.link, self.tencent.html_class_parsing, self.tencent.name), (
            str('https://ru.investing.com/equities/tencent-holdings-pk'), dict({'class': 'text-2xl'}),
            str('Tencent Holdings ➡ ')))
        self.assertEqual((self.nio.link, self.nio.html_class_parsing, self.nio.name), (
            str('https://ru.investing.com/equities/nio-inc'), dict({'class': 'text-2xl'}), str('Nio Inc. ➡ ')))
        self.assertEqual((self.xpeng.link, self.xpeng.html_class_parsing, self.xpeng.name), (
            str('https://ru.investing.com/equities/xpeng-inc'), dict({'class': 'text-2xl'}), str('Xpeng Inc. ➡ ')))


class TestStocksRus(unittest.TestCase):
    def setUp(self):
        self.magnit = stocksBasicSectorRus('https://ru.investing.com/equities/magnit_rts',
                                           html_class_parsing={'class': 'text-2xl'},
                                           name='Магнит ➡ ')
        self.x5retail = stocksBasicSectorRus('https://ru.investing.com/equities/x5-retail-grp?cid=1061926',
                                             html_class_parsing={'class': 'text-2xl'},
                                             name='X5 Retail Group ➡ ')
        self.detskiymir = stocksBasicSectorRus('https://ru.investing.com/equities/detskiy-mir-pao',
                                               html_class_parsing={'class': 'text-2xl'},
                                               name='Детский мир ➡ ')
        self.fixprice = stocksBasicSectorRus('https://ru.investing.com/equities/fix-price-group-drc?cid=1171256',
                                             html_class_parsing={'class': 'text-2xl'},
                                             name='Fix Price Group ➡ ')
        self.mvideo = stocksBasicSectorRus('https://ru.investing.com/equities/mvideo_rts',
                                           html_class_parsing={'class': 'text-2xl'},
                                           name='МВидео ➡ ')
        self.cherkizovo = stocksBasicSectorRus('https://ru.investing.com/equities/gruppa-cherkizovo',
                                               html_class_parsing={'class': 'text-2xl'},
                                               name='Черкизово ➡ ')
        self.vtb = stocksFinancialSectorRus('https://ru.investing.com/equities/vtb_rts',
                                            html_class_parsing={'class': 'text-2xl'},
                                            name='ВТБ ➡ ')
        self.tinkoffbank = stocksFinancialSectorRus(
            'https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662',
            html_class_parsing={'class': 'text-2xl'},
            name='TCS Group ➡ ')
        self.mkb = stocksFinancialSectorRus('https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao',
                                            html_class_parsing={'class': 'text-2xl'},
                                            name='МКБ ➡ ')
        self.sber = stocksFinancialSectorRus('https://ru.investing.com/equities/sberbank_rts',
                                             html_class_parsing={'class': 'text-2xl'},
                                             name='Сбер Банк ➡ ')
        self.sberprevs = stocksFinancialSectorRus('https://ru.investing.com/equities/sberbank-p_rts',
                                                  html_class_parsing={'class': 'text-2xl'},
                                                  name='Сбер Банк - привилегированные акции ➡ ')
        self.afk = stocksFinancialSectorRus('https://ru.investing.com/equities/afk-sistema_rts',
                                            html_class_parsing={'class': 'text-2xl'},
                                            name='АФК Система ➡ ')
        self.spbbank = stocksFinancialSectorRus('https://ru.investing.com/equities/bank-st-petersbr_rts',
                                                html_class_parsing={'class': 'text-2xl'},
                                                name='Банк Санкт-Петербург ➡ ')
        self.globaltrans = stocksIndustrialSectorRus(
            'https://ru.investing.com/equities/globaltrans-inv?cid=1167212',
            html_class_parsing={'class': 'text-2xl'},
            name='Globaltrans Investment ➡ ')
        self.petropavlovsk = stocksIndustrialSectorRus(
            'https://ru.investing.com/equities/petropavlovsk?cid=1163242',
            html_class_parsing={'class': 'text-2xl'},
            name='Petropavlovsk ➡ ')
        self.polymetal = stocksIndustrialSectorRus('https://ru.investing.com/equities/polymetal?cid=44465',
                                                   html_class_parsing={'class': 'text-2xl'},
                                                   name='Polymetal ➡ ')
        self.alrosa = stocksIndustrialSectorRus('https://ru.investing.com/equities/alrosa-ao',
                                                html_class_parsing={'class': 'text-2xl'},
                                                name='АК АЛРОСА ➡ ')
        self.aeroflot = stocksIndustrialSectorRus('https://ru.investing.com/equities/aeroflot',
                                                  html_class_parsing={'class': 'text-2xl'},
                                                  name='АЭРОФЛОТ ➡ ')
        self.gazprom = stocksIndustrialSectorRus('https://ru.investing.com/equities/gazprom_rts',
                                                 html_class_parsing={'class': 'text-2xl'},
                                                 name='ГАЗПРОМ ➡ ')
        self.interrao = stocksIndustrialSectorRus('https://ru.investing.com/equities/inter-rao-ees_mm',
                                                  html_class_parsing={'class': 'text-2xl'},
                                                  name='ИнтерРАО ➡ ')
        self.lukoil = stocksIndustrialSectorRus('https://ru.investing.com/equities/lukoil_rts',
                                                html_class_parsing={'class': 'text-2xl'},
                                                name='ЛУКОЙЛ ➡ ')
        self.mmk = stocksIndustrialSectorRus('https://ru.investing.com/equities/mmk_rts',
                                             html_class_parsing={'class': 'text-2xl'},
                                             name='ММК ➡ ')
        self.nlmk = stocksIndustrialSectorRus('https://ru.investing.com/equities/nlmk_rts',
                                              html_class_parsing={'class': 'text-2xl'},
                                              name='НЛМК ➡ ')
        self.novatek = stocksIndustrialSectorRus('https://ru.investing.com/equities/novatek_rts',
                                                 html_class_parsing={'class': 'text-2xl'},
                                                 name='НОВАТЕК ➡ ')
        self.nornikel = stocksIndustrialSectorRus('https://ru.investing.com/equities/gmk-noril-nickel_rts',
                                                  html_class_parsing={'class': 'text-2xl'},
                                                  name='НОРНИКЕЛЬ ➡ ')
        self.polyus = stocksIndustrialSectorRus('https://ru.investing.com/equities/polyus-zoloto_rts',
                                                html_class_parsing={'class': 'text-2xl'},
                                                name='Polyus ➡ ')
        self.rosneft = stocksIndustrialSectorRus('https://ru.investing.com/equities/rosneft_rts',
                                                 html_class_parsing={'class': 'text-2xl'},
                                                 name='Роснефть ➡ ')
        self.rusal = stocksIndustrialSectorRus('https://ru.investing.com/equities/united-company-rusal-plc%60',
                                               html_class_parsing={'class': 'text-2xl'},
                                               name='РУСАЛ ➡ ')
        self.rushydro = stocksIndustrialSectorRus('https://ru.investing.com/equities/gidroogk-011d',
                                                  html_class_parsing={'class': 'text-2xl'},
                                                  name='РусГидро ➡ ')
        self.severstal = stocksIndustrialSectorRus('https://ru.investing.com/equities/severstal_rts',
                                                   html_class_parsing={'class': 'text-2xl'},
                                                   name='Северсталь ➡ ')
        self.surgutneft = stocksIndustrialSectorRus('https://ru.investing.com/equities/surgutneftegas_rts',
                                                    html_class_parsing={'class': 'text-2xl'},
                                                    name='Сургутнефтегаз ➡ ')
        self.tatneft = stocksIndustrialSectorRus('https://ru.investing.com/equities/tatneft_rts',
                                                 html_class_parsing={'class': 'text-2xl'},
                                                 name='Татнефть ➡ ')
        self.transneft = stocksIndustrialSectorRus('https://ru.investing.com/equities/transneft-p_rts',
                                                   html_class_parsing={'class': 'text-2xl'},
                                                   name='Трансненфть ➡ ')
        self.phosagro = stocksIndustrialSectorRus('https://ru.investing.com/equities/phosagro',
                                                  html_class_parsing={'class': 'text-2xl'},
                                                  name='ФосАгро ➡ ')
        self.fsk = stocksIndustrialSectorRus('https://ru.investing.com/equities/fsk-ees_rts',
                                             html_class_parsing={'class': 'text-2xl'},
                                             name='ФСК ➡ ')
        self.hhru = stocksItSectorRus('https://ru.investing.com/equities/headhunter-group-plc?cid=1166764',
                                      html_class_parsing={'class': 'text-2xl'},
                                      name='HeadHunter ➡ ')
        self.yandex = stocksItSectorRus('https://ru.investing.com/equities/yandex?cid=102063',
                                        html_class_parsing={'class': 'text-2xl'},
                                        name='Яндекс ➡ ')
        self.vk = stocksItSectorRus('https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363',
                                    html_class_parsing={'class': 'text-2xl'},
                                    name='Vk ➡ ')
        self.mts = stocksItSectorRus('https://ru.investing.com/equities/mts_rts',
                                     html_class_parsing={'class': 'text-2xl'},
                                     name='МТС ➡ ')
        self.ozon = stocksItSectorRus('https://ru.investing.com/equities/ozon-holdings-plc?cid=1167498',
                                      html_class_parsing={'class': 'text-2xl'},
                                      name='Ozon Holdings ➡ ')
        self.qiwi = stocksItSectorRus('https://ru.investing.com/equities/qiwi-plc?cid=960754',
                                      html_class_parsing={'class': 'text-2xl'},
                                      name='Qiwi ➡ ')
        self.rosseti = stocksItSectorRus('https://ru.investing.com/equities/rosseti-ao',
                                         html_class_parsing={'class': 'text-2xl'},
                                         name='Россети ➡ ')
        self.rostelecom = stocksItSectorRus('https://ru.investing.com/equities/rostelecom',
                                            html_class_parsing={'class': 'text-2xl'},
                                            name='Ростелеком ➡ ')
        self.pik = stocksRealEstate('https://ru.investing.com/equities/pik_rts',
                                    html_class_parsing={'class': 'text-2xl'},
                                    name='Группа ПИК ➡ ')
        self.lsr = stocksRealEstate('https://ru.investing.com/equities/lsr-group_rts',
                                    html_class_parsing={'class': 'text-2xl'},
                                    name='ЛСР ➡ ')

    def test_init(self):
        self.assertEqual((self.magnit.link, self.magnit.html_class_parsing, self.magnit.name), (
            str('https://ru.investing.com/equities/magnit_rts'), dict({'class': 'text-2xl'}), str('Магнит ➡ ')))
        self.assertEqual((self.x5retail.link, self.x5retail.html_class_parsing, self.x5retail.name), (
            str('https://ru.investing.com/equities/x5-retail-grp?cid=1061926'), dict({'class': 'text-2xl'}),
            str('X5 Retail Group ➡ ')))
        self.assertEqual((self.detskiymir.link, self.detskiymir.html_class_parsing, self.detskiymir.name), (
            str('https://ru.investing.com/equities/detskiy-mir-pao'), dict({'class': 'text-2xl'}),
            str('Детский мир ➡ ')))
        self.assertEqual((self.fixprice.link, self.fixprice.html_class_parsing, self.fixprice.name), (
            str('https://ru.investing.com/equities/fix-price-group-drc?cid=1171256'), dict({'class': 'text-2xl'}),
            str('Fix Price Group ➡ ')))
        self.assertEqual((self.mvideo.link, self.mvideo.html_class_parsing, self.mvideo.name), (
            str('https://ru.investing.com/equities/mvideo_rts'), dict({'class': 'text-2xl'}), str('МВидео ➡ ')))
        self.assertEqual((self.cherkizovo.link, self.cherkizovo.html_class_parsing, self.cherkizovo.name), (
            str('https://ru.investing.com/equities/gruppa-cherkizovo'), dict({'class': 'text-2xl'}),
            str('Черкизово ➡ ')))
        self.assertEqual((self.vtb.link, self.vtb.html_class_parsing, self.vtb.name), (
            str('https://ru.investing.com/equities/vtb_rts'), dict({'class': 'text-2xl'}), str('ВТБ ➡ ')))
        self.assertEqual((self.tinkoffbank.link, self.tinkoffbank.html_class_parsing, self.tinkoffbank.name),
                         (str('https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662'),
                          dict({'class': 'text-2xl'}), str('TCS Group ➡ ')))
        self.assertEqual((self.mkb.link, self.mkb.html_class_parsing, self.mkb.name), (
            str('https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao'), dict({'class': 'text-2xl'}),
            str('МКБ ➡ ')))
        self.assertEqual((self.sber.link, self.sber.html_class_parsing, self.sber.name), (
            str('https://ru.investing.com/equities/sberbank_rts'), dict({'class': 'text-2xl'}),
            str('Сбер Банк ➡ ')))
        self.assertEqual((self.sberprevs.link, self.sberprevs.html_class_parsing, self.sberprevs.name), (
            str('https://ru.investing.com/equities/sberbank-p_rts'), dict({'class': 'text-2xl'}),
            str('Сбер Банк - привилегированные акции ➡ ')))
        self.assertEqual((self.afk.link, self.afk.html_class_parsing, self.afk.name), (
            str('https://ru.investing.com/equities/afk-sistema_rts'), dict({'class': 'text-2xl'}),
            str('АФК Система ➡ ')))
        self.assertEqual((self.spbbank.link, self.spbbank.html_class_parsing, self.spbbank.name), (
            str('https://ru.investing.com/equities/bank-st-petersbr_rts'), dict({'class': 'text-2xl'}),
            str('Банк Санкт-Петербург ➡ ')))
        self.assertEqual((self.globaltrans.link, self.globaltrans.html_class_parsing, self.globaltrans.name),
                         (str('https://ru.investing.com/equities/globaltrans-inv?cid=1167212'),
                          dict({'class': 'text-2xl'}), str('Globaltrans Investment ➡ ')))
        self.assertEqual((self.petropavlovsk.link, self.petropavlovsk.html_class_parsing, self.petropavlovsk.name),
                         (str('https://ru.investing.com/equities/petropavlovsk?cid=1163242'),
                          dict({'class': 'text-2xl'}), str('Petropavlovsk ➡ ')))
        self.assertEqual((self.polymetal.link, self.polymetal.html_class_parsing, self.polymetal.name),
                         (str('https://ru.investing.com/equities/polymetal?cid=44465'), dict({'class': 'text-2xl'}),
                          str('Polymetal ➡ ')))
        self.assertEqual((self.alrosa.link, self.alrosa.html_class_parsing, self.alrosa.name),
                         (str('https://ru.investing.com/equities/alrosa-ao'), dict({'class': 'text-2xl'}),
                          str('АК АЛРОСА ➡ ')))
        self.assertEqual((self.aeroflot.link, self.aeroflot.html_class_parsing, self.aeroflot.name),
                         (str('https://ru.investing.com/equities/aeroflot'), dict({'class': 'text-2xl'}),
                          str('АЭРОФЛОТ ➡ ')))
        self.assertEqual((self.gazprom.link, self.gazprom.html_class_parsing, self.gazprom.name),
                         (str('https://ru.investing.com/equities/gazprom_rts'), dict({'class': 'text-2xl'}),
                          str('ГАЗПРОМ ➡ ')))
        self.assertEqual((self.interrao.link, self.interrao.html_class_parsing, self.interrao.name),
                         (str('https://ru.investing.com/equities/inter-rao-ees_mm'), dict({'class': 'text-2xl'}),
                          str('ИнтерРАО ➡ ')))
        self.assertEqual((self.lukoil.link, self.lukoil.html_class_parsing, self.lukoil.name),
                         (str('https://ru.investing.com/equities/lukoil_rts'), dict({'class': 'text-2xl'}),
                          str('ЛУКОЙЛ ➡ ')))
        self.assertEqual((self.mmk.link, self.mmk.html_class_parsing, self.mmk.name),
                         (str('https://ru.investing.com/equities/mmk_rts'), dict({'class': 'text-2xl'}),
                          str('ММК ➡ ')))
        self.assertEqual((self.nlmk.link, self.nlmk.html_class_parsing, self.nlmk.name),
                         (str('https://ru.investing.com/equities/nlmk_rts'), dict({'class': 'text-2xl'}),
                          str('НЛМК ➡ ')))
        self.assertEqual((self.novatek.link, self.novatek.html_class_parsing, self.novatek.name),
                         (str('https://ru.investing.com/equities/novatek_rts'), dict({'class': 'text-2xl'}),
                          str('НОВАТЕК ➡ ')))
        self.assertEqual((self.nornikel.link, self.nornikel.html_class_parsing, self.nornikel.name),
                         (str('https://ru.investing.com/equities/gmk-noril-nickel_rts'),
                          dict({'class': 'text-2xl'}), str('НОРНИКЕЛЬ ➡ ')))
        self.assertEqual((self.polyus.link, self.polyus.html_class_parsing, self.polyus.name),
                         (str('https://ru.investing.com/equities/polyus-zoloto_rts'), dict({'class': 'text-2xl'}),
                          str('Polyus ➡ ')))
        self.assertEqual((self.rosneft.link, self.rosneft.html_class_parsing, self.rosneft.name),
                         (str('https://ru.investing.com/equities/rosneft_rts'), dict({'class': 'text-2xl'}),
                          str('Роснефть ➡ ')))
        self.assertEqual((self.rusal.link, self.rusal.html_class_parsing, self.rusal.name),
                         (str('https://ru.investing.com/equities/united-company-rusal-plc%60'),
                          dict({'class': 'text-2xl'}), str('РУСАЛ ➡ ')))
        self.assertEqual((self.rushydro.link, self.rushydro.html_class_parsing, self.rushydro.name),
                         (str('https://ru.investing.com/equities/gidroogk-011d'), dict({'class': 'text-2xl'}),
                          str('РусГидро ➡ ')))
        self.assertEqual((self.severstal.link, self.severstal.html_class_parsing, self.severstal.name),
                         (str('https://ru.investing.com/equities/severstal_rts'), dict({'class': 'text-2xl'}),
                          str('Северсталь ➡ ')))
        self.assertEqual((self.surgutneft.link, self.surgutneft.html_class_parsing, self.surgutneft.name),
                         (str('https://ru.investing.com/equities/surgutneftegas_rts'), dict({'class': 'text-2xl'}),
                          str('Сургутнефтегаз ➡ ')))
        self.assertEqual((self.tatneft.link, self.tatneft.html_class_parsing, self.tatneft.name),
                         (str('https://ru.investing.com/equities/tatneft_rts'), dict({'class': 'text-2xl'}),
                          str('Татнефть ➡ ')))
        self.assertEqual((self.transneft.link, self.transneft.html_class_parsing, self.transneft.name),
                         (str('https://ru.investing.com/equities/transneft-p_rts'), dict({'class': 'text-2xl'}),
                          str('Трансненфть ➡ ')))
        self.assertEqual((self.phosagro.link, self.phosagro.html_class_parsing, self.phosagro.name),
                         (str('https://ru.investing.com/equities/phosagro'), dict({'class': 'text-2xl'}),
                          str('ФосАгро ➡ ')))
        self.assertEqual((self.fsk.link, self.fsk.html_class_parsing, self.fsk.name),
                         (str('https://ru.investing.com/equities/fsk-ees_rts'), dict({'class': 'text-2xl'}),
                          str('ФСК ➡ ')))
        self.assertEqual((self.hhru.link, self.hhru.html_class_parsing, self.hhru.name),
                         (str('https://ru.investing.com/equities/headhunter-group-plc?cid=1166764'),
                          dict({'class': 'text-2xl'}), str('HeadHunter ➡ ')))
        self.assertEqual((self.yandex.link, self.yandex.html_class_parsing, self.yandex.name),
                         (str('https://ru.investing.com/equities/yandex?cid=102063'), dict({'class': 'text-2xl'}),
                          str('Яндекс ➡ ')))
        self.assertEqual((self.vk.link, self.vk.html_class_parsing, self.vk.name),
                         (str('https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363'),
                          dict({'class': 'text-2xl'}), str('Vk ➡ ')))
        self.assertEqual((self.mts.link, self.mts.html_class_parsing, self.mts.name),
                         (str('https://ru.investing.com/equities/mts_rts'), dict({'class': 'text-2xl'}),
                          str('МТС ➡ ')))
        self.assertEqual((self.ozon.link, self.ozon.html_class_parsing, self.ozon.name),
                         (str('https://ru.investing.com/equities/ozon-holdings-plc?cid=1167498'),
                          dict({'class': 'text-2xl'}), str('Ozon Holdings ➡ ')))
        self.assertEqual((self.qiwi.link, self.qiwi.html_class_parsing, self.qiwi.name),
                         (str('https://ru.investing.com/equities/qiwi-plc?cid=960754'),
                          dict({'class': 'text-2xl'}), str('Qiwi ➡ ')))
        self.assertEqual((self.rosseti.link, self.rosseti.html_class_parsing, self.rosseti.name),
                         (str('https://ru.investing.com/equities/rosseti-ao'), dict({'class': 'text-2xl'}),
                          str('Россети ➡ ')))
        self.assertEqual((self.rostelecom.link, self.rostelecom.html_class_parsing, self.rostelecom.name),
                         (str('https://ru.investing.com/equities/rostelecom'), dict({'class': 'text-2xl'}),
                          str('Ростелеком ➡ ')))
        self.assertEqual((self.pik.link, self.pik.html_class_parsing, self.pik.name),
                         (str('https://ru.investing.com/equities/pik_rts'), dict({'class': 'text-2xl'}),
                          str('Группа ПИК ➡ ')))
        self.assertEqual((self.lsr.link, self.lsr.html_class_parsing, self.lsr.name),
                         (str('https://ru.investing.com/equities/lsr-group_rts'), dict({'class': 'text-2xl'}),
                          str('ЛСР ➡ ')))


class TestStocksUsa(unittest.TestCase):
    def setUp(self):
        self.alibaba = stocksUsa('https://ru.investing.com/equities/alibaba', html_class_parsing={'class': 'text-2xl'},
                                 name='Alibaba ➡ ')
        self.amazon = stocksUsa('https://ru.investing.com/equities/amazon-com-inc',
                                html_class_parsing={'class': 'text-2xl'},
                                name='Amazon ➡ ')
        self.apple = stocksUsa('https://ru.investing.com/equities/apple-computer-inc',
                               html_class_parsing={'class': 'text-2xl'},
                               name='Apple ➡')
        self.exxon_mobil = stocksUsa('https://ru.investing.com/equities/exxon-mobil',
                                     html_class_parsing={'class': 'text-2xl'},
                                     name='Exxon Mobil ➡ ')
        self.netflix = stocksUsa('https://ru.investing.com/equities/netflix,-inc.',
                                 html_class_parsing={'class': 'text-2xl'},
                                 name='Netflix ➡ ')
        self.meta = stocksUsa('https://ru.investing.com/equities/facebook-inc',
                              html_class_parsing={'class': 'text-2xl'},
                              name='Meta Platforms ➡ ')
        self.nvidia = stocksUsa('https://ru.investing.com/equities/nvidia-corp',
                                html_class_parsing={'class': 'text-2xl'},
                                name='NVIDIA ➡ ')
        self.gm = stocksUsa('https://ru.investing.com/equities/general-electric',
                            html_class_parsing={'class': 'text-2xl'},
                            name='General Electric ➡ ')
        self.alphabet = stocksUsa('https://ru.investing.com/equities/google-inc',
                                  html_class_parsing={'class': 'text-2xl'},
                                  name='Alpabet A(Google) ➡ ')
        self.jpmorgan = stocksUsa('https://ru.investing.com/equities/jp-morgan-chase',
                                  html_class_parsing={'class': 'text-2xl'},
                                  name='JPMorgan Chase & Co ➡ ')
        self.microsoft = stocksUsa('https://ru.investing.com/equities/microsoft-corp',
                                   html_class_parsing={'class': 'text-2xl'},
                                   name='Microsoft ➡ ')
        self.tesla = stocksUsa('https://ru.investing.com/equities/tesla-motors',
                               html_class_parsing={'class': 'text-2xl'},
                               name='Tesla ➡ ')
        self.walmart = stocksUsa('https://ru.investing.com/equities/wal-mart-stores',
                                 html_class_parsing={'class': 'text-2xl'},
                                 name='Walmart ➡ ')
        self.palantir = stocksUsa('https://ru.investing.com/equities/palantir-technologies-inc',
                                  html_class_parsing={'class': 'text-2xl'},
                                  name='Palantir ➡ ')

    def test_init(self):
        self.assertEqual((self.alibaba.link, self.alibaba.html_class_parsing, self.alibaba.name),
                         (str('https://ru.investing.com/equities/alibaba'), dict({'class': 'text-2xl'}),
                          str('Alibaba ➡ ')))
        self.assertEqual((self.amazon.link, self.amazon.html_class_parsing, self.amazon.name),
                         (str('https://ru.investing.com/equities/amazon-com-inc'), dict({'class': 'text-2xl'}),
                          str('Amazon ➡ ')))
        self.assertEqual((self.apple.link, self.apple.html_class_parsing, self.apple.name),
                         (str('https://ru.investing.com/equities/apple-computer-inc'), dict({'class': 'text-2xl'}),
                          str('Apple ➡')))
        self.assertEqual((self.exxon_mobil.link, self.exxon_mobil.html_class_parsing, self.exxon_mobil.name),
                         (str('https://ru.investing.com/equities/exxon-mobil'), dict({'class': 'text-2xl'}),
                          str('Exxon Mobil ➡ ')))
        self.assertEqual((self.netflix.link, self.netflix.html_class_parsing, self.netflix.name),
                         (str('https://ru.investing.com/equities/netflix,-inc.'), dict({'class': 'text-2xl'}),
                          str('Netflix ➡ ')))
        self.assertEqual((self.meta.link, self.meta.html_class_parsing, self.meta.name),
                         (str('https://ru.investing.com/equities/facebook-inc'), dict({'class': 'text-2xl'}),
                          str('Meta Platforms ➡ ')))
        self.assertEqual((self.nvidia.link, self.nvidia.html_class_parsing, self.nvidia.name),
                         (str('https://ru.investing.com/equities/nvidia-corp'), dict({'class': 'text-2xl'}),
                          str('NVIDIA ➡ ')))
        self.assertEqual((self.gm.link, self.gm.html_class_parsing, self.gm.name),
                         (str('https://ru.investing.com/equities/general-electric'), dict({'class': 'text-2xl'}),
                          str('General Electric ➡ ')))
        self.assertEqual((self.alphabet.link, self.alphabet.html_class_parsing, self.alphabet.name),
                         (str('https://ru.investing.com/equities/google-inc'), dict({'class': 'text-2xl'}),
                          str('Alpabet A(Google) ➡ ')))
        self.assertEqual((self.jpmorgan.link, self.jpmorgan.html_class_parsing, self.jpmorgan.name),
                         (str('https://ru.investing.com/equities/jp-morgan-chase'), dict({'class': 'text-2xl'}),
                          str('JPMorgan Chase & Co ➡ ')))
        self.assertEqual((self.microsoft.link, self.microsoft.html_class_parsing, self.microsoft.name),
                         (str('https://ru.investing.com/equities/microsoft-corp'), dict({'class': 'text-2xl'}),
                          str('Microsoft ➡ ')))
        self.assertEqual((self.tesla.link, self.tesla.html_class_parsing, self.tesla.name),
                         (str('https://ru.investing.com/equities/tesla-motors'), dict({'class': 'text-2xl'}),
                          str('Tesla ➡ ')))
        self.assertEqual((self.walmart.link, self.walmart.html_class_parsing, self.walmart.name),
                         (str('https://ru.investing.com/equities/wal-mart-stores'), dict({'class': 'text-2xl'}),
                          str('Walmart ➡ ')))
        self.assertEqual((self.palantir.link, self.palantir.html_class_parsing, self.palantir.name),
                         (str('https://ru.investing.com/equities/palantir-technologies-inc'),
                          dict({'class': 'text-2xl'}), str('Palantir ➡ ')))


if __name__ == '__main__':
    unittest.main()
