import os
from pprint import pprint
import requests

from classes.abstract import APIInteraction

super_job_key = os.getenv('sj_key')


class SuperJobAPI(APIInteraction):
    def __init__(self, headers, params):
        self.headers = headers
        self.params = params

    def request(self):
        headers = {
            "X-Api-App-Id": super_job_key
        }

        params = {
            "keyword": "Python"
        }

        data = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers)
        pprint(data.json())

    def write_file(self):
        pass
    #