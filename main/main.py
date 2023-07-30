# Создание экземпяра класса для работы с API сайтов с вакансиями
from abc import abstractmethod
from classes.hhru import HeadHunterAPI
from classes.jsonsaver import JSONSaver
from classes.vacancy import Vacancy
from classes.superjob import SuperJobAPI


vacancies_json = []

print('Вам будет представлена информация по superjob и headhunter')
keyword = input('Введите ключевое слово для поиска: ')
vacancy_by_salary = input("По какой зарплате будет осуществлен поиск")
name_founder = input("Введите поисковое слово для работа с вакансиями")
first_salary = input("От какой зарплаты будет произведен поиск")
second_salary = input("До какой зарплаты будет произведен поиск")
skills = input("Какой опыт работы должен быть учтен для поиска")


hhru = HeadHunterAPI(keyword)
super_job = SuperJobAPI(keyword)
for api in (hhru, super_job):
    api.write_file(pages_count=10)
    vacancies_json.extend(api.write_file)

# Получение вакансий с разных платформ
hh_vacancies = hhru.request()
superjob_vacancies = super_job.request()

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy(f'{name_founder}, "<https://hh/ru/vacancy/123456>", {first_salary}-{second_salary} руб.", '
                  f'"Требования: опыт работы от {skills} лет..."')

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.get_vacancy_by_salary(vacancy_by_salary)
json_saver.delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковой запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))


if __name__ == "__main__":
    user_interaction()