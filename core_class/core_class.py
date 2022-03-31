import requests
from bs4 import BeautifulSoup


# Основной класс, реализующий парсинг процесс всего проекта
class Parsing:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

    def __init__(self, link, html_class_parsing, name):
        self.link = link
        self.html_class_parsing = html_class_parsing
        self.name = name

    def get_data(self):
        # Парсим всю страницу
        full_page = requests.get(self.link, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", self.html_class_parsing)
        return f'{self.name}{convert[0].text}'