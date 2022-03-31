# Подключаю библиотеку aiogram для создания телеграм-бота
from aiogram import types, Bot, Dispatcher, executor
import config

# Подключаю функции по показу котировок российских акций финансового сектора из моего модуля, где происходит основной парсинг

# Подключаю функции по показу котировок с названиями криптовалют и их котировками из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.cryptocurrencies.crypto import bitcoin, ethereum, litecoin, cardano, xrp, doge, bnb, tether, \
    solana, luna, uniswap, polkadot, avalanche, chainlink, tron, shiba
# Подключаю функции по показу котировок валютных пар к рублю
from WarrenBuffetBot.currency.currency import usd_rub, euro_rub

from WarrenBuffetBot.stocksRU.finance_sector_RU.stocks_finance_sector import show_vtb, show_tinkoff, show_mkb, \
    show_sber, show_sber_prevs, show_afk, show_spb_bank, show_vtb_name, show_tinkoff_bank_name, \
    show_mkb_name, show_sber_name, show_sber_prevs_name, show_afk_name, show_spb_bank_name

# Подключаю функции по показу котировок российских акций IT-сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.IT_sector_RU.stocks_IT_sector import show_headhunter, show_yandex, \
    show_mailru, show_mts, show_ozon, show_qiwi, show_rosseti, show_rostelecom, show_hhru_name, show_yandex_name, \
    show_mailru_name, show_mts_name, show_ozon_name, show_qiwi_name, show_rosseti_name, show_rostelecom_name

# Подключаю функции по показу котировок российских акций потребительского сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.basic_sector_RU.stocks_basic_sector import show_magnit, show_x5group, show_detskiy_mir, \
    show_fix_price, show_mvideo, show_cherkizovo, show_magnit_name, show_x5group_name, show_detskiy_mir_name, \
    show_fix_price_name, show_mvideo_name, show_cherkizovo_name

# Подключаю функции по показу котировок российскиз акций промышленного сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.industrial_sector.stocks_industrial_sector import show_globaltrans, show_petropavlovsk, \
    show_polymetal, show_alrosa, show_aeroflot, \
    show_gazprom, show_inter_rao, show_lukoil, show_mmk, show_nlmk, show_novatek, show_nornikel, show_polyus, \
    show_rosneft, show_rusal, show_rushydro, show_severstal, show_surgutneft, show_tatneft, show_transneft, \
    show_phosagro, show_fsk, show_globaltrans_name, show_petropavlovsk_name, show_polymetal_name, show_alrosa_name, \
    show_aeroflot_name, show_gazprom_name, show_inter_rao_name, show_lukoil_name, show_mmk_name, show_nlmk_name, \
    show_novatek_name, show_nornikel_name, show_polyus_name, show_rosneft_name, show_rusal_name, show_rushydro_name, \
    show_severstal_name, show_surgutneft_name, show_tatneft_name, show_transneft_name, show_phosagro_name, show_fsk_name

# Подключаю функции по показу котировок российских акций из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.medicine_sector_RU.medicine_sectorRU import show_life, show_iskj, show_mdmg, show_gemc, \
    show_life_name, show_iskj_name, show_mdmg_name, show_gemc_name

# Подключаю функции по показу котировок китайских акций из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.realEstate_RU.realEstate_sector import show_pik, show_lsr, show_pik_name, show_lsr_name
from WarrenBuffetBot.stocks_China.stock_China import show_li, show_baidu, show_jd, show_bilibili, show_tencent, \
    show_nio, show_xpeng, show_li_name, show_baidu_name, show_JD_name, show_bilibili_name, show_tencent_name, \
    show_nio_name, show_xpeng_name

# Подключаю функции по показу котировок американских акций из моего модуля, где происходит основной парсинг
from stocksUSA.stocks_USA import show_alibaba, show_amazon, show_apple, \
    show_exxonmobil, show_netflix, show_metaplatforms, show_nvidia, show_ge, show_google, show_jp, show_microsoft, \
    show_tesla, show_walmart, show_palantir, show_stock_USA_1_name, show_stock_USA_2_name, show_stock_USA_3_name, \
    show_stock_USA_4_name, show_stock_USA_5_name, show_stock_USA_6_name, show_stock_USA_7_name, show_stock_USA_8_name, \
    show_stock_USA_9_name, show_stock_USA_10_name, show_stock_USA_11_name, show_stock_USA_12_name, \
    show_stock_USA_13_name, show_stock_USA_14_name

