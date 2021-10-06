import requests
from bs4 import BeautifulSoup


# Парсинг данных о котировках акций - лидеров торгов фондового рынка США
'USA лидер торгов №1'
stock_USA_1_data = 'https://www.google.com/search?q=alibaba+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&oq=alibaba+%D0%BA%D1%83&aqs=chrome.1.69i57j0i512l5j0i22i30j0i22i30i457j0i22i30l2.8126j0j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_1_page = requests.get(stock_USA_1_data, headers=headers).text
stock_USA_1_soup = BeautifulSoup(stock_USA_1_page, 'html.parser')
stock_USA_1_convert = stock_USA_1_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_1_dollar = stock_USA_1_convert[0].text

stock_USA_1_name_data = 'https://www.google.com/search?q=alibaba+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&oq=alibaba+%D0%BA%D1%83&aqs=chrome.1.69i57j0i512l5j0i22i30j0i22i30i457j0i22i30l2.8126j0j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_1_name_page = requests.get(stock_USA_1_name_data, headers=headers).text
stock_USA_1_name_soup = BeautifulSoup(stock_USA_1_name_page, 'html.parser')
stock_USA_1_name_convert = stock_USA_1_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_1_name = stock_USA_1_name_convert[0].text


'USA лидер торгов №2'
stock_USA_2_data = 'https://www.google.com/search?q=amazon+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvI6fDoAhbswJvih_bEZ7DkWNNLSoQ%3A1633130946205&ei=wplXYb2GDOiOxc8PpM-a0AU&ved=0ahUKEwi9763vrqrzAhVoR_EDHaSnBloQ4dUDCA4&uact=5&oq=amazon+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQ-gEyBggAEAgQHjoHCAAQRxCwAzoGCAAQBxAeOggIABAIEAcQHjoHCCMQsAIQJzoECAAQDToICAAQCBANEB46CQgAEA0QRhD6AUoECEEYAFDk1iFYg_MhYL_4IWgCcAJ4AIABTIgBtAWSAQIxMJgBAKABAcgBCMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_2_page = requests.get(stock_USA_2_data, headers=headers).text
stock_USA_2_soup = BeautifulSoup(stock_USA_2_page, 'html.parser')
stock_USA_2_convert = stock_USA_2_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_2_dollar = stock_USA_2_convert[0].text

stock_USA_2_name_data = 'https://www.google.com/search?q=amazon+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvI6fDoAhbswJvih_bEZ7DkWNNLSoQ%3A1633130946205&ei=wplXYb2GDOiOxc8PpM-a0AU&ved=0ahUKEwi9763vrqrzAhVoR_EDHaSnBloQ4dUDCA4&uact=5&oq=amazon+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQ-gEyBggAEAgQHjoHCAAQRxCwAzoGCAAQBxAeOggIABAIEAcQHjoHCCMQsAIQJzoECAAQDToICAAQCBANEB46CQgAEA0QRhD6AUoECEEYAFDk1iFYg_MhYL_4IWgCcAJ4AIABTIgBtAWSAQIxMJgBAKABAcgBCMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_2_name_page = requests.get(stock_USA_2_name_data, headers=headers).text
stock_USA_2_name_soup = BeautifulSoup(stock_USA_2_name_page, 'html.parser')
stock_USA_2_name_convert = stock_USA_2_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_2_name = stock_USA_2_name_convert[0].text



'USA лидер торгов №3'
stock_USA_3_data = 'https://www.google.com/search?q=apple+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvK3-YQ3VY61m8KxA-Ifyr_mVB8Y2w%3A1633132643744&ei=Y6BXYZfzLOvrrgSm7aXICQ&ved=0ahUKEwjXsOeYtarzAhXrtYsKHaZ2CZkQ4dUDCA4&uact=5&oq=apple+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgUIABCABDoGCAAQBxAeOggIABAIEAcQHkoECEEYAFDtNFjYRWDzR2gAcAJ4AIABSogBjgOSAQE2mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_3_page = requests.get(stock_USA_3_data, headers=headers).text
stock_USA_3_soup = BeautifulSoup(stock_USA_3_page, 'html.parser')
stock_USA_3_convert = stock_USA_3_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_3_dollar = stock_USA_3_convert[0].text

