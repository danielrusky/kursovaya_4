from abc import ABC, abstractmethod

import json
from operator import itemgetter
from classes.vacancy import Vacancy

def write_file(filename):
    pass


def save_to_json(vacancy, filename):
    vacs = []
    for item in vacancy:
        vacs.append(item.__dict__)
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(vacs, indent=2, ensure_ascii=False))
    print(f'\nЗаписано {len(vacs)} вакансий в файл {filename}\n')

def hh_for_dict(hh_vacancies):
    hh_vacancies_dict = []
    for vacancy in hh_vacancies:
        hh_vacancy = Vacancy(vacancy['name'],
                             vacancy['salary']['from'],
                             vacancy['salary']['to'],
                             vacancy['alternate_url'],
                             vacancy['snippet']['requirement'],
                             vacancy['snippet']['responsibility'])
        hh_vacancies_dict.append(hh_vacancy)
    return hh_vacancies_dict

def sj_for_dict(superjob_vacancies):
    sj_vacancies_dict = []
    for vacancy in superjob_vacancies:
        sj_vacancy = Vacancy(vacancy['profession'],
                             vacancy['payment_from'],
                             vacancy['payment_to'],
                             vacancy['link'],
                             vacancy['candidat'],
                             None)
        sj_vacancies_dict.append(sj_vacancy)
    return sj_vacancies_dict


class APIIteraction(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях.
    """

    @abstractmethod
    def add_vacancy(self, vacancy, filename):
        pass

    def get_vacancies_by_response(self, response, filename):
        pass

    def get_vacancies_by_salary(self, salary, filename):
        pass

    def delete_vacancy(self, vacancy_del, filename):
        pass

    def sort_vacancy(self, list_vacancies, filename_to):
        pass

    def read_file(self, filename):
        with open(filename, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data


class SaveToJSON(APIIteraction):
    """
    Класс для сохранения информации о вакансиях в JSON-файл.
    """

    def add_vacancy(self, vacancy, filename):
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(vacancy, indent=2, ensure_ascii=False))
        print(f'\nЗаписано {len(vacancy)} вакансий в файл {filename}')


class LoadFileJSON(APIIteraction):
    """
    Класс для загрузки информации о вакансиях из JSON-файл.
    """

    def add_vacancy(self, vacancy, filename):
        pass

    def get_vacancies_by_salary(self, salary, filename):
        with open(filename, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        new_list = []
        for item in data:
            if item['salary_from'] is None:
                continue
            if salary <= item['salary_from']:
                new_list.append(item)
        return new_list


class DeleteFileJSON(APIIteraction):
    """
    Класс для удаления определенной вакансии из JSON-файл.
    """

    def add_vacancy(self, vacancy, filename):
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(vacancy, indent=2, ensure_ascii=False))
        print(f'\nЗаписано {len(vacancy)} вакансий в файл {filename} без лишней вакансии')

    def delete_vacancy(self, vacancy_del_url, filename):
        vacancies = []
        for vacancy in self.read_file('json/suitable_vacancies.json'):
            if vacancy['url'] != vacancy_del_url:
                vacancies.append(vacancy)
        self.add_vacancy(vacancies, filename)


class RespondFileJSON(APIIteraction):

    def add_vacancy(self, vacancy, filename):
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(vacancy, indent=2, ensure_ascii=False))
        print(f'\nЗаписано {len(vacancy)} вакансий в файл {filename} соответствующих запросу')

    def get_vacancies_by_response(self, response, filename):
        vacancies = []
        for vacancy in self.read_file('json/suitable_vacancies.json'):
            if response in str(vacancy['info']) or response in str(vacancy['name']):
                vacancies.append(vacancy)
        self.add_vacancy(vacancies, filename)


class SortFileJSON(APIIteraction):
    def add_vacancy(self, vacancy, filename):
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(vacancy, indent=2, ensure_ascii=False))
        print(f'\nЗаписано {len(vacancy)} вакансий в файл {filename} соответствующих запросу')

    def sort_vacancy(self, list_vacancies, filename_to):
        # vacancies = []
        vacancies = sorted(list_vacancies, key=itemgetter('salary_from'))
        # vacancies = sorted(list_vacancies, key=lambda d: d['salary_from'])
        # vacancies = list_vacancies.sort(key=lambda x: x['salary_from'], reverse=True)
        self.add_vacancy(vacancies, filename_to)
