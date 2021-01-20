import time, threading
from game.client.server_connection import ServerConnection


connection = None
current_question = 0
is_end = threading.Event()

def new_question(question):
    if question.text_question == 'END_SIGNAL':
        global is_end
        is_end.set()
        return

    global current_question
    current_question = question.number_question
    print ('{}. QUESTION {}'.format(question.number_question, question.text_question))
    print('CHOOSE ONLY ONE CORRECT ANSWER \n '
          'A. {} \n B. {} \n C. {} \n D. {}'.format(
        question.answers[0],question.answers[1],question.answers[2],
        question.answers[3]
    ))
    print('Enter your answer: ', end='', flush=True)



def answer_question():
    global connection
    global current_question

    while True:

        answer = int(input(''))
        resp = connection.answer_question(
            number_question=current_question,
            answer=answer)

        if resp.answer_score == True:
            print('You are right!')
        else:
            print('You are wrong!')

        print('Your rating is', resp.rating)



def main():
    global  connection
    connection = ServerConnection(target='localhost:8080')
    username = input('Enter your username: ')
    connection.connect_user(username=username)
    connection.start_message_listener(new_question)
    time.sleep(0.5)
    answer_thread = threading.Thread(
        target=answer_question,
    )
    answer_thread.start()

    global is_end
    is_end.wait()
    print()
    print('====[ Leaderboard ]====')
    print(connection.get_result_table())



if __name__ == '__main__':
    main()