stock_USA_3_name_data = 'https://www.google.com/search?q=apple+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvK3-YQ3VY61m8KxA-Ifyr_mVB8Y2w%3A1633132643744&ei=Y6BXYZfzLOvrrgSm7aXICQ&ved=0ahUKEwjXsOeYtarzAhXrtYsKHaZ2CZkQ4dUDCA4&uact=5&oq=apple+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgUIABCABDoGCAAQBxAeOggIABAIEAcQHkoECEEYAFDtNFjYRWDzR2gAcAJ4AIABSogBjgOSAQE2mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_3_name_page = requests.get(stock_USA_3_name_data, headers=headers).text
stock_USA_3_name_soup = BeautifulSoup(stock_USA_3_name_page, 'html.parser')
stock_USA_3_name_convert = stock_USA_3_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_3_name = stock_USA_3_name_convert[0].text


'USA лидер торгов №4'
stock_USA_4_data = 'https://www.google.com/search?q=exxonmobil+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvKl9CZceOkf3yUDMHgz02bnT7jMTg%3A1633132654058&ei=bqBXYeD5Aof8rgSO1puwDg&oq=exxonmobil+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMggIABAIEAcQHjoECCMQJzoECAAQQzoLCAAQgAQQsQMQgwE6BQgAEIAESgQIQRgAUOOgDVjcsw1gh7wNaAJwAngAgAFOiAGlA5IBATaYAQCgAQHAAQE&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_4_page = requests.get(stock_USA_4_data, headers=headers).text
stock_USA_4_soup = BeautifulSoup(stock_USA_4_page, 'html.parser')
stock_USA_4_convert = stock_USA_4_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_4_dollar = stock_USA_4_convert[0].text

stock_USA_4_name_data = 'https://www.google.com/search?q=exxonmobil+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvKl9CZceOkf3yUDMHgz02bnT7jMTg%3A1633132654058&ei=bqBXYeD5Aof8rgSO1puwDg&oq=exxonmobil+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMggIABAIEAcQHjoECCMQJzoECAAQQzoLCAAQgAQQsQMQgwE6BQgAEIAESgQIQRgAUOOgDVjcsw1gh7wNaAJwAngAgAFOiAGlA5IBATaYAQCgAQHAAQE&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_4_name_page = requests.get(stock_USA_4_name_data, headers=headers).text
stock_USA_4_name_soup = BeautifulSoup(stock_USA_4_name_page, 'html.parser')
stock_USA_4_name_convert = stock_USA_4_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_4_name = stock_USA_4_name_convert[0].text


'USA лидер торгов №5'
stock_USA_5_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+netflix&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+net&aqs=chrome.0.0i131i433i512j0i512l9.5347j1j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_5_page = requests.get(stock_USA_5_data, headers=headers).text
stock_USA_5_soup = BeautifulSoup(stock_USA_5_page, 'html.parser')
stock_USA_5_convert = stock_USA_5_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_5_dollar = stock_USA_5_convert[0].text

stock_USA_5_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+netflix&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+net&aqs=chrome.0.0i131i433i512j0i512l9.5347j1j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_5_name_page = requests.get(stock_USA_5_name_data, headers=headers).text
stock_USA_5_name_soup = BeautifulSoup(stock_USA_5_name_page, 'html.parser')
stock_USA_5_name_convert = stock_USA_5_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_5_name = stock_USA_5_name_convert[0].text


'USA лидер торгов №6'
stock_USA_6_data = 'https://www.google.com/search?q=facebook+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvLvXxmHB9MvVyr0c98MD0fNN-ohEQ%3A1633132875416&ei=S6FXYdHlGO3yqwHk7Y3QDw&oq=facebook+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMggIABAIEAcQHjIICAAQCBAHEB4yCAgAEAcQBRAeOgcIABBHELADOgcIIxCwAhAnOgQIABANOgQIIxAnOgQIABBDOgsIABCABBCxAxCDAToFCAAQgAQ6CggAEAgQBxAKEB5KBAhBGABQ57cLWJXPC2Ck2AtoAnACeACAAbsBiAHIBZIBAzQuM5gBAKABAcgBCMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_6_page = requests.get(stock_USA_6_data, headers=headers).text
stock_USA_6_soup = BeautifulSoup(stock_USA_6_page, 'html.parser')
stock_USA_6_convert = stock_USA_6_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_6_dollar = stock_USA_6_convert[0].text

