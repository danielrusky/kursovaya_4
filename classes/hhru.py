import os
import requests
from abstract import APIInteraction
from vacancy import Vacancy


class HeadHunterAPI(APIInteraction):
    def request(self, name, page):   # name, page
        """
        Создаем метод для получения страницы со списком вакансий
        """
        params = {
            "text": f'NAME: {name}',  # Текст фильтра name
            "area": 1,  # Поиск осуществляется по городу Москва
            "page": {page},  # Индекс страницы поиска на hh page
            "per_page": 100  # Количество вакансий на 1 странице
        }

        get_data = requests.get("https://api.hh.ru/vacancies", params=params)  # Посылаем запрос к API
        data = get_data.json()
        print(data)
        print(get_data)

        return data
