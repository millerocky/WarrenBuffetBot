import requests
from bs4 import BeautifulSoup



# Парсинг данных о котировках акций - лидеров торгов фондового рынка России
'RUS лидер торгов №1'
stockRu_1_data = 'https://www.google.com/search?q=%D0%B2%D1%82%D0%B1+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8&sxsrf=AOaemvLzDI9TCV3LWosY6OunJcs-9KdYBg%3A1633127452199&ei=HIxXYcDYC5-GwPAPksGgmAc&ved=0ahUKEwjA1qTtoarzAhUfAxAIHZIgCHMQ4dUDCA4&uact=5&oq=%D0%B2%D1%82%D0%B1+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyBQgAEIAEMgQIABBDMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgYIABAKECo6BAgAEAo6BggAEAgQHjoECCMQJzoHCAAQsQMQQzoICAAQgAQQsQM6BggAEAcQHjoECAAQDUoECEEYAFCFlQtY07cLYMi8C2gAcAJ4AIABVIgB4AKSAQE1mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_1_page = requests.get(stockRu_1_data, headers=headers).text
stockRu_1_soup = BeautifulSoup(stockRu_1_page, 'html.parser')
stockRu_1_convert = stockRu_1_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_1_rub = stockRu_1_convert[0].text

stockRu_1_name_data = 'https://www.google.com/search?q=%D0%B2%D1%82%D0%B1+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8&sxsrf=AOaemvLzDI9TCV3LWosY6OunJcs-9KdYBg%3A1633127452199&ei=HIxXYcDYC5-GwPAPksGgmAc&ved=0ahUKEwjA1qTtoarzAhUfAxAIHZIgCHMQ4dUDCA4&uact=5&oq=%D0%B2%D1%82%D0%B1+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyBQgAEIAEMgQIABBDMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgYIABAKECo6BAgAEAo6BggAEAgQHjoECCMQJzoHCAAQsQMQQzoICAAQgAQQsQM6BggAEAcQHjoECAAQDUoECEEYAFCFlQtY07cLYMi8C2gAcAJ4AIABVIgB4AKSAQE1mAEAoAEBwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_1_name_page = requests.get(stockRu_1_name_data, headers=headers).text
stockRu_1_name_soup = BeautifulSoup(stockRu_1_name_page, 'html.parser')
stockRu_1_name_convert = stockRu_1_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_1_name = stockRu_1_name_convert[0].text


'RUS лидер торгов №2'
stockRu_2_data = 'https://www.google.com/search?q=headhunter+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8&oq=h&aqs=chrome.0.69i59j46i67i199i291i433j69i57j69i59j35i39j0i67l2j46i199i291i433i512j46i199i291i512j0i271.1214j1j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_2_page = requests.get(stockRu_2_data, headers=headers).text
stockRu_2_soup = BeautifulSoup(stockRu_2_page, 'html.parser')
stockRu_2_convert = stockRu_2_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_2_rub = stockRu_2_convert[0].text

stockRu_2_name_data = 'https://www.google.com/search?q=headhunter+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8&oq=h&aqs=chrome.0.69i59j46i67i199i291i433j69i57j69i59j35i39j0i67l2j46i199i291i433i512j46i199i291i512j0i271.1214j1j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_2_name_page = requests.get(stockRu_2_name_data, headers=headers).text
stockRu_2_name_soup = BeautifulSoup(stockRu_2_name_page, 'html.parser')
stockRu_2_name_convert = stockRu_2_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_2_name = stockRu_2_name_convert[0].text


