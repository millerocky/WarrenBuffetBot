import requests
from bs4 import BeautifulSoup


# Получение данных о курсе валют, используя парсинг данных с помощью BeautifulSoup
dollar_data = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&aqs=chrome.2.69i57j0i20i263i433i512j0i67i433j0i67j0i67i433j0i20i263i433i457i512j0i402j0i433i512j0i67i131i433j0i433i512.3857j1j15&sourceid'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
dollar_page = requests.get(dollar_data, headers=headers).text
dollar_soup = BeautifulSoup(dollar_page, 'html.parser')
dollar_convert = dollar_soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
dollar_rub = dollar_convert[0].text

euro_data = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&sxsrf=AOaemvKjntOoSFXPva59HA82F9jEM7nc8Q%3A1632602363779&ei=-4hPYdT_LsuHxc8Pk--XgAs&oq=%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAEYADISCAAQgAQQhwIQsQMQFBBGEIICMggIABCABBCxAzIKCAAQgAQQhwIQFDIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQM6BwgjEOoCECc6BAgjECc6BAguECc6DQgAEIAEEIcCELEDEBRKBAhBGABQxr8FWNnGBWDu0gVoAXACeACAAV-IAecCkgEBNJgBAKABAbABCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
euro_page = requests.get(euro_data, headers=headers).text
euro_soup = BeautifulSoup(euro_page, 'html.parser')
euro_convert = euro_soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
euro_rub = euro_convert[0].text