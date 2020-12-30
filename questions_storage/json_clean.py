import json


with open('questions_bank.json') as read_data:
    result_dict = {}
    data = json.load(read_data)
    for i in range(1,len(data)+1): #(1,len(data)+1):
        col_names = ['number_q', 'question', 'answers_list',
                     'correct_answer']  # по дефолту последний ответ в списке - правильный
        single_question_dict = data.get(str(i))
        answers_l = single_question_dict.get('answers_list')

        answers_l = [i.replace(' ','') if i[0]==' '  else i for i in answers_l if answers_l]
        print(answers_l)
        single_dict = {col_names[0]: single_question_dict.get('number_q'),
                       col_names[1]: single_question_dict.get(col_names[1]),
                       col_names[2]: answers_l,
                       col_names[3]: single_question_dict.get(col_names[3])}

        result_dict[str(single_question_dict.get(col_names[0]))] = single_dict
    # print(result_dict)