'RUS лидер торгов №3'
stockRu_3_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B3%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC&sxsrf=AOaemvLHPS3gAgq4a0K5QZV4TzfAgy5upQ%3A1633128012021&ei=TI5XYYpS6rGuBImanbgK&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B3%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC&gs_lcp=Cgdnd3Mtd2l6EAEYAzIECCMQJzIECCMQJzIECAAQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIGCAAQBxAeMgQIABBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDOgcIIxCwAxAnOgcIABBHELADOhAILhDHARCjAhDIAxCwAxBDOhAILhDHARDRAxDIAxCwAxBDOgoIIxCwAhAnEJ0COgQIABANOg8IIxCwAhAnEJ0CEEYQ-gE6CggAEA0QBRAKEB46CAgAEA0QBRAeSgUIOBIBMUoECEEYAFD2GViiKWDFPWgBcAJ4AYABgAOIAfYGkgEFNy4zLTGYAQCgAQHIAQzAAQE&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_3_page = requests.get(stockRu_3_data, headers=headers).text
stockRu_3_soup = BeautifulSoup(stockRu_3_page, 'html.parser')
stockRu_3_convert = stockRu_3_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_3_rub = stockRu_3_convert[0].text

stockRu_3_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B3%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC&sxsrf=AOaemvLHPS3gAgq4a0K5QZV4TzfAgy5upQ%3A1633128012021&ei=TI5XYYpS6rGuBImanbgK&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B3%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC&gs_lcp=Cgdnd3Mtd2l6EAEYAzIECCMQJzIECCMQJzIECAAQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIGCAAQBxAeMgQIABBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDOgcIIxCwAxAnOgcIABBHELADOhAILhDHARCjAhDIAxCwAxBDOhAILhDHARDRAxDIAxCwAxBDOgoIIxCwAhAnEJ0COgQIABANOg8IIxCwAhAnEJ0CEEYQ-gE6CggAEA0QBRAKEB46CAgAEA0QBRAeSgUIOBIBMUoECEEYAFD2GViiKWDFPWgBcAJ4AYABgAOIAfYGkgEFNy4zLTGYAQCgAQHIAQzAAQE&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_3_name_page = requests.get(stockRu_3_name_data, headers=headers).text
stockRu_3_name_soup = BeautifulSoup(stockRu_3_name_page, 'html.parser')
stockRu_3_name_convert = stockRu_3_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_3_name = stockRu_3_name_convert[0].text


'RUS лидер торгов №4'
stockRu_4_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%BB%D1%83%D0%BA%D0%BE%D0%B9%D0%BB&sxsrf=AOaemvJUrQq2jtJ1M9y6ynEQVvnFEa-OBQ%3A1633128153867&ei=2Y5XYay0NIWSrwSe8L-oCQ&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%BB%D1%83%D0%BA%D0%BE%D0%B9%D0%BB&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQsQMQgwEQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoMCCMQJxCdAhBGEPoBOgQIIxAnOgcIABCxAxBDOgQIABBDSgQIQRgAUL_sBVjA8wVg6PsFaAFwAngAgAHiAogBiASSAQUyLjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_4_page = requests.get(stockRu_4_data, headers=headers).text
stockRu_4_soup = BeautifulSoup(stockRu_4_page, 'html.parser')
stockRu_4_convert = stockRu_4_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_4_rub = stockRu_4_convert[0].text

stockRu_4_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%BB%D1%83%D0%BA%D0%BE%D0%B9%D0%BB&sxsrf=AOaemvJUrQq2jtJ1M9y6ynEQVvnFEa-OBQ%3A1633128153867&ei=2Y5XYay0NIWSrwSe8L-oCQ&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%BB%D1%83%D0%BA%D0%BE%D0%B9%D0%BB&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQsQMQgwEQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoMCCMQJxCdAhBGEPoBOgQIIxAnOgcIABCxAxBDOgQIABBDSgQIQRgAUL_sBVjA8wVg6PsFaAFwAngAgAHiAogBiASSAQUyLjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_4_name_page = requests.get(stockRu_4_name_data, headers=headers).text
stockRu_4_name_soup = BeautifulSoup(stockRu_4_name_page, 'html.parser')
stockRu_4_name_convert = stockRu_4_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_4_name = stockRu_4_name_convert[0].text


