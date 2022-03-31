# Подключаю библиотеку aiogram для создания телеграм-бота
from aiogram import types, Bot, Dispatcher, executor
import config

# Подключаю функции по показу котировок с названиями криптовалют и их котировками из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.cryptocurrencies.crypto import bitcoin, ethereum, litecoin, cardano, xrp, doge, bnb, tether, \
    solana, luna, uniswap, polkadot, avalanche, chainlink, tron, shiba

# Подключаю функции по показу котировок валютных пар к рублю
from WarrenBuffetBot.currency.currency import usd_rub, euro_rub

# Подключаю функции по показу котировок российских акций потребительского сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.basic_sector_RU.stocks_basic_sector import magnit, x5retail, detskiymir, fixprice, mvideo, \
    cherkizovo

# Подключаю функции по показу котировок российских акций финансового сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.finance_sector_RU.stocks_finance_sector import vtb, tinkoffbank, mkb, sber, \
    sberprevs, afk, spbbank

# Подключаю функции по показу котировок российских акций IT-сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.IT_sector_RU.stocks_IT_sector import hhru, yandex, vk, mts, ozon, qiwi, rosseti, \
    rostelecom

# Подключаю функции по показу котировок российских акций сектора - недвижимость из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.realEstate_RU.realEstate_sector import pik, lsr

# Подключаю функции по показу котировок российскиз акций промышленного сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.industrial_sector.stocks_industrial_sector import globaltrans, petropavlovsk, polymetal, \
    alrosa, aeroflot, gazprom, interrao, lukoil, mmk, nlmk, novatek, nornikel, polyus, rosneft, rusal, rushydro, \
    severstal, surgutneft, tatneft, transneft, phosagro, fsk

# Подключаю функции по показу котировок китайских акций из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocks_China.stock_China import liauto, baidu, jd, bilibili, tencent, nio, xpeng

# Подключаю функции по показу котировок мировых индексов из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.world_indexes.world_indexes import moex, snp500, nasdaq, shangai

