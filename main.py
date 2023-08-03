import json

from classes.api_classes import HeadHunterAPI, SuperJobAPI
from classes.json_interaction import SortFileJSON, SaveToJSON, LoadFileJSON, DeleteFileJSON, \
    RespondFileJSON, save_to_json, hh_for_dict, sj_for_dict, sorted_data, instance_vacancy_sorted, top_n_vacancies
from classes.vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("Python")
superjob_vacancies = superjob_api.get_vacancies("Python")


def user_interaction():
    platforms = ['1', '2', '3']
    platform = 0
    all_vacancies = []

    while platform not in platforms:
        resposibility_sj = 'см. в предыдущее поле'
        platform = input("Выберите платформу (1 или 2 или 3(все)):\n   1) HeadHunter\n   2) SuperJob\n   3) Все\n")
        match platform:
            case '1':
                print("Вы выбрали HeadHunter")

                for vacancy in hh_vacancies:
                    hh_vacancy = Vacancy(vacancy['name'], vacancy['salary']['from'], vacancy['salary']['to'],
                                         vacancy['alternate_url'],
                                         vacancy['snippet']['requirement'],
                                         vacancy['snippet']['responsibility'],
                                         vacancy["published_at"])
                    all_vacancies.append(hh_vacancy)
            case '2':
                print("Вы выбрали SuperJob")

                for vacancy in superjob_vacancies:
                    sj_vacancy = Vacancy(vacancy['profession'], vacancy['payment_from'], vacancy['payment_to'],
                                         vacancy['link'],
                                         vacancy['candidat'],
                                         None,
                                         vacancy["date_published"])
                    all_vacancies.append(sj_vacancy)
            case '3':
                print("Вы выбрали все платформы вакансий")

                for vacancy in hh_vacancies:
                    hh_vacancy = Vacancy(vacancy['name'], vacancy['salary']['from'], vacancy['salary']['to'],
                                         vacancy['alternate_url'],
                                         vacancy['snippet']['requirement'],
                                         vacancy['snippet']['responsibility'],
                                         vacancy["published_at"])
                    all_vacancies.append(hh_vacancy)

                for vacancy in superjob_vacancies:
                    sj_vacancy = Vacancy(vacancy['profession'], vacancy['payment_from'], vacancy['payment_to'],
                                         vacancy['link'],
                                         vacancy['candidat'],
                                         None,
                                         vacancy["date_published"])
                    all_vacancies.append(sj_vacancy)
            case _:
                print("Неправильный ввод. Попробуйте ещё раз.\n")

    # Сохраняю все вакансии в файл data
    save_to_json(all_vacancies, 'data/all_vacancies.json')
    json_saver = SaveToJSON()
    # Фильтр вакансии по зарплате не менее чем
    min_salary = int(input("Введите минимальную зарплату:\n"))
    json_loader = LoadFileJSON()
    dict_vacancy_with_salary_filter = json_loader.get_vacancies_by_salary(min_salary, 'data/all_vacancies.json')
    # Записываю в файл data suitable_vacancies.json
    json_saver.add_vacancy(dict_vacancy_with_salary_filter, 'data/suitable_vacancies.json')

    # Сортировка вакансий по зарплате от меньшего к большему
    # json_sort = SortFileJSON()

    # Удаляю вакансию по ссылке
    json_deleter = DeleteFileJSON()
    json_deleter.delete_vacancy("https://hh.ru/vacancy/84302495", 'data/suitable_vacancies_del.json')

    # Поисковый запрос пользователя в описании вакансии
    response = input("Введите поисковый запрос:\n")
    json_response = RespondFileJSON()
    suitable_vacancies_by_response = json_response.get_vacancies_by_response(response,
                                                                             'data/suitable_vacancies_by_response.json')

    #  сортируем список вакансий по дате
    sort_data = sorted_data(dict_vacancy_with_salary_filter)

    # создаем экземпляры класса после применения всех фильтров и сортировки
    list_instance_vacancy_sorted = instance_vacancy_sorted(sort_data)

    # выводим топ N список вакансий
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_n_vacancies(list_instance_vacancy_sorted, top_n)

    # сохраняем top N список вакансий в json файл
    while True:
        save_json = input("Сохранить в json файл? [y/n]: ")
        if save_json.lower() == 'y':
            json_saver.save_json(list_instance_vacancy_sorted)
            break
        elif save_json.lower() == 'n':
            print('Программа завершена')
            break
        else:
            print('Неверный ввод')

    # suitable_vacancies = []
    # with open('data/suitable_vacancies.json', 'r', encoding='utf-8') as file:
    #     data = json.load(file)
    # for vacancy in data:
    #     suit_vacancy = Vacancy(vacancy['name'],
    #                            vacancy['salary_from'],
    #                            vacancy['salary_to'],
    #                            vacancy['url'],
    #                            vacancy['info'],
    #                            vacancy['responsibility'],
    #                            vacancy["published_at"])
    #     suitable_vacancies.append(suit_vacancy)

    # json_sort.sort_vacancy(suitable_vacancies, 'data/suitable_vacancies_sorted.json')


if __name__ == "__main__":
    user_interaction()