'RUS лидер торгов №5'
stockRu_5_data = 'https://ru.investing.com/equities/magnit_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_5_page = requests.get(stockRu_5_data, headers=headers).text
stockRu_5_soup = BeautifulSoup(stockRu_5_page, 'html.parser')
stockRu_5_convert = stockRu_5_soup.findAll('span', {'class': 'instrument-price_last__KQzyA'})
stockRu_5_rub = stockRu_5_convert[0].text

stockRu_5_name_data = 'https://ru.investing.com/equities/magnit_rts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_5_name_page = requests.get(stockRu_5_name_data, headers=headers).text
stockRu_5_name_soup = BeautifulSoup(stockRu_5_name_page, 'html.parser')
stockRu_5_name_convert = stockRu_5_name_soup.findAll('h1', {'class': 'text-2xl', 'class': 'font-semibold', 'class': 'instrument-header_title__GTWDv', 'class': 'mobile:mb-2'})
stockRu_5_name = stockRu_5_name_convert[0].text


'RUS лидер торгов №6'
stockRu_6_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%BC%D0%BE%D1%81%D0%B1%D0%B8%D1%80%D0%B6%D0%B0&sxsrf=AOaemvLpeH6S2en6LzSq3c8GC9uXDs_kpw%3A1633128377361&ei=uY9XYabFFfHrrgT5_4fIDA&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%BC%D0%BE%D1%81%D0%B1%D0%B8%D1%80%D0%B6%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6BAgAEEM6CAgAEIAEELEDOgoIABCABBCHAhAUOggIABCABBDJAzoMCCMQJxCdAhBGEPoBOgsIABCABBCxAxCDAToECCMQJzoICAAQsQMQgwFKBAhBGABQhcUHWJ3VB2DU3QdoAnACeAGAAZ8CiAH0BpIBBTguMC4xmAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_6_page = requests.get(stockRu_6_data, headers=headers).text
stockRu_6_soup = BeautifulSoup(stockRu_6_page, 'html.parser')
stockRu_6_convert = stockRu_6_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_6_rub = stockRu_6_convert[0].text

stockRu_6_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%BC%D0%BE%D1%81%D0%B1%D0%B8%D1%80%D0%B6%D0%B0&sxsrf=AOaemvLpeH6S2en6LzSq3c8GC9uXDs_kpw%3A1633128377361&ei=uY9XYabFFfHrrgT5_4fIDA&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%BC%D0%BE%D1%81%D0%B1%D0%B8%D1%80%D0%B6%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6BAgAEEM6CAgAEIAEELEDOgoIABCABBCHAhAUOggIABCABBDJAzoMCCMQJxCdAhBGEPoBOgsIABCABBCxAxCDAToECCMQJzoICAAQsQMQgwFKBAhBGABQhcUHWJ3VB2DU3QdoAnACeAGAAZ8CiAH0BpIBBTguMC4xmAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_6_name_page = requests.get(stockRu_6_name_data, headers=headers).text
stockRu_6_name_soup = BeautifulSoup(stockRu_6_name_page, 'html.parser')
stockRu_6_name_convert = stockRu_6_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_6_name = stockRu_6_name_convert[0].text


'RUS лидер торгов №7'
stockRu_7_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%80%D0%BE%D1%81%D0%BD%D0%B5%D1%84%D1%82%D1%8C&sxsrf=AOaemvIeXvW2t7GsoLdWsZs6-muspu7Q-w%3A1633128504850&ei=OJBXYZ-uM_aGwPAPkoS_qAU&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%80%D0%BE%D1%81%D0%BD%D0%B5%D1%84%D1%82%D1%8C&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQsQMQgwEQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoHCCMQJxCdAjoECCMQJzoLCAAQgAQQsQMQgwE6BAgAEENKBAhBGABQppQIWJmmCGDSrwhoAnACeACAAawBiAGrA5IBAzQuMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_7_page = requests.get(stockRu_7_data, headers=headers).text
stockRu_7_soup = BeautifulSoup(stockRu_7_page, 'html.parser')
stockRu_7_convert = stockRu_7_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_7_rub = stockRu_7_convert[0].text