stock_USA_6_name_data = 'https://www.google.com/search?q=facebook+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvLvXxmHB9MvVyr0c98MD0fNN-ohEQ%3A1633132875416&ei=S6FXYdHlGO3yqwHk7Y3QDw&oq=facebook+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMggIABAIEAcQHjIICAAQCBAHEB4yCAgAEAcQBRAeOgcIABBHELADOgcIIxCwAhAnOgQIABANOgQIIxAnOgQIABBDOgsIABCABBCxAxCDAToFCAAQgAQ6CggAEAgQBxAKEB5KBAhBGABQ57cLWJXPC2Ck2AtoAnACeACAAbsBiAHIBZIBAzQuM5gBAKABAcgBCMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_6_name_page = requests.get(stock_USA_6_name_data, headers=headers).text
stock_USA_6_name_soup = BeautifulSoup(stock_USA_6_name_page, 'html.parser')
stock_USA_6_name_convert = stock_USA_6_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_6_name = stock_USA_6_name_convert[0].text


'USA лидер торгов №7'
stock_USA_7_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+nvidia&sxsrf=AOaemvLGcfJexQPvaY_omQVdjjrx-oxZKw%3A1633463973392&ei=pa5cYbSXF8TLrgTn3J2QDw&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+nvidia&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6BAgjECc6CAgAELEDEIMBOgQIABBDOgwIIxAnEJ0CEEYQ-gFKBAhBGABQg64LWLS-C2DHyAtoAnACeAGAAaUDiAG1BZIBBTQuNC0xmAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_7_page = requests.get(stock_USA_7_data, headers=headers).text
stock_USA_7_soup = BeautifulSoup(stock_USA_7_page, 'html.parser')
stock_USA_7_convert = stock_USA_7_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_7_dollar = stock_USA_7_convert[0].text

stock_USA_7_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+nvidia&sxsrf=AOaemvLGcfJexQPvaY_omQVdjjrx-oxZKw%3A1633463973392&ei=pa5cYbSXF8TLrgTn3J2QDw&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+nvidia&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6BAgjECc6CAgAELEDEIMBOgQIABBDOgwIIxAnEJ0CEEYQ-gFKBAhBGABQg64LWLS-C2DHyAtoAnACeAGAAaUDiAG1BZIBBTQuNC0xmAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_7_name_page = requests.get(stock_USA_7_name_data, headers=headers).text
stock_USA_7_name_soup = BeautifulSoup(stock_USA_7_name_page, 'html.parser')
stock_USA_7_name_convert = stock_USA_7_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_7_name = stock_USA_7_name_convert[0].text


'USA лидер торгов №8'
stock_USA_8_data = 'https://www.google.com/search?q=ge+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvJZLCfzyQ3JuBLjWqVe-ry7wFNOqQ%3A1633133067674&ei=C6JXYZrJKOLirgTviZ2IDw&oq=ge+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyCAgAEAgQBxAeMggIABAHEAUQHjoECCMQJzoECAAQQzoLCAAQgAQQsQMQgwE6BggAEAcQHkoECEEYAFCtzQ5YpNwOYLnkDmgBcAJ4AIABTIgBiAKSAQE0mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_8_page = requests.get(stock_USA_8_data, headers=headers).text
stock_USA_8_soup = BeautifulSoup(stock_USA_8_page, 'html.parser')
stock_USA_8_convert = stock_USA_8_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_8_dollar = stock_USA_8_convert[0].text

