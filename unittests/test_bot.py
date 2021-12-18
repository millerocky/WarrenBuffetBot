from unittest import TestCase, main
from WarrenBuffetBot.currency.currency import show_USD_RUB, show_EUR_RUB, dollar_rub, show_ticker_usd, ticker_usd, \
    show_ticker_euro, ticker_euro, euro_rub
from WarrenBuffetBot.stocksRU.finance_sector_RU.stocks_finance_sector import show_vtb, show_tinkoff, show_mkb, \
    show_sber, show_sber_prevs, show_afk, show_spb_bank, show_vtb_name, vtb_name, vtb_rub, \
    show_tinkoff_bank_name, tinkoff_bank_name, tinkoff_bank_rub, show_mkb_name, mkb_name, mkb_rub, show_sber_name, sber_name, sber_rub, show_sber_prevs_name, sber_prevs_name, sber_prevs_rub, \
    show_afk_name, afk_name, afk_rub, show_spb_bank_name, spb_bank_name, spb_bank_rub
from WarrenBuffetBot.stocksRU.IT_sector_RU.stocks_IT_sector import show_headhunter, show_yandex, show_mailru, show_mts, \
    show_ozon, show_qiwi, show_rosseti, show_rostelecom, show_hhru_name, hhru_name, hhru_rub, show_yandex_name, \
    yandex_name, yandex_rub, show_mailru_name, mailru_name, mailru_rub, show_mts_name, mts_name, mts_rub, \
    show_ozon_name, ozon_name, ozon_rub, show_qiwi_name, qiwi_name, qiwi_rub, show_rosseti_name, rosseti_name, \
    rosseti_rub, show_rostelecom_name, rostelecom_name, rostelecom_rub
from WarrenBuffetBot.stocksRU.basic_sector_RU.stocks_basic_sector import show_magnit, show_x5group, show_detskiy_mir, \
    show_fix_price, show_mvideo, show_cherkizovo, magnit_name, show_magnit_name, magnit_rub, show_x5group_name, \
    x5group_rub, show_detskiy_mir_name, detskiy_mir_name, detskiy_mir_rub, show_fix_price_name, fix_price_name, \
    fix_price_rub, show_mvideo_name, mvideo_name, mvideo_rub, show_cherkizovo_name, cherkizovo_name, cherkizovo_rub, \
    x5group_name
from WarrenBuffetBot.stocksRU.industrial_sector.stocks_industrial_sector import show_globaltrans, show_petropavlovsk, \
    show_polymetal, show_alrosa, show_aeroflot, \
    show_gazprom, show_inter_rao, show_lukoil, show_mmk, show_nlmk, show_novatek, show_nornikel, show_polyus, \
    show_rosneft, show_rusal, show_rushydro, show_severstal, show_surgutneft, show_tatneft, show_transneft, \
    show_phosagro, show_fsk, show_globaltrans_name, globaltrans_name, globaltrans_rub, show_petropavlovsk_name, \
    petropavlovsk_name, petropavlovsk_rub, show_polymetal_name, polymetal_name, polymetal_rub, show_alrosa_name, \
    alrosa_name, alrosa_rub, show_aeroflot_name, aeroflot_name, aeroflot_rub, show_gazprom_name, gazprom_name, \
    gazprom_rub, show_inter_rao_name, inter_rao_name, inter_rao_rub, show_lukoil_name, lukoil_name, lukoil_rub, \
    show_mmk_name, mmk_name, mmk_rub, show_nlmk_name, nlmk_name, nlmk_rub, show_novatek_name, novatek_name, novatek_rub, \
    show_nornikel_name, nornikel_name, nornikel_rub, show_polyus_name, polyus_name, polyus_rub, show_rosneft_name, \
    rosneft_name, rosneft_rub, show_rusal_name, rusal_name, rusal_rub, show_rushydro_name, rushydro_name, rushydro_rub, \
    show_severstal_name, severstal_name, severstal_rub, show_surgutneft_name, surgutneft_name, surgutneft_rub, \
    show_tatneft_name, tatneft_name, tatneft_rub, show_transneft_name, transneft_name, transneft_rub, \
    show_phosagro_name, phosagro_name, phosagro_rub, show_fsk_name, fsk_name, fsk_rub