# Подключаю функции по показу котировок мировых индексов из моего модуля, где происходит основной парсинг
from world_indexes.world_indexes import show_MOEX, show_snp500, show_nasdaq, show_shanghai, show_SnP500_name, \
    show_NASDAQ_name, show_SHANGAI_name, show_MOEX_name

# Создаю бота, используя секретный токен(он находится в файле config, который дал нам @BotFather
bot = Bot(config.TOKEN)

# Создаю диспетчера, который отслеживает взаимодействие бота с пользователем
dp = Dispatcher(bot)


# Дескриптор(диспетчер отслеживает все стартовые нажатия на кнопки)
@dp.message_handler(commands=['start'])
async def bot_start(message: types.message):
    '''
    :param message:
    :return: Запуск меню бота
    '''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    currency_button = types.KeyboardButton('💰 Курс валют')
    stocks_button = types.KeyboardButton('💸 Курс акций')
    cryptocurrency_button = types.KeyboardButton('💎 Курс криптовалют')
    information_button = types.KeyboardButton('⚙️ Разработчик')
    markup.add(currency_button, stocks_button, cryptocurrency_button, information_button)
    await bot.send_message(message.chat.id, 'Уоррен Баффетт приветствует тебя в мире инвестиций, {0.first_name}'.format(
        message.from_user), reply_markup=markup)


