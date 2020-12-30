import json
import random



# для начала реализуем только для генерации вопроса и получения ответа
def get_data_from_json(json_file_path):
    with open(json_file_path) as read_file:
        data = json.load(read_file)
        return data




def generate_random_question_index(len_of_data_dict):
    number_question = random.randint(0,len_of_data_dict)
    return number_question


def generate_question ():
    data = get_data_from_json('../questions_storage/questions_bank.json')
    question_index = generate_random_question_index(len(data))
    random_question_struct = data.get(str(question_index))
    question = random_question_struct.get('question')
    answers_list = random_question_struct.get('answers_list')
    random.shuffle(answers_list)
    correct_answer = random_question_struct.get('correct_answer')
    return question_index, question, answers_list



def main():
    question = generate_question()
    print(question)

if __name__ == '__main__':
    main()