# Подключаю функции по показу котировок американских акций из моего модуля, где происходит основной парсинг
from stocksUSA.stocks_USA import alibaba, amazon, apple, exxon_mobil, netflix, meta, nvidia, gm, \
    alphabet, jpmorgan, microsoft, tesla, walmart, palantir

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
    currencyButton = types.KeyboardButton('💰 Курс валют')
    stocksButton = types.KeyboardButton('💸 Курс акций')
    cryptocurrencyButton = types.KeyboardButton('💎 Курс криптовалют')
    informationButton = types.KeyboardButton('⚙️ Разработчик')
    developerUrlButton = types.InlineKeyboardButton(text='Связаться с разработчиком',
                                                    url='https://coruscating-faun-401a0c.netlify.app/')
    markup.add(currencyButton, stocksButton, cryptocurrencyButton, informationButton, developerUrlButton)
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

        if message.text == 'Связаться с разработчиком':
            markup = types.InlineKeyboardMarkup()
            developerUrlButton = types.InlineKeyboardButton(text='Связаться с разработчиком',
                                                            url='https://coruscating-faun-401a0c.netlify.app/')
            markup.add(developerUrlButton)
            await bot.send_message(message.chat.id, text='Переходите на мой сайт ⬇️', reply_markup=markup)

        if message.text == '💰 Курс валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            backButton = types.KeyboardButton('◀️Назад')
            markup.add(backButton)
            await bot.send_message(message.chat.id, '🕑 Загружаю курсы валют\n 🟩Загрузка...', reply_markup=markup)
            await bot.send_message(message.chat.id,
                                   text='Доллар к рублю: ' + usd_rub.get_currency_value() + ' руб.' + '\n'
                                                                                                      'Евро к рублю: ' + euro_rub.get_currency_value() + ' руб.')

        if message.text == '◀️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            currencyButton = types.KeyboardButton('💰 Курс валют')
            stocksButton = types.KeyboardButton('💸 Курс акций')
            cryptocurrencyButton = types.KeyboardButton('💎 Курс криптовалют')
            informationButton = types.KeyboardButton('⚙️ Разработчик')
            developerUrlButton = types.InlineKeyboardButton(text='Связаться с разработчиком',
                                                            url='https://coruscating-faun-401a0c.netlify.app/')
            markup.add(currencyButton, stocksButton, cryptocurrencyButton, informationButton, developerUrlButton)
            await bot.send_message(message.chat.id, '◀️Назад', reply_markup=markup)

        if message.text == '💸 Курс акций':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            rusStocks = types.KeyboardButton('🇷🇺 Акции')
            usaStocks = types.KeyboardButton('🇺🇸 Акции')
            chinaStocks = types.KeyboardButton('🇨🇳 Акции')
            worldIndecies = types.KeyboardButton('🌆 Мировые индексы')
            backButton = types.KeyboardButton('◀️Назад')
            markup.add(rusStocks, usaStocks, chinaStocks, worldIndecies, backButton)
            await bot.send_message(message.chat.id, '🕑Загрузка', reply_markup=markup)

        if message.text == '🇷🇺 Акции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            basicSectorRus = types.KeyboardButton('🧃 Потребительский сектор 🇷🇺')
            ItSectorRus = types.KeyboardButton('📱 IT сектор 🇷🇺')
            financeSectorRus = types.KeyboardButton('🏦 Финансовый сектор 🇷🇺')
            industrialSectorRus = types.KeyboardButton('⛰ Промышленный сектор 🇷🇺')
            realEstateSectorRus = types.KeyboardButton('🏙 Недвижимость 🇷🇺')
            backButton = types.KeyboardButton('◀️Назад')
            markup.add(basicSectorRus, ItSectorRus, financeSectorRus, industrialSectorRus,
                       realEstateSectorRus, backButton)
            await bot.send_message(message.chat.id, text='🕑Загрузка', reply_markup=markup)

        if message.text == '🧃 Потребительский сектор 🇷🇺':
            await bot.send_message(message.chat.id, text=magnit.get_data() + '\n' +
                                                         x5retail.get_data() + '\n' +
                                                         detskiymir.get_data() + '\n' +
                                                         fixprice.get_data() + '\n' +
                                                         mvideo.get_data() + '\n' +
                                                         cherkizovo.get_data())

        if message.text == '📱 IT сектор 🇷🇺':
            await bot.send_message(message.chat.id, text=hhru.get_data() + '\n' +
                                                         yandex.get_data() + '\n' +
                                                         vk.get_data() + '\n' +
                                                         mts.get_data() + '\n' +
                                                         ozon.get_data() + '\n' +
                                                         qiwi.get_data() + '\n' +
                                                         rosseti.get_data() + '\n' +
                                                         rostelecom.get_data() + '\n')

        if message.text == '🏦 Финансовый сектор 🇷🇺':
            await bot.send_message(message.chat.id, text=vtb.get_data() + '\n' +
                                                         tinkoffbank.get_data() + '\n' +
                                                         mkb.get_data() + '\n' +
                                                         sber.get_data() + '\n' +
                                                         sberprevs.get_data() + '\n' +
                                                         afk.get_data() + '\n' +
                                                         spbbank.get_data())

        if message.text == '⛰ Промышленный сектор 🇷🇺':
            await bot.send_message(message.chat.id, text=globaltrans.get_data() + '\n' +
                                                         petropavlovsk.get_data() + '\n' +
                                                         polymetal.get_data() + '\n' +
                                                         alrosa.get_data() + '\n' +
                                                         aeroflot.get_data() + '\n' +
                                                         gazprom.get_data() + '\n' +
                                                         interrao.get_data() + '\n' +
                                                         lukoil.get_data() + '\n' +
                                                         mmk.get_data() + '\n' +
                                                         nlmk.get_data() + '\n' +
                                                         novatek.get_data() + '\n' +
                                                         nornikel.get_data() + '\n' +
                                                         polyus.get_data() + '\n' +
                                                         rosneft.get_data() + '\n' +
                                                         rusal.get_data() + '\n' +
                                                         rushydro.get_data() + '\n' +
                                                         severstal.get_data() + '\n' +
                                                         surgutneft.get_data() + '\n' +
                                                         tatneft.get_data() + '\n' +
                                                         transneft.get_data() + '\n' +
                                                         phosagro.get_data() + '\n' +
                                                         fsk.get_data())

        if message.text == '🏙 Недвижимость 🇷🇺':
            await bot.send_message(message.chat.id, text=pik.get_data() + '\n' +
                                                         lsr.get_data())

        if message.text == '◀️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            rusStocks = types.KeyboardButton('🇷🇺 Акции')
            usaStocks = types.KeyboardButton('🇺🇸 Акции')
            chinaStocks = types.KeyboardButton('🇨🇳 Акции')
            worldIndecies = types.KeyboardButton('🌆 Мировые индексы')
            backButton = types.KeyboardButton('◀️Назад')
            markup.add(rusStocks, usaStocks, chinaStocks, worldIndecies, backButton)
            await bot.send_message(message.chat.id, '🕑Загрузка', reply_markup=markup)

        if message.text == '🇺🇸 Акции':
            await bot.send_message(message.chat.id, text=alibaba.get_data() + '\n' +
                                                         amazon.get_data() + '\n' +
                                                         apple.get_data() + '\n' +
                                                         exxon_mobil.get_data() + '\n' +
                                                         netflix.get_data() + '\n' +
                                                         meta.get_data() + '\n' +
                                                         nvidia.get_data() + '\n' +
                                                         gm.get_data() + '\n' +
                                                         alphabet.get_data() + '\n' +
                                                         jpmorgan.get_data() + '\n' +
                                                         microsoft.get_data() + '\n' +
                                                         tesla.get_data() + '\n' +
                                                         walmart.get_data() + '\n' +
                                                         palantir.get_data()
                                   )

        if message.text == '🇨🇳 Акции':
            await bot.send_message(message.chat.id, text=liauto.get_data() + '\n' +
                                                         baidu.get_data() + '\n' +
                                                         jd.get_data() + '\n' +
                                                         bilibili.get_data() + '\n' +
                                                         tencent.get_data() + '\n' +
                                                         nio.get_data() + '\n' +
                                                         xpeng.get_data())

        if message.text == '🌆 Мировые индексы':
            await bot.send_message(message.chat.id, text=moex.get_data() + '\n' +
                                                         snp500.get_data() + '\n' +
                                                         nasdaq.get_data() + '\n' +
                                                         shangai.get_data())

        if message.text == '◀️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            currencyButton = types.KeyboardButton('💰 Курс валют')
            stocksButton = types.KeyboardButton('💸 Курс акций')
            cryptocurrencyButton = types.KeyboardButton('💎 Курс криптовалют')
            informationButton = types.KeyboardButton('⚙️ Разработчик')
            developerUrlButton = types.InlineKeyboardButton(text='Связаться с разработчиком',
                                                            url='https://coruscating-faun-401a0c.netlify.app/')
            markup.add(currencyButton, stocksButton, cryptocurrencyButton, informationButton, developerUrlButton)
            await bot.send_message(message.chat.id, '🕑Загружаю', reply_markup=markup)

    if message.text == '💎 Курс криптовалют':
        await bot.send_message(message.chat.id, '🕐🔜 Загружаю криптобазу...')
        await bot.send_message(message.chat.id, text=bitcoin.get_data() + '\n' +
                                                     ethereum.get_data() + '\n' +
                                                     litecoin.get_data() + '\n' +
                                                     cardano.get_data() + '\n' +
                                                     xrp.get_data() + '\n' +
                                                     doge.get_data() + '\n' +
                                                     bnb.get_data() + '\n' +
                                                     tether.get_data() + '\n' +
                                                     solana.get_data() + '\n' +
                                                     luna.get_data() + '\n' +
                                                     uniswap.get_data() + '\n' +
                                                     polkadot.get_data() + '\n' +
                                                     avalanche.get_data() + '\n' +
                                                     chainlink.get_data() + '\n' +
                                                     tron.get_data() + '\n' +
                                                     shiba.get_data())

    if message.text == '⚙️ Разработчик':
        await bot.send_message(message.chat.id,
                               text='🌐 Разработчик: Миллер Ян Станиславович\n🏙 Студент НИУ ВШЭ, МИЭМ Информационная безопасность\n📚Уч.группа: БИБ211')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
