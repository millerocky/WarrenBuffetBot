import requests
from bs4 import BeautifulSoup


# Парсинг данных о котировках мировых индексов

MOEX_index_data = 'https://www.google.com/search?q=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D0%BC%D0%BE%D1%81%D0%B1%D0%B8%D1%80%D0%B6%D0%B8&oq=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D0%BC%D0%BE&aqs=chrome.1.0i433i512j0i131i433i512j69i57j0i512l7.4157j0j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MOEX_index_page = requests.get(MOEX_index_data, headers=headers).text
MOEX_index_soup = BeautifulSoup(MOEX_index_page, 'html.parser')
MOEX_index_convert = MOEX_index_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
MOEX_index_rub = MOEX_index_convert[0].text

MOEX_index_name_data = 'https://www.google.com/search?q=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D0%BC%D0%BE%D1%81%D0%B1%D0%B8%D1%80%D0%B6%D0%B8&oq=%D0%B8%D0%BD&aqs=chrome.2.69i59l3j69i57j0i131i433i512j46i199i291i433i512j0i20i263i433i512j0i433i512j46i131i433i512j0i433i512.1729j0j15&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
MOEX_index_name_page = requests.get(MOEX_index_name_data, headers=headers).text
MOEX_index_name_soup = BeautifulSoup(MOEX_index_name_page, 'html.parser')
MOEX_index_name_convert = MOEX_index_name_soup.findAll('div', {'class': 'oPhL2e'})
MOEX_index_name = 'Московская биржа'



SnP500_index_data = 'https://www.google.com/search?q=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+s%26p+500&sxsrf=AOaemvJtEs9OAqa3lY3SloDtU5zKFSEUsg%3A1633135340807&ei=7KpXYerpMI6wrgTi7bWYCA&oq=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+s%26p+500&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMggIABCABBDJAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BwgjECcQnQI6BAgAEEM6CAgAEIAEELEDSgQIQRgAUO7AC1iGyAtg89MLaAFwAngBgAGMAogBlQSSAQU0LjAuMZgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SnP500_index_page = requests.get(SnP500_index_data, headers=headers).text
SnP500_index_soup = BeautifulSoup(SnP500_index_page, 'html.parser')
SnP500_index_convert = SnP500_index_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
SnP500_index = SnP500_index_convert[0].text

SnP500_index_name_data = 'https://www.google.com/search?q=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+snp500&sxsrf=AOaemvL14H8Kf5zB-fROIidRC_tYMRBIfA%3A1633137362366&ei=0rJXYcnkFejmrgSr1auIBw&oq=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+snp500&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQhwIQFDIKCAAQgAQQhwIQFDIFCAAQgAQyBAgAEAoyBAgAEAoyBwgAEMkDEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAo6BwgjELADECc6BwgAEEcQsAM6BwgAELADEEM6BAgAEEM6BwgjECcQnQI6CAgAEIAEELEDOgQIIxAnOggIABCABBDJA0oECEEYAFDFsAVYq8YFYJjWBWgEcAJ4AIABVogBoweSAQIxNJgBAKABAcgBCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SnP500_index_name_page = requests.get(SnP500_index_name_data, headers=headers).text
SnP500_index_name_soup = BeautifulSoup(SnP500_index_name_page, 'html.parser')
SnP500_index_name_convert = SnP500_index_name_soup.findAll('div', {'class': 'oPhL2e'})
SnP500_index_name = 'S&P 500'



NASDAQ_index_data = 'https://www.google.com/search?q=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+nasdaq+%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8&sxsrf=AOaemvKNlzQ6Pn_v3C2BW083jCmUmw_Bvg%3A1633464276431&ei=1K9cYdTeGeGurgTE0bbQCw&ved=0ahUKEwjUmMzPiLTzAhVhl4sKHcSoDboQ4dUDCA8&uact=5&oq=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+nasdaq+%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOgQIABBDOgUIABCABEoECEEYAFD1DVjGPWDhQmgBcAJ4AIABvQGIAYQHkgEDOC4ymAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
NASDAQ_index_page = requests.get(NASDAQ_index_data, headers=headers).text
NASDAQ_index_soup = BeautifulSoup(NASDAQ_index_page, 'html.parser')
NASDAQ_index_convert = NASDAQ_index_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
NASDAQ_index = NASDAQ_index_convert[0].text

