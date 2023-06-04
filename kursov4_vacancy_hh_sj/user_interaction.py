import json

from class_vacancy import Vacancy
from class_json_saver import JSONSaver
from get_sample_of_vacancies_lists import unite_samples_of_vacancies
from print_vacancies import print_vacancies

from colorama import Fore

def user_interaction():

    while True:
        choice = input(f"1. Поиск вакансии. \n2. Конец. \nEnter ")
        if choice == "2":
            break

        elif choice == "1":
            search_query = input(f"Введите данные для поиска: ")
            keywords = input("Введите слова для фильтра вакансий: ")

            while True:
                top_vacancies = input(f"Введите топ вакансий: ")
                if top_vacancies.isdigit():
                    top_vacancies = int(top_vacancies)
                    break
                else:
                    print(f"Это не номер\n")
                    continue

            not_sorted_vacancies = unite_samples_of_vacancies(search_query, keywords, top_vacancies)
            sorted_vacancies = Vacancy.sorted_by_salary(not_sorted_vacancies)

            add_in_file = input("Добавить в файл?  (1. Да  2. Нет)")
            if add_in_file == "1":
                JSONSaver.add_vacancies(sorted_vacancies, top_vacancies)


            try:
                with open("vacancies.json")  as file:
                    print_in_monitor = input("Показатӣ на экран?  (1. Да  2. Нет)")
                    if print_in_monitor == "1":
                        print_vacancies()

            except FileNotFoundError:
                continue

            task_complete = False
            while task_complete is False:
                user_choice = input("1. Завершить \n2. На начало (фильтр и добавление). \n3. Удаление. \n Интер: ")
                if user_choice.isdigit() and user_choice in ('1', '2', '3'):
                    if user_choice == "1":
                        print("ok")
                        break
                    elif user_choice == "3":
                        JSONSaver.delete_vacancies()
                        break