# Декскриптор - обработчик данных от пользователя
@dp.message_handler(content_types=['text'])
async def process_menu(message: types.message):
    '''
    :param message:
    :return: Обработчик функционала меню
    '''
    if message.chat.type == 'private':

        if message.text == '💰 Курс валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back_button = types.KeyboardButton('◀️Назад')
            markup.add(back_button)
            await bot.send_message(message.chat.id, '🕑 Загружаю курсы валют\n 🟩Загрузка...', reply_markup=markup)
            await bot.send_message(message.chat.id,
                                   text='Доллар к рублю: ' + usd_rub.get_currency_value() + ' руб.' + '\n'
                                                                                                      'Евро к рублю: ' + euro_rub.get_currency_value() + ' руб.')

        if message.text == '◀️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            currency_button = types.KeyboardButton('💰 Курс валют')
            stocks_button = types.KeyboardButton('💸 Курс акций')
            cryptocurrency_button = types.KeyboardButton('💎 Курс криптовалют')
            information_button = types.KeyboardButton('⚙️ Разработчик')
            markup.add(currency_button, stocks_button, cryptocurrency_button, information_button)
            await bot.send_message(message.chat.id, '◀️Назад', reply_markup=markup)

        if message.text == '💸 Курс акций':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            rus_stocks = types.KeyboardButton('🇷🇺 Акции')
            usa_stocks = types.KeyboardButton('🇺🇸 Акции')
            china_stocks = types.KeyboardButton('🇨🇳 Акции')
            world_indexes = types.KeyboardButton('🌆 Мировые индексы')
            back_button = types.KeyboardButton('◀️Назад')
            markup.add(rus_stocks, usa_stocks, china_stocks, world_indexes, back_button)
            await bot.send_message(message.chat.id, '🕑Загрузка', reply_markup=markup)

        # if message.text == '🇷🇺 Акции':
        # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #  basic_sector_rus = types.KeyboardButton('🧃 Потребительский сектор 🇷🇺')
        # IT_sector_rus = types.KeyboardButton('📱 IT сектор 🇷🇺')
        # finance_sector_rus = types.KeyboardButton('🏦 Финансовый сектор 🇷🇺')
        # industrial_sector_rus = types.KeyboardButton('⛰ Промышленный сектор 🇷🇺')
        # realEstate_sector_rus = types.KeyboardButton('🏙 Недвижимость 🇷🇺')
        # medicine_sector_rus = types.KeyboardButton('💊 Медицина 🇷🇺')
        # back_button = types.KeyboardButton('◀️Назад')
        # markup.add(basic_sector_rus, IT_sector_rus, finance_sector_rus, industrial_sector_rus,
        #          realEstate_sector_rus, medicine_sector_rus, back_button)
        # await bot.send_message(message.chat.id, text='🕑Загрузка', reply_markup=markup)

        # if message.text == '🧃 Потребительский сектор 🇷🇺':
        #   await bot.send_message(message.chat.id, text=show_magnit_name() + show_magnit())
        # await bot.send_message(message.chat.id, text=show_x5group_name() + show_x5group())
        # await bot.send_message(message.chat.id, text=show_detskiy_mir_name() + show_detskiy_mir())
        # await bot.send_message(message.chat.id, text=show_fix_price_name() + show_fix_price())
        # await bot.send_message(message.chat.id, text=show_mvideo_name() + show_mvideo())
        # await bot.send_message(message.chat.id, text=show_cherkizovo_name() + show_cherkizovo())

        # if message.text == '📱 IT сектор 🇷🇺':
        # await bot.send_message(message.chat.id, text=show_hhru_name() + show_headhunter())
        # await bot.send_message(message.chat.id, text=show_yandex_name() + show_yandex())
        # await bot.send_message(message.chat.id, text=show_mailru_name() + show_mailru())
        # await bot.send_message(message.chat.id, text=show_mts_name() + show_mts())
        # await bot.send_message(message.chat.id, text=show_ozon_name() + show_ozon())
        # await bot.send_message(message.chat.id, text=show_qiwi_name() + show_qiwi())
        # await bot.send_message(message.chat.id, text=show_rosseti_name() + show_rosseti())
        # await bot.send_message(message.chat.id, text=show_rostelecom_name() + show_rostelecom())

        # if message.text == '🏦 Финансовый сектор 🇷🇺':
        #   await bot.send_message(message.chat.id, text=show_vtb_name() + show_vtb())
        # await bot.send_message(message.chat.id, text=show_tinkoff_bank_name() + show_tinkoff())
        # await bot.send_message(message.chat.id, text=show_mkb_name() + show_mkb())
        # await bot.send_message(message.chat.id, text=show_sber_name() + show_sber())
        # await bot.send_message(message.chat.id, text=show_sber_prevs_name() + show_sber_prevs())
        # await bot.send_message(message.chat.id, text=show_afk_name() + show_afk())
        # await bot.send_message(message.chat.id, text=show_spb_bank_name() + show_spb_bank())

        # if message.text == '⛰ Промышленный сектор 🇷🇺':
        # await bot.send_message(message.chat.id, text=show_globaltrans_name() + show_globaltrans())
        # await bot.send_message(message.chat.id, text=show_petropavlovsk_name() + show_petropavlovsk())
        # await bot.send_message(message.chat.id, text=show_polymetal_name() + show_polymetal())
        # await bot.send_message(message.chat.id, text=show_alrosa_name() + show_alrosa())
        # await bot.send_message(message.chat.id, text=show_aeroflot_name() + show_aeroflot())
        # await bot.send_message(message.chat.id, text=show_gazprom_name() + show_gazprom())
        # await bot.send_message(message.chat.id, text=show_inter_rao_name() + show_inter_rao())
        # await bot.send_message(message.chat.id, text=show_lukoil_name() + show_lukoil())
        # await bot.send_message(message.chat.id, text=show_mmk_name() + show_mmk())
        # await bot.send_message(message.chat.id, text=show_nlmk_name() + show_nlmk())
        # await bot.send_message(message.chat.id, text=show_novatek_name() + show_novatek())
        # await bot.send_message(message.chat.id, text=show_nornikel_name() + show_nornikel())
        # await bot.send_message(message.chat.id, text=show_polyus_name() + show_polyus())
        # await bot.send_message(message.chat.id, text=show_rosneft_name() + show_rosneft())
        # await bot.send_message(message.chat.id, text=show_rusal_name() + show_rusal())
        # await bot.send_message(message.chat.id, text=show_rushydro_name() + show_rushydro())
        # await bot.send_message(message.chat.id, text=show_severstal_name() + show_severstal())
        # await bot.send_message(message.chat.id, text=show_surgutneft_name() + show_surgutneft())
        # await bot.send_message(message.chat.id, text=show_tatneft_name() + show_tatneft())
        # await bot.send_message(message.chat.id, text=show_transneft_name() + show_transneft())
        # await bot.send_message(message.chat.id, text=show_phosagro_name() + show_phosagro())
        # await bot.send_message(message.chat.id, text=show_fsk_name() + show_fsk())

        # if message.text == '🏙 Недвижимость 🇷🇺':
        #   await bot.send_message(message.chat.id, text=show_pik_name() + show_pik())
        # await bot.send_message(message.chat.id, text=show_lsr_name() + show_lsr())

        # if message.text == '💊 Медицина 🇷🇺':
        #   await bot.send_message(message.chat.id, text=show_life_name() + show_life())
        # await bot.send_message(message.chat.id, text=show_iskj_name() + show_iskj())
        # await bot.send_message(message.chat.id, text=show_mdmg_name() + show_mdmg())
        # await bot.send_message(message.chat.id, text=show_gemc_name() + show_gemc())

        # if message.text == '◀️Назад':
        #   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # rus_stocks = types.KeyboardButton('🇷🇺 Акции')
        # usa_stocks = types.KeyboardButton('🇺🇸 Акции')
        # china_stocks = types.KeyboardButton('🇨🇳 Акции')
        # world_indexes = types.KeyboardButton('🌆 Мировые индексы')
        # back_button = types.KeyboardButton('◀️Назад')
        # markup.add(rus_stocks, usa_stocks, china_stocks, world_indexes, back_button)
        # await bot.send_message(message.chat.id, '🕑Загрузка', reply_markup=markup)

        # if message.text == '🇺🇸 Акции':
        #   await bot.send_message(message.chat.id, text=showIsxSnp500())

        # if message.text == '🇨🇳 Акции':
        #   await bot.send_message(message.chat.id, text=show_li_name() + show_li())
        # await bot.send_message(message.chat.id, text=show_baidu_name() + show_baidu())
        # await bot.send_message(message.chat.id, text=show_JD_name() + show_jd())
        # await bot.send_message(message.chat.id, text=show_bilibili_name() + show_bilibili())
        # await bot.send_message(message.chat.id, text=show_tencent_name() + show_tencent())
        # await bot.send_message(message.chat.id, text=show_nio_name() + show_nio())
        # await bot.send_message(message.chat.id, text=show_xpeng_name() + show_xpeng())

        # if message.text == '🌆 Мировые индексы':
        #   await bot.send_message(message.chat.id, text=show_MOEX_name() + show_MOEX())
        # await bot.send_message(message.chat.id, text=show_SnP500_name() + show_snp500())
        # await bot.send_message(message.chat.id, text=show_NASDAQ_name() + show_nasdaq())
        # await bot.send_message(message.chat.id, text=show_SHANGAI_name() + show_shanghai())

        # if message.text == '◀️Назад':
        #   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # currency_button = types.KeyboardButton('💰 Курс валют')
        # stocks_button = types.KeyboardButton('💸 Курс акций')
        # cryptocurrency_button = types.KeyboardButton('💎 Курс криптовалют')
        # information_button = types.KeyboardButton('⚙️ Разработчик')
        # markup.add(currency_button, stocks_button, cryptocurrency_button, information_button)
        # await bot.send_message(message.chat.id, '🕑Загружаю', reply_markup=markup)

        if message.text == '💎 Курс криптовалют':
            await bot.send_message(message.chat.id, '🕐🔜 Загружаю криптобазу...')
            await bot.send_message(message.chat.id, text=bitcoin.get_cryptocurrency_value() + '\n' +
                                                         ethereum.get_cryptocurrency_value() + '\n' +
                                                         litecoin.get_cryptocurrency_value() + '\n' +
                                                         cardano.get_cryptocurrency_value() + '\n' +
                                                         xrp.get_cryptocurrency_value() + '\n' +
                                                         doge.get_cryptocurrency_value() + '\n' +
                                                         bnb.get_cryptocurrency_value() + '\n' +
                                                         tether.get_cryptocurrency_value() + '\n' +
                                                         solana.get_cryptocurrency_value() + '\n' +
                                                         luna.get_cryptocurrency_value() + '\n' +
                                                         uniswap.get_cryptocurrency_value() + '\n' +
                                                         polkadot.get_cryptocurrency_value() + '\n' +
                                                         avalanche.get_cryptocurrency_value() + '\n' +
                                                         chainlink.get_cryptocurrency_value() + '\n' +
                                                         tron.get_cryptocurrency_value() + '\n' +
                                                         shiba.get_cryptocurrency_value())

        if message.text == '⚙️ Разработчик':
            await bot.send_message(message.chat.id,
                                   text='🌐 Разработчик: Миллер Ян Станиславович\n🏙 Студент НИУ ВШЭ, МИЭМ Информационная безопасность\n📚Уч.группа: БИБ211')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
