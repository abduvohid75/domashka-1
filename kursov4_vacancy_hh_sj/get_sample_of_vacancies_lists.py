from class_vacancy import Vacancy
from classes_api import HeadHunterAPI, SuperJobAPI
#from colorama import Fore

import json
import os

def get_sample_of_vacancies_list_hh_ru(search_query: str, keywords: str, top_vacancies: int):
    vacancies = []

    HeadHunterAPI().get_vacancies(search_query, keywords, top_vacancies)
    file_write_jobs = 'hh_jobs.json'
    try:
        with open(file_write_jobs) as json_file_read:
            content = json.load(json_file_read)
            json_file_read.close()
    except FileNotFoundError:

        return []

    else:
        vacancy_index = 0
        barrier = len(content)

        for vacancy in content:
            #print(vacancy)


            if vacancy["snippet"]["requirement"] is None:
                requirement = "Unknown"
            else:
                requirement = vacancy["snippet"]["requirement"]

            if vacancy["snippet"]["responsibility"] is None:
                responsibility = "Unknown"
            else:
                responsibility = vacancy["snippet"]["responsibility"]

            name = vacancy["name"]
            url = vacancy["alternate_url"]

            professional_roles = vacancy["professional_roles"][0]["name"]
            experience = vacancy["experience"]["name"]
            employment = vacancy["employment"]["name"]

            if vacancy["salary"] is None:
                salary_from = 0
                salary_to = 0

            else:

                if vacancy["salary"]["from"] is None:
                    salary_from = 0
                else:
                    salary_from = vacancy["salary"]["from"]

                if vacancy["salary"]["to"] is None:
                    salary_to = 0
                else:
                    salary_to = vacancy["salary"]["to"]

            vacancies.append(Vacancy(name,url,salary_from,salary_to, requirement, responsibility, professional_roles, experience, employment))

            vacancy_index +=1
            if vacancy_index == barrier:
                os.remove(file_write_jobs)
                break
        return vacancies

def get_sample_of_vacancies_list_sj_ru(search_query: str, keywords: str, top_vacancies: int):

    vacancies = []

    SuperJobAPI().get_vacancies(search_query, keywords, top_vacancies)
    file_write_jobs = 'sj_jobs.json'
    try:
        with open(file_write_jobs) as json_file:
            content = json.load(json_file)
            json_file.close()
    except FileNotFoundError:

        return []

    else:
        vacancy_index = 0
        barrier = len(content)

        for vacancy in content:
            #print(vacancy)

            if vacancy["education"]["title"] is None:
                requirement = "Unknown"
            else:
                requirement = vacancy["education"]["title"]

            if vacancy["candidat"] is None:
                responsibility = "Unknown"
            else:
                responsibility = vacancy["candidat"]

            try:
                professional_roles = vacancy["catalogues"][0]["positions"][0]['title']
            except IndexError:
                professional_roles = 'Unknown'

            finally:
                name = vacancy["profession"]
                url = vacancy["link"]

                experience = vacancy["experience"]["title"]
                employment = vacancy["type_of_work"]["title"]
                salary_from = vacancy["payment_from"]
                salary_to = vacancy["payment_to"]

                vacancies.append(Vacancy(name,url,salary_from,salary_to, requirement, responsibility, professional_roles, experience, employment))

                vacancy_index +=1
                if vacancy_index == barrier:
                    os.remove(file_write_jobs)
                    break

        return vacancies

def unite_samples_of_vacancies(search_query: str, keywords: str, top_vacancies: int) -> object:

    vacancies_hh_ru = get_sample_of_vacancies_list_hh_ru(search_query, keywords, top_vacancies)
    vacancies_sj_ru = get_sample_of_vacancies_list_sj_ru(search_query, keywords, top_vacancies)
    vacancies_all = vacancies_sj_ru + vacancies_hh_ru

    return vacancies_all

















