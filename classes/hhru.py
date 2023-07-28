import requests

from abstract import APIInteraction

from vacancy import Vacancy
##

class HeadHunterAPI(APIInteraction):
    def request(self, name, page=0):
        params = {
            "text": f'NAME: {name}',
            "area": 1,
            "page": page,
            "per_page": 100
        }
        get_data = requests.get("https://api.hh.ru/vacancies", params)
        data = get_data.json()

        return self.parse(data)



def parse(self, data) -> list[Vacancy]:
    vacancy_list = []
    for vacancy in data["items"]:
        name = vacancy['name']
        url = vacancy['alternate_url']
        if "salary" in vacancy and vacancy ["salar"]:
            salary = f' от {vacancy["salary"]["from"]} до {vacancy["salary"]["to"]}'
        else:
            salary = f'Заработная плата не указана'
        experience = vacancy["snippet"]["requirement"]
        vacancy_list.append(Vacancy(name, url, salary, experience))
    return  vacancy_list