stockRu_7_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%80%D0%BE%D1%81%D0%BD%D0%B5%D1%84%D1%82%D1%8C&sxsrf=AOaemvIeXvW2t7GsoLdWsZs6-muspu7Q-w%3A1633128504850&ei=OJBXYZ-uM_aGwPAPkoS_qAU&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%80%D0%BE%D1%81%D0%BD%D0%B5%D1%84%D1%82%D1%8C&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQsQMQgwEQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoHCCMQJxCdAjoECCMQJzoLCAAQgAQQsQMQgwE6BAgAEENKBAhBGABQppQIWJmmCGDSrwhoAnACeACAAawBiAGrA5IBAzQuMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_7_name_page = requests.get(stockRu_7_name_data, headers=headers).text
stockRu_7_name_soup = BeautifulSoup(stockRu_7_name_page, 'html.parser')
stockRu_7_name_convert = stockRu_7_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_7_name = stockRu_7_name_convert[0].text


'RUS лидер торгов №8'
stockRu_8_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%81%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA%D0%B0&sxsrf=AOaemvJxJjAQ8uauSrehd5xi5Xx2OlNfBw%3A1633128642884&ei=wpBXYdG-NaySwPAPo-KryA0&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%81%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6CggAEIAEEIcCEBQ6DAgjECcQnQIQRhD6AToECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQgAQQsQM6CAgAELEDEIMBSgQIQRgAUJz9B1ipjAhgvZcIaAFwAngBgAHzAogBkgeSAQU4LjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_8_page = requests.get(stockRu_8_data, headers=headers).text
stockRu_8_soup = BeautifulSoup(stockRu_8_page, 'html.parser')
stockRu_8_convert = stockRu_8_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_8_rub = stockRu_8_convert[0].text

stockRu_8_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%81%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA%D0%B0&sxsrf=AOaemvJxJjAQ8uauSrehd5xi5Xx2OlNfBw%3A1633128642884&ei=wpBXYdG-NaySwPAPo-KryA0&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%81%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6CggAEIAEEIcCEBQ6DAgjECcQnQIQRhD6AToECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQgAQQsQM6CAgAELEDEIMBSgQIQRgAUJz9B1ipjAhgvZcIaAFwAngBgAHzAogBkgeSAQU4LjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_8_name_page = requests.get(stockRu_8_name_data, headers=headers).text
stockRu_8_name_soup = BeautifulSoup(stockRu_8_name_page, 'html.parser')
stockRu_8_name_convert = stockRu_8_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_8_name = stockRu_8_name_convert[0].text


'RUS лидер торгов №9'
stockRu_9_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D1%81%D1%82%D0%B0%D0%BB%D1%8C&sxsrf=AOaemvIb11o_CAovpibnofih1NwxLnDt8Q%3A1633128777719&ei=SZFXYfeuK-iIrwSa-q6ABA&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D1%81%D1%82%D0%B0%D0%BB%D1%8C&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6DAgjECcQnQIQRhD6AUoECEEYAFD-0QdY0OEHYJzpB2gBcAJ4AYAB3QKIAcwIkgEHOS4xLjAuMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_9_page = requests.get(stockRu_9_data, headers=headers).text
stockRu_9_soup = BeautifulSoup(stockRu_9_page, 'html.parser')
stockRu_9_convert = stockRu_9_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_9_rub = stockRu_9_convert[0].text

stockRu_9_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D1%81%D1%82%D0%B0%D0%BB%D1%8C&sxsrf=AOaemvIb11o_CAovpibnofih1NwxLnDt8Q%3A1633128777719&ei=SZFXYfeuK-iIrwSa-q6ABA&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D1%81%D1%82%D0%B0%D0%BB%D1%8C&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6DAgjECcQnQIQRhD6AUoECEEYAFD-0QdY0OEHYJzpB2gBcAJ4AYAB3QKIAcwIkgEHOS4xLjAuMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_9_name_page = requests.get(stockRu_9_name_data, headers=headers).text
stockRu_9_name_soup = BeautifulSoup(stockRu_9_name_page, 'html.parser')
stockRu_9_name_convert = stockRu_9_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_9_name = stockRu_9_name_convert[0].text