from WarrenBuffetBot.stocksRU.medicine_sector_RU.medicine_sectorRU import show_life, show_iskj, show_mdmg, show_gemc, \
    show_life_name, life_name, life_rub, show_iskj_name, iskj_name, iskj_rub, show_mdmg_name, mdmg_name, mdmg_rub, \
    show_gemc_name, gemc_name, gemc_rub
from WarrenBuffetBot.stocksRU.realEstate_RU.realEstate_sector import show_pik, show_lsr, show_pik_name, pik_name, \
    pik_rub, show_lsr_name, lsr_name, lsr_rub
from WarrenBuffetBot.stocks_China.stock_China import show_li, show_baidu, show_jd, show_bilibili, show_tencent, \
    show_nio, show_xpeng, show_li_name, li_auto_name, li_auto_usd, show_baidu_name, baidu_name, baidu_usd, show_JD_name, \
    JD_name, JD_usd, show_bilibili_name, bilibili_name, bilibili_usd, show_tencent_name, tencent_name, tencent_usd, \
    show_nio_name, nio_name, nio_usd, show_xpeng_name, xpeng_name, xpeng_usd
from WarrenBuffetBot.cryptocurrencies.crypto import show_bitcoin, show_ethereum, show_litecoin, \
    show_cardano, show_xrp, show_doge, show_bnb, show_tether, show_solana, show_terra, show_uniswap, show_dot, \
    show_avalanche, show_chainlink, show_tron, show_shiba, show_bitcoin_name, bitcoin_name, bitcoin_usd, \
    show_ethereum_name, ethereum_name, ethereum_usd, show_litecoin_name, litecoin_name, litecoin_usd, show_cardano_name, \
    cardano_name, cardano_usd, show_xrp_name, xrp_name, xrp_usd, show_doge_name, doge_name, doge_usd, show_bnb_name, \
    bnb_name, bnb_usd, show_tether_name, tether_name, tether_usd, show_solana_name, solana_name, solana_usd, \
    show_terra_name, terra_name, terra_usd, show_uniswap_name, uniswap_name, uniswap_usd, show_polkadot_name, \
    polkadot_name, polkadot_usd, show_avalanche_name, avalanche_name, avalanche_usd, show_chainlink_name, \
    chainlink_name, chainlink_usd, show_tron_name, tron_name, tron_usd, show_shiba_name, shiba_name, shiba_usd
from WarrenBuffetBot.stocksUSA.stocks_USA import show_alibaba, show_amazon, show_apple, \
    show_exxonmobil, show_netflix, show_metaplatforms, show_nvidia, show_ge, show_google, show_jp, show_microsoft, \
    show_tesla, show_walmart, show_palantir, show_stock_USA_1_name, stock_USA_1_name, stock_USA_1_dollar, \
    show_stock_USA_2_name, stock_USA_2_name, stock_USA_2_dollar, show_stock_USA_3_name, stock_USA_3_name, \
    stock_USA_3_dollar, show_stock_USA_4_name, stock_USA_4_name, stock_USA_4_dollar, show_stock_USA_5_name, \
    stock_USA_5_name, stock_USA_5_dollar, show_stock_USA_6_name, stock_USA_6_name, stock_USA_6_dollar, \
    show_stock_USA_7_name, stock_USA_7_name, stock_USA_7_dollar, show_stock_USA_8_name, stock_USA_8_name, \
    stock_USA_8_dollar, show_stock_USA_9_name, stock_USA_9_name, stock_USA_9_dollar, show_stock_USA_10_name, \
    stock_USA_10_name, stock_USA_10_dollar, show_stock_USA_11_name, stock_USA_11_name, stock_USA_11_dollar, \
    show_stock_USA_12_name, stock_USA_12_name, stock_USA_12_dollar, show_stock_USA_13_name, stock_USA_13_name, \
    stock_USA_13_dollar, show_stock_USA_14_name, stock_USA_14_name, stock_USA_14_dollar