NASDAQ_index_name_data = 'https://www.google.com/search?q=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+nasdaq+%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8&sxsrf=AOaemvKNlzQ6Pn_v3C2BW083jCmUmw_Bvg%3A1633464276431&ei=1K9cYdTeGeGurgTE0bbQCw&ved=0ahUKEwjUmMzPiLTzAhVhl4sKHcSoDboQ4dUDCA8&uact=5&oq=%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+nasdaq+%D0%BA%D0%BE%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOgQIABBDOgUIABCABEoECEEYAFD1DVjGPWDhQmgBcAJ4AIABvQGIAYQHkgEDOC4ymAEAoAEByAEKwAEB&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
NASDAQ_index_name_page = requests.get(NASDAQ_index_name_data, headers=headers).text
NASDAQ_index_name_soup = BeautifulSoup(NASDAQ_index_name_page, 'html.parser')
NASDAQ_index_name_convert = NASDAQ_index_name_soup.findAll('div', {'class': 'oPhL2e'})
NASDAQ_index_name = NASDAQ_index_name_convert[0].text



SHANGAI_index_data = 'https://www.google.com/search?q=shanghai+index&sxsrf=AOaemvIPlHN6iUmetwYwjt2T-DrXILHzNg%3A1633136217898&ei=Wa5XYc2bNsqrrgSE_6_ACg&ved=0ahUKEwiNrIzBwqrzAhXKlYsKHYT_C6gQ4dUDCA4&uact=5&oq=shanghai+index&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAEIAEEIcCEBQQRhD6ATIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjoHCAAQRxCwAzoHCAAQsAMQQzoQCC4QxwEQ0QMQyAMQsAMQQzoKCAAQgAQQhwIQFEoFCDgSATFKBAhBGABQ9BRYuBhg1BxoAXACeACAAUWIAcQBkgEBM5gBAKABAcgBDMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SHANGAI_index_page = requests.get(SHANGAI_index_data, headers=headers).text
SHANGAI_index_soup = BeautifulSoup(SHANGAI_index_page, 'html.parser')
SHANGAI_index_convert = SHANGAI_index_soup.findAll('span', {'class': 'IsqQVc', 'class': 'NprOob', 'class': 'XcVN5d', 'class': 'wT3VGc'})
SHANGAI_index = SHANGAI_index_convert[0].text

SHANGAI_index_name_data = 'https://www.google.com/search?q=shanghai+index&sxsrf=AOaemvIPlHN6iUmetwYwjt2T-DrXILHzNg%3A1633136217898&ei=Wa5XYc2bNsqrrgSE_6_ACg&ved=0ahUKEwiNrIzBwqrzAhXKlYsKHYT_C6gQ4dUDCA4&uact=5&oq=shanghai+index&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAEIAEEIcCEBQQRhD6ATIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjoHCAAQRxCwAzoHCAAQsAMQQzoQCC4QxwEQ0QMQyAMQsAMQQzoKCAAQgAQQhwIQFEoFCDgSATFKBAhBGABQ9BRYuBhg1BxoAXACeACAAUWIAcQBkgEBM5gBAKABAcgBDMABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
SHANGAI_index_name_page = requests.get(SHANGAI_index_name_data, headers=headers).text
SHANGAI_index_name_soup = BeautifulSoup(SHANGAI_index_name_page, 'html.parser')
SHANGAI_index_name_convert = SHANGAI_index_name_soup.findAll('div', {'class': 'oPhL2e'})
SHANGAI_index_name = SHANGAI_index_name_convert[0].text