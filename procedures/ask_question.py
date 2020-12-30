# как должна выглядеть игра:
# 1) игра начинается - выбираем 10 рандомных вопросов
# 2) пользователи отвечают на эти вопросы, у кого больше правильных ответов - тот и выиграл
# => 10 балов - максимальное количество балов за игру


# для начала реализуем только для генерации вопроса и получения ответа

import json
import random
'''Процедура которую хотим вызывать удаленно.
Получение n-количества вопросов от ведущего (вопросы берем из json файла)'''

def get_data_from_json(json_file_path):
    with open(json_file_path) as read_file:
        data = json.load(read_file)
        return data



def generate_random_questions_indexes(len_of_data_dict,question_pull_size):
    index_list = []
    for i in range(0,question_pull_size):
        number_questio= random.randint(0,len_of_data_dict)
        if number_questio not in index_list:
            index_list.append(number_questio)
    return index_list


def form_question_list(game_pull_size):
    data = get_data_from_json('../questions_storage/questions_bank.json')
    index_list_questions = generate_random_questions_indexes(len(data),game_pull_size)
    for i in range(len(index_list_questions)):
        random_question_struct = data.get(str(index_list_questions[i]))
        question = random_question_struct.get('question')
        answers_list = random_question_struct.get('answers_list')
        random.shuffle(answers_list)
        correct_answer = random_question_struct.get('correct_answer')
        print(question, answers_list, correct_answer)


if __name__ == '__main__':
    form_question_list(10)