from WarrenBuffetBot.world_indexes.world_indexes import show_MOEX, show_snp500, show_nasdaq, show_shanghai, \
    MOEX_index_name, MOEX_index_rub, show_SnP500_name, SnP500_index_name, SnP500_index, show_NASDAQ_name, \
    NASDAQ_index_name, NASDAQ_index, show_SHANGAI_name, SHANGAI_index_name, SHANGAI_index, show_MOEX_name


class TestShowStocks(TestCase):

    def test_cryptocurrencies(self):
        '''
        :return: Тестирование работыvфункций по выводу тикеров-названий
        '''
        self.assertRegex(bitcoin_usd, '\d+(\,|\.)\d*USD')
        self.assertRegex(ethereum_usd, '\d+\,\d*USD')
        self.assertRegex(litecoin_usd, '\d+\,\d*USD')
        self.assertRegex(cardano_usd, '\d+\,\d*USD')
        self.assertRegex(xrp_usd, '\d+\,\d*USD')
        self.assertRegex(doge_usd, '\d+\,\d*USD')
        self.assertRegex(bnb_usd, '\d+\,\d*USD')
        self.assertRegex(tether_usd, '\d+\,\d*USD')
        self.assertRegex(solana_usd, '\d+\,\d*USD')
        self.assertRegex(terra_usd, '\d+\,\d*USD')
        self.assertRegex(uniswap_usd, '\d+\,\d*USD')
        self.assertRegex(polkadot_usd, '\d+\,\d*USD')
        self.assertRegex(avalanche_usd, '\d+\,\d*USD')
        self.assertRegex(chainlink_usd, '\d+\,\d*USD')
        self.assertRegex(tron_usd, '\d+\,\d*USD')
        self.assertRegex(shiba_usd, '\d+\,\d*USD')

    def test_currency(self):
        self.assertRegex(dollar_rub, '\d+\,\d*RUB')
        self.assertRegex(euro_rub, '\d+\,\d*RUB')

    def test_stocksRU(self):
        self.assertRegex(magnit_rub, '\d+\,\d*RUB')
        self.assertRegex(x5group_rub, '\d+\,\d*RUB')
        self.assertRegex(detskiy_mir_rub, '\d+\,\d*RUB')
        self.assertRegex(fix_price_rub, '\d+\,\d*RUB')
        self.assertRegex(mvideo_rub, '\d+\,\d*RUB')
        self.assertRegex(cherkizovo_rub, '\d+\,\d*RUB')
        self.assertRegex(hhru_rub, '\d+\,\d*RUB')
        self.assertRegex(yandex_rub, '\d+\,\d*RUB')
        self.assertRegex(mailru_rub, '\d+\,\d*RUB')
        self.assertRegex(mts_rub, '\d+\,\d*RUB')
        self.assertRegex(ozon_rub, '\d+\,\d*RUB')
        self.assertRegex(qiwi_rub, '\d+\,\d*RUB')
        self.assertRegex(rosseti_rub, '\d+\,\d*RUB')
        self.assertRegex(rostelecom_rub, '\d+\,\d*RUB')
        self.assertRegex(vtb_rub, '\d+\,\d*RUB')
        self.assertRegex(tinkoff_bank_rub, '\d+\,\d*RUB')
        self.assertRegex(mkb_rub, '\d+\,\d*RUB')
        self.assertRegex(sber_rub, '\d+\,\d*RUB')
        self.assertRegex(sber_prevs_rub, '\d+\,\d*RUB')
        self.assertRegex(afk_rub, '\d+\,\d*RUB')
        self.assertRegex(spb_bank_rub, '\d+\,\d*RUB')
        self.assertRegex(globaltrans_rub, '\d+\,\d*RUB')
        self.assertRegex(petropavlovsk_rub, '\d+\,\d*RUB')
        self.assertRegex(polymetal_rub, '\d+\,\d*RUB')
        self.assertRegex(alrosa_rub, '\d+\,\d*RUB')
        self.assertRegex(aeroflot_rub, '\d+\,\d*RUB')
        self.assertRegex(gazprom_rub, '\d+\,\d*RUB')
        self.assertRegex(inter_rao_rub, '\d+\,\d*RUB')
        self.assertRegex(lukoil_rub, '\d+\,\d*RUB')
        self.assertRegex(mmk_rub, '\d+\,\d*RUB')
        self.assertRegex(nlmk_rub, '\d+\,\d*RUB')
        self.assertRegex(novatek_rub, '\d+\,\d*RUB')
        self.assertRegex(nornikel_rub, '\d+\,\d*RUB')
        self.assertRegex(polyus_rub, '\d+\,\d*RUB')
        self.assertRegex(rosneft_rub, '\d+\,\d*RUB')
        self.assertRegex(rusal_rub, '\d+\,\d*RUB')
        self.assertRegex(rushydro_rub, '\d+\,\d*RUB')
        self.assertRegex(severstal_rub, '\d+\,\d*RUB')
        self.assertRegex(surgutneft_rub, '\d+\,\d*RUB')
        self.assertRegex(tatneft_rub, '\d+\,\d*RUB')
        self.assertRegex(transneft_rub, '\d+(\,|\.)\d*RUB')
        self.assertRegex(phosagro_rub, '\d+\,\d*RUB')
        self.assertRegex(fsk_rub, '\d+\,\d*RUB')
        self.assertRegex(pik_rub, '\d+\,\d*RUB')
        self.assertRegex(lsr_rub, '\d+\,\d*RUB')
        self.assertRegex(life_rub, '\d+\,\d*RUB')
        self.assertRegex(iskj_rub, '\d+\,\d*RUB')
        self.assertRegex(mdmg_rub, '\d+\,\d*RUB')
        self.assertRegex(gemc_rub, '\d+\,\d*RUB')

    def test_stocksUSA(self):
        self.assertRegex(stock_USA_1_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_2_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_3_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_4_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_5_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_6_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_7_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_8_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_9_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_10_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_11_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_12_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_13_dollar, '\d+\,\d*USD')
        self.assertRegex(stock_USA_14_dollar, '\d+\,\d*USD')

    def test_stocksChina(self):
        self.assertRegex(li_auto_usd, '\d+\,\d*USD')
        self.assertRegex(baidu_usd, '\d+\,\d*USD')
        self.assertRegex(JD_usd, '\d+\,\d*USD')
        self.assertRegex(bilibili_usd, '\d+\,\d*USD')
        self.assertRegex(tencent_usd, '\d+\,\d*USD')
        self.assertRegex(nio_usd, '\d+\,\d*USD')
        self.assertRegex(xpeng_usd, '\d+\,\d*USD')

    def test_indexies(self):
        self.assertRegex(MOEX_index_rub, '\d+\,\d*RUB')
        self.assertRegex(SnP500_index, '\d+\,\d*USD')
        self.assertRegex(NASDAQ_index, '\d+\,\d*USD')
        self.assertRegex(SHANGAI_index, '\d+\,\d*USD')

    def test_values(self):
        '''
        :return: Тестирование работы всех функций по выводу названий интсрументов и их котировок
        '''
        self.assertEqual(show_ticker_usd(), ticker_usd)
        self.assertEqual(show_USD_RUB(), dollar_rub)
        self.assertEqual(show_ticker_euro(), ticker_euro)
        self.assertEqual(show_EUR_RUB(), euro_rub)
        self.assertEqual(show_magnit_name(), magnit_name)
        self.assertEqual(show_magnit(), magnit_rub)
        self.assertEqual(show_x5group_name(), x5group_name)
        self.assertEqual(show_x5group(), x5group_rub)
        self.assertEqual(show_detskiy_mir_name(), detskiy_mir_name)
        self.assertEqual(show_detskiy_mir(), detskiy_mir_rub)
        self.assertEqual(show_fix_price_name(), fix_price_name)
        self.assertEqual(show_fix_price(), fix_price_rub)
        self.assertEqual(show_mvideo_name(), mvideo_name)
        self.assertEqual(show_mvideo(), mvideo_rub)
        self.assertEqual(show_cherkizovo_name(), cherkizovo_name)
        self.assertEqual(show_cherkizovo(), cherkizovo_rub)
        self.assertEqual(show_hhru_name(), hhru_name)
        self.assertEqual(show_headhunter(), hhru_rub)
        self.assertEqual(show_yandex_name(), yandex_name)
        self.assertEqual(show_yandex(), yandex_rub)
        self.assertEqual(show_mailru_name(), mailru_name)
        self.assertEqual(show_mailru(), mailru_rub)
        self.assertEqual(show_mts_name(), mts_name)
        self.assertEqual(show_mts(), mts_rub)
        self.assertEqual(show_ozon_name(), ozon_name)
        self.assertEqual(show_ozon(), ozon_rub)
        self.assertEqual(show_qiwi_name(), qiwi_name)
        self.assertEqual(show_qiwi(), qiwi_rub)
        self.assertEqual(show_rosseti_name(), rosseti_name)
        self.assertEqual(show_rosseti(), rosseti_rub)
        self.assertEqual(show_rostelecom_name(), rostelecom_name)
        self.assertEqual(show_rostelecom(), rostelecom_rub)
        self.assertEqual(show_vtb_name(), vtb_name)
        self.assertEqual(show_vtb(), vtb_rub)
        self.assertEqual(show_tinkoff_bank_name(), tinkoff_bank_name)
        self.assertEqual(show_tinkoff(), tinkoff_bank_rub)
        self.assertEqual(show_mkb_name(), mkb_name)
        self.assertEqual(show_mkb(), mkb_rub)
        self.assertEqual(show_sber_name(), sber_name)
        self.assertEqual(show_sber(), sber_rub)
        self.assertEqual(show_sber_prevs_name(), sber_prevs_name)
        self.assertEqual(show_sber_prevs(), sber_prevs_rub)
        self.assertEqual(show_afk_name(), afk_name)
        self.assertEqual(show_afk(), afk_rub)
        self.assertEqual(show_spb_bank_name(), spb_bank_name)
        self.assertEqual(show_spb_bank(), spb_bank_rub)
        self.assertEqual(show_globaltrans_name(), globaltrans_name)
        self.assertEqual(show_globaltrans(), globaltrans_rub)
        self.assertEqual(show_petropavlovsk_name(), petropavlovsk_name)
        self.assertEqual(show_petropavlovsk(), petropavlovsk_rub)
        self.assertEqual(show_polymetal_name(), polymetal_name)
        self.assertEqual(show_polymetal(), polymetal_rub)
        self.assertEqual(show_alrosa_name(), alrosa_name)
        self.assertEqual(show_alrosa(), alrosa_rub)
        self.assertEqual(show_aeroflot_name(), aeroflot_name)
        self.assertEqual(show_aeroflot(), aeroflot_rub)
        self.assertEqual(show_gazprom_name(), gazprom_name)
        self.assertEqual(show_gazprom(), gazprom_rub)
        self.assertEqual(show_inter_rao_name(), inter_rao_name)
        self.assertEqual(show_inter_rao(), inter_rao_rub)
        self.assertEqual(show_lukoil_name(), lukoil_name)
        self.assertEqual(show_lukoil(), lukoil_rub)
        self.assertEqual(show_mmk_name(), mmk_name)
        self.assertEqual(show_mmk(), mmk_rub)
        self.assertEqual(show_nlmk_name(), nlmk_name)
        self.assertEqual(show_nlmk(), nlmk_rub)
        self.assertEqual(show_novatek_name(), novatek_name)
        self.assertEqual(show_novatek(), novatek_rub)
        self.assertEqual(show_nornikel_name(), nornikel_name)
        self.assertEqual(show_nornikel(), nornikel_rub)
        self.assertEqual(show_polyus_name(), polyus_name)
        self.assertEqual(show_polyus(), polyus_rub)
        self.assertEqual(show_rosneft_name(), rosneft_name)
        self.assertEqual(show_rosneft(), rosneft_rub)
        self.assertEqual(show_rusal_name(), rusal_name)
        self.assertEqual(show_rusal(), rusal_rub)
        self.assertEqual(show_rushydro_name(), rushydro_name)
        self.assertEqual(show_rushydro(), rushydro_rub)
        self.assertEqual(show_severstal_name(), severstal_name)
        self.assertEqual(show_severstal(), severstal_rub)
        self.assertEqual(show_surgutneft_name(), surgutneft_name)
        self.assertEqual(show_surgutneft(), surgutneft_rub)
        self.assertEqual(show_tatneft_name(), tatneft_name)
        self.assertEqual(show_tatneft(), tatneft_rub)
        self.assertEqual(show_transneft_name(), transneft_name)
        self.assertEqual(show_transneft(), transneft_rub)
        self.assertEqual(show_phosagro_name(), phosagro_name)
        self.assertEqual(show_phosagro(), phosagro_rub)
        self.assertEqual(show_fsk_name(), fsk_name)
        self.assertEqual(show_fsk(), fsk_rub)
        self.assertEqual(show_pik_name(), pik_name)
        self.assertEqual(show_pik(), pik_rub)
        self.assertEqual(show_lsr_name(), lsr_name)
        self.assertEqual(show_lsr(), lsr_rub)
        self.assertEqual(show_life_name(), life_name)
        self.assertEqual(show_life(), life_rub)
        self.assertEqual(show_iskj_name(), iskj_name)
        self.assertEqual(show_iskj(), iskj_rub)
        self.assertEqual(show_mdmg_name(), mdmg_name)
        self.assertEqual(show_mdmg(), mdmg_rub)
        self.assertEqual(show_gemc_name(), gemc_name)
        self.assertEqual(show_gemc(), gemc_rub)
        self.assertEqual(show_stock_USA_1_name(), stock_USA_1_name)
        self.assertEqual(show_alibaba(), stock_USA_1_dollar)
        self.assertEqual(show_stock_USA_2_name(), stock_USA_2_name)
        self.assertEqual(show_amazon(), stock_USA_2_dollar)
        self.assertEqual(show_stock_USA_3_name(), stock_USA_3_name)
        self.assertEqual(show_apple(), stock_USA_3_dollar)
        self.assertEqual(show_stock_USA_4_name(), stock_USA_4_name)
        self.assertEqual(show_exxonmobil(), stock_USA_4_dollar)
        self.assertEqual(show_stock_USA_5_name(), stock_USA_5_name)
        self.assertEqual(show_netflix(), stock_USA_5_dollar)
        self.assertEqual(show_stock_USA_6_name(), stock_USA_6_name)
        self.assertEqual(show_metaplatforms(), stock_USA_6_dollar)
        self.assertEqual(show_stock_USA_7_name(), stock_USA_7_name)
        self.assertEqual(show_nvidia(), stock_USA_7_dollar)
        self.assertEqual(show_stock_USA_8_name(), stock_USA_8_name)
        self.assertEqual(show_ge(), stock_USA_8_dollar)
        self.assertEqual(show_stock_USA_9_name(), stock_USA_9_name)
        self.assertEqual(show_google(), stock_USA_9_dollar)
        self.assertEqual(show_stock_USA_10_name(), stock_USA_10_name)
        self.assertEqual(show_jp(), stock_USA_10_dollar)
        self.assertEqual(show_stock_USA_11_name(), stock_USA_11_name)
        self.assertEqual(show_microsoft(), stock_USA_11_dollar)
        self.assertEqual(show_stock_USA_12_name(), stock_USA_12_name)
        self.assertEqual(show_tesla(), stock_USA_12_dollar)
        self.assertEqual(show_stock_USA_13_name(), stock_USA_13_name)
        self.assertEqual(show_walmart(), stock_USA_13_dollar)
        self.assertEqual(show_stock_USA_14_name(), stock_USA_14_name)
        self.assertEqual(show_palantir(), stock_USA_14_dollar)
        self.assertEqual(show_li_name(), li_auto_name)
        self.assertEqual(show_li(), li_auto_usd)
        self.assertEqual(show_baidu_name(), baidu_name)
        self.assertEqual(show_baidu(), baidu_usd)
        self.assertEqual(show_JD_name(), JD_name)
        self.assertEqual(show_jd(), JD_usd)
        self.assertEqual(show_bilibili_name(), bilibili_name)
        self.assertEqual(show_bilibili(), bilibili_usd)
        self.assertEqual(show_tencent_name(), tencent_name)
        self.assertEqual(show_tencent(), tencent_usd)
        self.assertEqual(show_nio_name(), nio_name)
        self.assertEqual(show_nio(), nio_usd)
        self.assertEqual(show_xpeng_name(), xpeng_name)
        self.assertEqual(show_xpeng(), xpeng_usd)
        self.assertEqual(show_MOEX_name(), MOEX_index_name)
        self.assertEqual(show_MOEX(), MOEX_index_rub)
        self.assertEqual(show_SnP500_name(), SnP500_index_name)
        self.assertEqual(show_snp500(), SnP500_index)
        self.assertEqual(show_NASDAQ_name(), NASDAQ_index_name)
        self.assertEqual(show_nasdaq(), NASDAQ_index)
        self.assertEqual(show_SHANGAI_name(), SHANGAI_index_name)
        self.assertEqual(show_shanghai(), SHANGAI_index)
        self.assertEqual(show_bitcoin_name(), bitcoin_name)
        self.assertEqual(show_bitcoin(), bitcoin_usd)
        self.assertEqual(show_ethereum_name(), ethereum_name)
        self.assertEqual(show_ethereum(), ethereum_usd)
        self.assertEqual(show_litecoin_name(), litecoin_name)
        self.assertEqual(show_litecoin(), litecoin_usd)
        self.assertEqual(show_cardano_name(), cardano_name)
        self.assertEqual(show_cardano(), cardano_usd)
        self.assertEqual(show_xrp_name(), xrp_name)
        self.assertEqual(show_xrp(), xrp_usd)
        self.assertEqual(show_doge_name(), doge_name)
        self.assertEqual(show_doge(), doge_usd)
        self.assertEqual(show_bnb_name(), bnb_name)
        self.assertEqual(show_bnb(), bnb_usd)
        self.assertEqual(show_tether_name(), tether_name)
        self.assertEqual(show_tether(), tether_usd)
        self.assertEqual(show_solana_name(), solana_name)
        self.assertEqual(show_solana(), solana_usd)
        self.assertEqual(show_terra_name(), terra_name)
        self.assertEqual(show_terra(), terra_usd)
        self.assertEqual(show_uniswap_name(), uniswap_name)
        self.assertEqual(show_uniswap(), uniswap_usd)
        self.assertEqual(show_polkadot_name(), polkadot_name)
        self.assertEqual(show_dot(), polkadot_usd)
        self.assertEqual(show_avalanche_name(), avalanche_name)
        self.assertEqual(show_avalanche(), avalanche_usd)
        self.assertEqual(show_chainlink_name(), chainlink_name)
        self.assertEqual(show_chainlink(), chainlink_usd)
        self.assertEqual(show_tron_name(), tron_name)
        self.assertEqual(show_tron(), tron_usd)
        self.assertEqual(show_shiba_name(), shiba_name)
        self.assertEqual(show_shiba(), shiba_usd)


if __name__ == '__main__':
    main()