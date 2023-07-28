import json


class JSONSaver():
    filename = "data.json"

    def read_file(self):
        with open(self.filename) as file:
            return json.load(file)

    def write_file(self, data):
        with open(self.filename, 'w') as file:
            file.write(json.dumps(data))

    def add_vacancy(self, vacancy):
        data = self.read_file()
        data.append(vacancy.to_dict())
        self.write_file(data)

    def get_vacancy_by_salary(self, salary):
        vacancies_by_salary = []
        for vacancy in self.read_file():
            if vacancy["salary"] == salary:
                vacancies_by_salary.append(vacancy)
        return vacancies_by_salary

    def delete_vacancy(self, vacancy_):
        vacancies = []
        for vacancy in self.read_file():
            if vacancy['url'] != vacancy_.url:
                vacancies.append(vacancy)
        self.write_file(vacancies)