# coding: utf8
from abc import ABC, abstractmethod
import requests
import json
import os
import time



class SiteAPI(ABC):

    @abstractmethod
    def get_vacancies(self, search_query: str, keywords: str, top_vacancies: int):
        pass


class HeadHunterAPI(SiteAPI):

    def get_vacancies(self, search_query: str, keywords: str, top_vacancies: int):
        page_number = 0
        pages_count = 1
        while page_number < pages_count:

            hh_api = f'https://api.hh.ru/vacancies?text={search_query.replace(" ", "&")}&' \
                     f'description={keywords.replace(" ", "&")}&area=1&page={page_number}&per_page=100'

            response = requests.get(hh_api, headers={"User-Agent": "K_ParserApp/1.0"})
            response_json = response.json()
            file_write_jobs = 'hh_jobs.json'

            if len(response_json["items"]) == 0:
                time.sleep(0.25)
                break
            else:
                with open(file_write_jobs, 'a', encoding="utf-8") as add_file:
                    if os.stat(file_write_jobs).st_size == 0:
                        json.dump(response_json["items"], add_file, indent=4)
                        add_file.close()
                        if len(response_json["items"]) < top_vacancies:
                            pages_count +=1

                    else:
                        with open(file_write_jobs, encoding="utf-8") as json_file_read:
                            content = json.load(json_file_read)
                            json_file_read.close()
                            for vacancy in response_json["items"]:
                                content.append(vacancy)

                        with open(file_write_jobs, "w", encoding="utf-8") as json_file_write:
                            json.dump(content, json_file_write, indent=4)
                            json_file_write.close()

                    page_number += 1
                    time.sleep(0.25)
            print(f"LOADING: 50 %")


class SuperJobAPI(SiteAPI):
    def get_vacancies(self, search_query: str, keywords: str, top_vacancies: int):
        headers = {"X-Api-App-Id": 'v3.h.4470305.34df124d3610ceb6323baf8548815788c0c9031b.7a728b4d5c84b82bb14e5899a8991fdfe0fbff53'}
        superjob_api = 'https://api.superjob.ru/2.0/vacancies'

        page_number = 0
        pages_count = 1

        while page_number < pages_count:

            response = requests.get(superjob_api, headers= headers, params= f"keyword={search_query.replace(' ', '&')}"
                                                                          f"{keywords.replace(' ', '&')}"
                                                                          f"&page={page_number}"
                                                                          f"&count=100")


            response_json = response.json()

            file_write_jobs = 'sj_jobs.json'


            if len(response_json["objects"]) == 0:
                time.sleep(0.25)
                break

            else:
                with open(file_write_jobs, 'a', encoding="utf-8") as add_file:
                    if os.stat(file_write_jobs).st_size == 0:
                        json.dump(response_json["objects"], add_file, indent=4)
                        add_file.close()

                        if len(response_json["objects"]) < top_vacancies:
                            pages_count += 1
                    else:
                        with open(file_write_jobs, encoding="utf-8") as json_file_read:
                            content = json.load(json_file_read)
                            json_file_read.close()
                            for vacancy in response_json["objects"]:
                                content.append(vacancy)

                        with open(file_write_jobs, "w", encoding="utf-8") as json_file_write:
                            json.dump(content, json_file_write, indent=4)
                            json_file_write.close()

                    page_number += 1
                    time.sleep(0.25)

        print(f"LOADING: 100 %")
        time.sleep(0.25)