'RUS лидер торгов №10'
stockRu_10_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81&sxsrf=AOaemvJO0i3yHPSTsS5maNn80zuI022sdQ%3A1633128906665&ei=ypFXYaD9J4CGwPAP_YegqAk&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6BAgjECc6CwgAEIAEELEDEIMBOgQIABBDOgwIIxAnEJ0CEEYQ-gE6EAgAEIAEEIcCELEDEIMBEBQ6CAgAELEDEIMBSgQIQRgAUJa4B1i3vwdgx8gHaAFwAngBgAHMAogBmwSSAQUzLjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_10_page = requests.get(stockRu_10_data, headers=headers).text
stockRu_10_soup = BeautifulSoup(stockRu_10_page, 'html.parser')
stockRu_10_convert = stockRu_10_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_10_rub = stockRu_10_convert[0].text

stockRu_10_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81&sxsrf=AOaemvJO0i3yHPSTsS5maNn80zuI022sdQ%3A1633128906665&ei=ypFXYaD9J4CGwPAP_YegqAk&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6BAgjECc6CwgAEIAEELEDEIMBOgQIABBDOgwIIxAnEJ0CEEYQ-gE6EAgAEIAEEIcCELEDEIMBEBQ6CAgAELEDEIMBSgQIQRgAUJa4B1i3vwdgx8gHaAFwAngBgAHMAogBmwSSAQUzLjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_10_name_page = requests.get(stockRu_10_name_data, headers=headers).text
stockRu_10_name_soup = BeautifulSoup(stockRu_10_name_page, 'html.parser')
stockRu_10_name_convert = stockRu_10_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_10_name = stockRu_10_name_convert[0].text


'RUS лидер торгов №11'
stockRu_11_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+x5+retail+group&sxsrf=AOaemvLwRxHyMWNc6mUNNgJxnHp_vUwzxA%3A1633129031397&ei=R5JXYa7QF83HrgTjyJvIAQ&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+x5+retail+group&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEMkDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6DAgjECcQnQIQRhD6AToKCAAQgAQQhwIQFDoECAAQQzoECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQgAQQsQM6CAgAELEDEIMBOgcIABCABBAKOggIABAWEAoQHjoGCAAQFhAeSgQIQRgAUIuwB1jF3Qdgo-cHaARwAngAgAHvAogBygeSAQU5LjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_11_page = requests.get(stockRu_11_data, headers=headers).text
stockRu_11_soup = BeautifulSoup(stockRu_11_page, 'html.parser')
stockRu_11_convert = stockRu_11_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_11_rub = stockRu_11_convert[0].text

stockRu_11_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+x5+retail+group&sxsrf=AOaemvLwRxHyMWNc6mUNNgJxnHp_vUwzxA%3A1633129031397&ei=R5JXYa7QF83HrgTjyJvIAQ&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+x5+retail+group&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEMkDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6DAgjECcQnQIQRhD6AToKCAAQgAQQhwIQFDoECAAQQzoECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQgAQQsQM6CAgAELEDEIMBOgcIABCABBAKOggIABAWEAoQHjoGCAAQFhAeSgQIQRgAUIuwB1jF3Qdgo-cHaARwAngAgAHvAogBygeSAQU5LjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_11_name_page = requests.get(stockRu_11_name_data, headers=headers).text
stockRu_11_name_soup = BeautifulSoup(stockRu_11_name_page, 'html.parser')
stockRu_11_name_convert = stockRu_11_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_11_name = stockRu_11_name_convert[0].text


