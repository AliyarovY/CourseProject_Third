import json
from pprint import pprint

import requests
from v_vars import api_key


class Meta:
    def __init__(self, page: int, name: str, per_page: int):
        self.page = page
        self.name = name
        self.per_page = per_page
        self.check()

    def check(self):
        assert all(isinstance(x, tp) for x, tp in zip([self.page, self.name, self.per_page], [int, str, int]))

    def get_page(self, params, link):
        req = requests.get(link, params)
        data = req.json()
        req.close()
        return data


class HH(Meta):
    def __init__(self, page=0, name='Python', per_page=10):
        super().__init__(page, name, per_page)
        self.data = self.get_data()

    def get_page(self):
        params = {
            'text': f'NAME:{self.name}',
            'area': 113,
            'page': self.page,
            'per_page': self.per_page
        }

        link = 'https://api.hh.ru/vacancies'
        return super().get_page(params, link)

    def get_data(self):
        res = []
        for k in self.get_page()['items']:
            now = {}
            now['name'] = k['name']
            now['url'] = k['alternate_url']
            now['money'] = k['salary']
            now['description'] = k['snippet']['requirement']
            res.append(now)
        return res


class SJ(Meta):
    def __init__(self, page=0, name='Python', per_page=10):
        super().__init__(page, name, per_page)
        self.data = self.get_data()

    def get_page(self):
        return super().get_page({'area': 113, 'app_key': api_key, 'count': self.per_page, 'page': self.page, 'keywords': self.name},
                                'https://api.superjob.ru/2.0/vacancies')

    def get_data(self):
        res = []
        for k in self.get_page()['objects']:
            now = {}
            now['name'] = k['profession']
            now['url'] = k['link']
            now['money'] = {}
            now['money']['from'] = k['payment_from']
            now['money']['to'] = k['payment_to']
            now['money']['currency'] = k['currency']
            now['description'] = k['vacancyRichText']
            res.append(now)
        return res


