# при использовании нужно шуфлетить варианты ответов

from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import json

def main():
    '''method should write json file: number_q,question,answers_list, correct_answer'''

    result_dict ={}
    url_from = 'https://baza-otvetov.ru/categories/view/1/{}'
    driver = webdriver.Chrome(executable_path='/Users/kate/PycharmProjects/cleverest/questions_storage/chromedriver 2')

    for index in range(0,2501,10):
        driver.get(url_from.format(index))
        html_page = driver.page_source
        data = []
        soup = bs(html_page, 'lxml')
        table = soup.find('table', attrs={'class': 'q-list__table'})
        table_body = table.find('tbody')
        # print(table_body)

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        for i in range(1,11):
            col_names = ['number_q', 'question', 'answers_list',
                         'correct_answer']  # по дефолту последний ответ в списке - правильный
            single_question = data[i]
            answers = single_question[1].split('\n\n\t\t\t\t\t\t\t\t')[1].split('Ответы для викторин: ')[1].split(',')
            answers.append(single_question[2])
            single_dict = {col_names[0]:single_question[0],
                           col_names[1]: single_question[1].split('\n\n\t\t\t\t\t\t\t\t')[0],
                           col_names[2]:answers,
                           col_names[3]:single_question[2]}

            result_dict[str(single_question[0])] = single_dict
    print(result_dict)
    with open('questions_bank.json', 'w') as fp:
        json.dump(result_dict, fp)






if __name__ == '__main__':
    main()