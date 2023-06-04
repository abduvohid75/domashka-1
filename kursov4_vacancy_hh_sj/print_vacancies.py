#from colorama import Fore

import json

def print_vacancies():

    try:
        with open("vacancies.json")  as json_file:
            content = json.load(json_file)
            json_file.close()
    except FileNotFoundError:
        print('')
    else:
        vacancies_count = 0
        for vacancy in content:
            print(f'Title:{vacancy["items"]["name"]}')
            print(f'URL: {vacancy["items"]["url"]}')
            print(f'From:{vacancy["items"]["salary_from"]}')
            print(f'To:{vacancy["items"]["salary_to"]}')
            print(f'Requirement:{vacancy["items"]["requirement"]}')
            print(f'Responsibility:{vacancy["items"]["responsibility"]}')
            print(f'Position:{vacancy["items"]["professional_roles"]}')
            print(f'Experience:{vacancy["items"]["experience"]}')
            print(f'Type of Employment:{vacancy["items"]["employment"]}\n')
            vacancies_count +=1
        print(f"Всего:  {vacancies_count}\n")