stock_USA_8_name_data = 'https://www.google.com/search?q=ge+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvJZLCfzyQ3JuBLjWqVe-ry7wFNOqQ%3A1633133067674&ei=C6JXYZrJKOLirgTviZ2IDw&oq=ge+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyCAgAEAgQBxAeMggIABAHEAUQHjoECCMQJzoECAAQQzoLCAAQgAQQsQMQgwE6BggAEAcQHkoECEEYAFCtzQ5YpNwOYLnkDmgBcAJ4AIABTIgBiAKSAQE0mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_8_name_page = requests.get(stock_USA_8_name_data, headers=headers).text
stock_USA_8_name_soup = BeautifulSoup(stock_USA_8_name_page, 'html.parser')
stock_USA_8_name_convert = stock_USA_8_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_8_name = stock_USA_8_name_convert[0].text


'USA лидер торгов №9'
stock_USA_9_data = 'https://www.google.com/search?q=google+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvIIU4IwioavjQmTLeZ141gcxfU-uQ%3A1633133310647&ei=_qJXYauGJ4WHwPAPs8O_wAg&oq=google+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMggIABAIEAcQHjIICAAQCBAHEB4yCAgAEAgQBxAeMggIABAHEAUQHjIICAAQBxAFEB46BwgAEEcQsANKBAhBGABQ_pYJWLudCWC8pwloAXACeACAAUeIAYgBkgEBMpgBAKABAcgBCMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_9_page = requests.get(stock_USA_9_data, headers=headers).text
stock_USA_9_soup = BeautifulSoup(stock_USA_9_page, 'html.parser')
stock_USA_9_convert = stock_USA_9_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_9_dollar = stock_USA_9_convert[0].text

stock_USA_9_name_data = 'https://www.google.com/search?q=google+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvIIU4IwioavjQmTLeZ141gcxfU-uQ%3A1633133310647&ei=_qJXYauGJ4WHwPAPs8O_wAg&oq=google+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMggIABAIEAcQHjIICAAQCBAHEB4yCAgAEAgQBxAeMggIABAHEAUQHjIICAAQBxAFEB46BwgAEEcQsANKBAhBGABQ_pYJWLudCWC8pwloAXACeACAAUeIAYgBkgEBMpgBAKABAcgBCMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_9_name_page = requests.get(stock_USA_9_name_data, headers=headers).text
stock_USA_9_name_soup = BeautifulSoup(stock_USA_9_name_page, 'html.parser')
stock_USA_9_name_convert = stock_USA_9_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_9_name = stock_USA_9_name_convert[0].text


'USA лидер торгов №10'
stock_USA_10_data = 'https://www.google.com/search?q=gpmorgan+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvLp2VI7ij1fKgaycucf3T0aRdkPtw%3A1633133464109&ei=mKNXYaKLBq_2qwGx5LvADw&ved=0ahUKEwiit_6fuKrzAhUv-yoKHTHyDvgQ4dUDCA4&uact=5&oq=gpmorgan+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEAgQDRAeOgcIABBHELADOgcIIxCwAhAnOgQIABANOgQIIxAnOgQIABBDOgsIABCABBCxAxCDAToFCAAQgAQ6BggAEAcQHjoICAAQCBAHEB46BQgAEM0CSgQIQRgAUMvaCFjouwlglMEJaANwAngAgAHyAYgBmAmSAQYxMy4wLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_10_page = requests.get(stock_USA_10_data, headers=headers).text
stock_USA_10_soup = BeautifulSoup(stock_USA_10_page, 'html.parser')
stock_USA_10_convert = stock_USA_10_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_10_dollar = stock_USA_10_convert[0].text

stock_USA_10_name_data = 'https://www.google.com/search?q=gpmorgan+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvLp2VI7ij1fKgaycucf3T0aRdkPtw%3A1633133464109&ei=mKNXYaKLBq_2qwGx5LvADw&ved=0ahUKEwiit_6fuKrzAhUv-yoKHTHyDvgQ4dUDCA4&uact=5&oq=gpmorgan+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEAgQDRAeOgcIABBHELADOgcIIxCwAhAnOgQIABANOgQIIxAnOgQIABBDOgsIABCABBCxAxCDAToFCAAQgAQ6BggAEAcQHjoICAAQCBAHEB46BQgAEM0CSgQIQRgAUMvaCFjouwlglMEJaANwAngAgAHyAYgBmAmSAQYxMy4wLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_10_name_page = requests.get(stock_USA_10_name_data, headers=headers).text
stock_USA_10_name_soup = BeautifulSoup(stock_USA_10_name_page, 'html.parser')
stock_USA_10_name_convert = stock_USA_10_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_10_name = stock_USA_10_name_convert[0].text


