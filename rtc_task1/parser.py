import requests
from bs4 import BeautifulSoup
from selectors_list import Selectors


class Parse:
    def __init__(self, url):
        self.url: str = url
        self.selectors = Selectors.__dict__

    def data_collector(self) -> dict:
        row = {}
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            for key, value in self.selectors.items():
                if "_" in key:
                    continue

                element = soup.select_one(value['selector'])

                if element:
                    row[value['column']] = element.get_text(strip=True)
                else:
                    row[value['column']] = "Данные отсутствуют"

            return row