'RUS лидер торгов №12'
stockRu_12_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+tcs+group&sxsrf=AOaemvL5EJ1oUY7gM8MASznuNpvXJr0-gA%3A1633129272452&ei=OJNXYZOXG5eXrwScpKyoCg&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+tcs+group&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCCMQJxCdAjoNCAAQgAQQhwIQsQMQFDoHCAAQsQMQQzoICAAQgAQQsQM6CwgAEIAEELEDEIMBOgQIIxAnOgQIABBDOhAIABCABBCHAhCxAxCDARAUSgQIQRgAUMYhWJ89YIdJaAFwAngAgAGoAYgB2wWSAQM5LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_12_page = requests.get(stockRu_12_data, headers=headers).text
stockRu_12_soup = BeautifulSoup(stockRu_12_page, 'html.parser')
stockRu_12_convert = stockRu_12_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_12_rub = stockRu_12_convert[0].text

stockRu_12_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+tcs+group&sxsrf=AOaemvL5EJ1oUY7gM8MASznuNpvXJr0-gA%3A1633129272452&ei=OJNXYZOXG5eXrwScpKyoCg&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+tcs+group&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCCMQJxCdAjoNCAAQgAQQhwIQsQMQFDoHCAAQsQMQQzoICAAQgAQQsQM6CwgAEIAEELEDEIMBOgQIIxAnOgQIABBDOhAIABCABBCHAhCxAxCDARAUSgQIQRgAUMYhWJ89YIdJaAFwAngAgAGoAYgB2wWSAQM5LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_12_name_page = requests.get(stockRu_12_name_data, headers=headers).text
stockRu_12_name_soup = BeautifulSoup(stockRu_12_name_page, 'html.parser')
stockRu_12_name_convert = stockRu_12_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_12_name = stockRu_12_name_convert[0].text


'RUS лидер торгов №13'
stockRu_13_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+mail.ru&sxsrf=AOaemvJCRaY9FUbGqvmGqlm7lU1NJPw7rQ%3A1633129282550&ei=QpNXYc_wIImprgSDi63IBw&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+mail.ru&gs_lcp=Cgdnd3Mtd2l6EAEYATILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6DAgjECcQnQIQRhD6AToECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoECAAQQzoICAAQgAQQsQM6CAgAELEDEIMBSgQIQRgAUO_8B1is_wdg64cIaAFwAngAgAHGAogBhgOSAQUxLjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_13_page = requests.get(stockRu_13_data, headers=headers).text
stockRu_13_soup = BeautifulSoup(stockRu_13_page, 'html.parser')
stockRu_13_convert = stockRu_13_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_13_rub = stockRu_13_convert[0].text

stockRu_13_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+mail.ru&sxsrf=AOaemvJCRaY9FUbGqvmGqlm7lU1NJPw7rQ%3A1633129282550&ei=QpNXYc_wIImprgSDi63IBw&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+mail.ru&gs_lcp=Cgdnd3Mtd2l6EAEYATILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6DAgjECcQnQIQRhD6AToECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoECAAQQzoICAAQgAQQsQM6CAgAELEDEIMBSgQIQRgAUO_8B1is_wdg64cIaAFwAngAgAHGAogBhgOSAQUxLjMtMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_13_name_page = requests.get(stockRu_13_name_data, headers=headers).text
stockRu_13_name_soup = BeautifulSoup(stockRu_13_name_page, 'html.parser')
stockRu_13_name_convert = stockRu_13_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_13_name = stockRu_13_name_convert[0].text


'RUS лидер торгов №14'
stockRu_14_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B0%D0%BB%D1%80%D0%BE%D1%81%D0%B0&sxsrf=AOaemvJm9e-ukhtwgQ5ze1xj9RvCE5DoCA%3A1633129415394&ei=x5NXYfPOF-TGrgTew6-4AQ&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B0%D0%BB%D1%80%D0%BE%D1%81%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CAgAEIAEELADOgkIABCwAxAHEB46BwgjECcQnQI6CggAEIAEEIcCEBQ6DAgjECcQnQIQRhD6AToECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQsQMQgwFKBAhBGAFQuMgGWI3bBmDz5wZoAnAAeAGAAc0CiAHbBZIBBTYuMy0xmAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_14_page = requests.get(stockRu_14_data, headers=headers).text
stockRu_14_soup = BeautifulSoup(stockRu_14_page, 'html.parser')
stockRu_14_convert = stockRu_14_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_14_rub = stockRu_14_convert[0].text