'USA лидер торгов №11'
stock_USA_11_data = 'https://www.google.com/search?q=%D0%BC%D0%B0%D0%B9%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D1%84%D1%82+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvKBGiA-x5nFxFqbNIdf4xVDlAGN9Q%3A1633133620918&ei=NKRXYeuoN9GnrgS2o4HgAQ&oq=%D0%BC%D0%B0%D0%B9%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D1%84%D1%82+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQzQIyBQgAEM0CMgUIABDNAjIFCAAQzQI6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgUIABCABDoGCAAQBxAeOggIABAIEAcQHkoECEEYAFCl2gZY_IoHYJebB2gAcAJ4AIABS4gBqwSSAQE4mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_11_page = requests.get(stock_USA_11_data, headers=headers).text
stock_USA_11_soup = BeautifulSoup(stock_USA_11_page, 'html.parser')
stock_USA_11_convert = stock_USA_11_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_11_dollar = stock_USA_11_convert[0].text

stock_USA_11_name_data = 'https://www.google.com/search?q=%D0%BC%D0%B0%D0%B9%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D1%84%D1%82+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvKBGiA-x5nFxFqbNIdf4xVDlAGN9Q%3A1633133620918&ei=NKRXYeuoN9GnrgS2o4HgAQ&oq=%D0%BC%D0%B0%D0%B9%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D1%84%D1%82+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQzQIyBQgAEM0CMgUIABDNAjIFCAAQzQI6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgUIABCABDoGCAAQBxAeOggIABAIEAcQHkoECEEYAFCl2gZY_IoHYJebB2gAcAJ4AIABS4gBqwSSAQE4mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_11_name_page = requests.get(stock_USA_11_name_data, headers=headers).text
stock_USA_11_name_soup = BeautifulSoup(stock_USA_11_name_page, 'html.parser')
stock_USA_11_name_convert = stock_USA_11_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_11_name = stock_USA_11_name_convert[0].text


'USA лидер торгов №12'
stock_USA_12_data = 'https://www.google.com/search?q=tesla+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvJNuHIbmN-jyR0QgMdOzLXmS0K54Q%3A1633133739966&ei=q6RXYdK7Os2FrwTjw43IBw&oq=tesla+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIECAAQDTIICAAQCBANEB4yBggAEAgQHjIICAAQCBANEB4yCAgAEAgQDRAeOgQIIxAnOgQIABBDOgsIABCABBCxAxCDAToFCAAQgAQ6BggAEAcQHjoICAAQCBAHEB5KBAhBGABQzsMHWNbUB2CI4QdoAHACeACAAZABiAHKA5IBAzQuMZgBAKABAcABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_12_page = requests.get(stock_USA_12_data, headers=headers).text
stock_USA_12_soup = BeautifulSoup(stock_USA_12_page, 'html.parser')
stock_USA_12_convert = stock_USA_12_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_12_dollar = stock_USA_12_convert[0].text

stock_USA_12_name_data = 'https://www.google.com/search?q=tesla+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvJNuHIbmN-jyR0QgMdOzLXmS0K54Q%3A1633133739966&ei=q6RXYdK7Os2FrwTjw43IBw&oq=tesla+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAEYADIECAAQDTIICAAQCBANEB4yBggAEAgQHjIICAAQCBANEB4yCAgAEAgQDRAeOgQIIxAnOgQIABBDOgsIABCABBCxAxCDAToFCAAQgAQ6BggAEAcQHjoICAAQCBAHEB5KBAhBGABQzsMHWNbUB2CI4QdoAHACeACAAZABiAHKA5IBAzQuMZgBAKABAcABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_12_name_page = requests.get(stock_USA_12_name_data, headers=headers).text
stock_USA_12_name_soup = BeautifulSoup(stock_USA_12_name_page, 'html.parser')
stock_USA_12_name_convert = stock_USA_12_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_12_name = stock_USA_12_name_convert[0].text