stockRu_14_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B0%D0%BB%D1%80%D0%BE%D1%81%D0%B0&sxsrf=AOaemvJm9e-ukhtwgQ5ze1xj9RvCE5DoCA%3A1633129415394&ei=x5NXYfPOF-TGrgTew6-4AQ&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B0%D0%BB%D1%80%D0%BE%D1%81%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CAgAEIAEELADOgkIABCwAxAHEB46BwgjECcQnQI6CggAEIAEEIcCEBQ6DAgjECcQnQIQRhD6AToECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQsQMQgwFKBAhBGAFQuMgGWI3bBmDz5wZoAnAAeAGAAc0CiAHbBZIBBTYuMy0xmAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_14_name_page = requests.get(stockRu_14_name_data, headers=headers).text
stockRu_14_name_soup = BeautifulSoup(stockRu_14_name_page, 'html.parser')
stockRu_14_name_convert = stockRu_14_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_14_name = stockRu_14_name_convert[0].text


'RUS лидер торгов №15'
stockRu_15_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B0%D1%8D%D1%80%D0%BE%D1%84%D0%BB%D0%BE%D1%82%D0%B0&sxsrf=AOaemvKMWyrKdKrEUE68DK8FsWccizBciw%3A1633129527727&ei=N5RXYb_iK-GkrgTcq7fQBg&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B0%D1%8D%D1%80%D0%BE%D1%84%D0%BB%D0%BE%D1%82%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADIQCAAQgAQQsQMQgwEQRhD6ATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoHCCMQJxCdAjoLCAAQgAQQsQMQgwE6CggAEIAEEIcCEBQ6BAgAEEM6DAgjECcQnQIQRhD6AToICAAQgAQQsQM6CggAELEDEIMBEEM6EAgAEIAEEIcCELEDEIMBEBRKBAhBGABQmqwHWJnAB2CuyQdoAXACeAGAAd0CiAH8BZIBBTYuMy0xmAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_15_page = requests.get(stockRu_15_data, headers=headers).text
stockRu_15_soup = BeautifulSoup(stockRu_15_page, 'html.parser')
stockRu_15_convert = stockRu_15_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
stockRu_15_rub = stockRu_15_convert[0].text

stockRu_15_name_data = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B0%D1%8D%D1%80%D0%BE%D1%84%D0%BB%D0%BE%D1%82%D0%B0&sxsrf=AOaemvKMWyrKdKrEUE68DK8FsWccizBciw%3A1633129527727&ei=N5RXYb_iK-GkrgTcq7fQBg&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D0%B0%D1%8D%D1%80%D0%BE%D1%84%D0%BB%D0%BE%D1%82%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADIQCAAQgAQQsQMQgwEQRhD6ATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoHCCMQJxCdAjoLCAAQgAQQsQMQgwE6CggAEIAEEIcCEBQ6BAgAEEM6DAgjECcQnQIQRhD6AToICAAQgAQQsQM6CggAELEDEIMBEEM6EAgAEIAEEIcCELEDEIMBEBRKBAhBGABQmqwHWJnAB2CuyQdoAXACeAGAAd0CiAH8BZIBBTYuMy0xmAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
stockRu_15_name_page = requests.get(stockRu_15_name_data, headers=headers).text
stockRu_15_name_soup = BeautifulSoup(stockRu_15_name_page, 'html.parser')
stockRu_15_name_convert = stockRu_15_name_soup.findAll('div', {'class': 'oPhL2e'})
stockRu_15_name = stockRu_15_name_convert[0].text