'USA лидер торгов №13'
stock_USA_13_data = 'https://www.google.com/search?q=walmart+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvKctcDqeLxIxq6az3W13y6TXstJxQ%3A1633133868137&ei=LKVXYZvmB_CJwPAPqLmc4Ac&ved=0ahUKEwibrNLguarzAhXwBBAIHagcB3wQ4dUDCA4&uact=5&oq=walmart+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgUIABCABDoGCAAQBxAeOggIABAIEAcQHkoECEEYAFCZ_gpY1ZkLYKefC2gAcAJ4AIABUogByQSSAQE4mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_13_page = requests.get(stock_USA_13_data, headers=headers).text
stock_USA_13_soup = BeautifulSoup(stock_USA_13_page, 'html.parser')
stock_USA_13_convert = stock_USA_13_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_13_dollar = stock_USA_13_convert[0].text

stock_USA_13_name_data = 'https://www.google.com/search?q=walmart+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&sxsrf=AOaemvKctcDqeLxIxq6az3W13y6TXstJxQ%3A1633133868137&ei=LKVXYZvmB_CJwPAPqLmc4Ac&ved=0ahUKEwibrNLguarzAhXwBBAIHagcB3wQ4dUDCA4&uact=5&oq=walmart+%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgUIABCABDoGCAAQBxAeOggIABAIEAcQHkoECEEYAFCZ_gpY1ZkLYKefC2gAcAJ4AIABUogByQSSAQE4mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_13_name_page = requests.get(stock_USA_13_name_data, headers=headers).text
stock_USA_13_name_soup = BeautifulSoup(stock_USA_13_name_page, 'html.parser')
stock_USA_13_name_convert = stock_USA_13_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_13_name = stock_USA_13_name_convert[0].text


'USA лидер торгов №14'
stock_USA_14_data = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9+pltr&sxsrf=AOaemvL_FaG3FbVG--IBn07N8vv_K5hmEw%3A1633134053193&ei=5aVXYYaOC8XHrgTZr4_oCQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9+pltr&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQCBAHEB4yCAgAEAgQBxAeOgcIABBHELADOg8IIxCwAhAnEJ0CEEYQ-gE6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgUIABCABDoKCAAQgAQQhwIQFDoGCAAQBxAeSgQIQRgAUOixAljRvQJgstECaAFwAngAgAGgA4gBtgeSAQU4LjQtMZgBAKABAcgBCMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_14_page = requests.get(stock_USA_14_data, headers=headers).text
stock_USA_14_soup = BeautifulSoup(stock_USA_14_page, 'html.parser')
stock_USA_14_convert = stock_USA_14_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stock_USA_14_dollar = stock_USA_14_convert[0].text

stock_USA_14_name_data = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9+pltr&sxsrf=AOaemvL_FaG3FbVG--IBn07N8vv_K5hmEw%3A1633134053193&ei=5aVXYYaOC8XHrgTZr4_oCQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%BA%D1%86%D0%B8%D0%B9+pltr&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQCBAHEB4yCAgAEAgQBxAeOgcIABBHELADOg8IIxCwAhAnEJ0CEEYQ-gE6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgUIABCABDoKCAAQgAQQhwIQFDoGCAAQBxAeSgQIQRgAUOixAljRvQJgstECaAFwAngAgAGgA4gBtgeSAQU4LjQtMZgBAKABAcgBCMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stock_USA_14_name_page = requests.get(stock_USA_14_name_data, headers=headers).text
stock_USA_14_name_soup = BeautifulSoup(stock_USA_14_name_page, 'html.parser')
stock_USA_14_name_convert = stock_USA_14_name_soup.findAll('div', {'class': 'oPhL2e'})
stock_USA_14_name = stock_USA_14_name_convert[0].text