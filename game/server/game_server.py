from concurrent import futures
import threading

import grpc

from ..proto import game_pb2
from ..proto import game_pb2_grpc
import pika
# from loguru import logger
import json
from  datetime import datetime


class GameServicer (game_pb2_grpc.GameServicer):
    def __init__(self):

        self.questions = [
            {'question':'How much planets?', 'answer':['9','2','39','8'], 'correct_answer':0},
            {'question':'How much 2+3?', 'answer':['3','10','4','5'], 'correct_answer':3},
            {'question':'How we can translate love to German?','answer':['Kiss','Deutsch','Liebe','Love'], 'correct_answer':2},
            {'question': 'END_SIGNAL', 'answer': [], 'correct_answer': 0}
        ]

        self.users = {}
        self.current_question = 0

        self.new_question_event = threading.Event()
        self.queue_name = 'game_events'
        self.rabbit_connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.rabbit_channel = self.rabbit_connection.channel()
        self.rabbit_channel.queue_declare(queue=self.queue_name)

    # method: add action to rabbitmq => to db
    def add_to_rabbit_action(self, username,action_string,payload=''):
        self.rabbit_channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body = json.dumps({
                'time': datetime.now().timestamp(),
                'username': username,
                'action_string': action_string,
                # user answer (only one digit)
                'payload':payload

            })
        )

    def connection(self, request, context):
        if request.username in self.users:
            print('User with username {} already on server'.format(request.username))
            self.add_to_rabbit_action(
                request.username,
                'User already on server.'
            )
            return game_pb2.Status(result=False)
        else:
            self.users[request.username] = 0
            print('User with username {} connected'.format(request.username))
            self.add_to_rabbit_action(
                request.username,
                'Connected to game.'
            )
            return game_pb2.Status(result=True)

    def disconnection(self, request, context):
        if request.username in self.users:
            del self.users[request.username]
            print('User {} disconnected'.format(request.username))
            self.add_to_rabbit_action(
                request.username,
                'Disconnected from game.'
            )
            return game_pb2.Status(result=True)
        else:
            print('Disconnect error. username {}'.format(request.username))
            self.add_to_rabbit_action(
                request.username,
                'Disconnect error.'
            )
            return game_pb2.Status(result=False)

    def answer_question(self, request, context):
        print('Request', request)
        if self.questions[request.number_question]['correct_answer'] == request.user_answer:
            self.users[request.username] += 1
            self.current_question += 1
            self.new_question_event.set()
            print('Correct answer on {} question, username {}, user answer {}'.format(request.number_question,request.username,request.user_answer))
            self.add_to_rabbit_action(
                request.username,
                'User answered correct.',
                request.user_answer
            )
            return game_pb2.AnswerResponse(answer_score=True, rating = self.users[request.username])
        else:
            print('Incorrect answer: question {} username {} user answer {}'.format(request.number_question,request.username,request.user_answer))
            self.add_to_rabbit_action(
                request.username,
                'User answered incorrect.Waiting for someone else answer (should be correct, then give new one)',
                request.user_answer
            )
            # self.current_question = request.number_question #номер текущего вопроса
            return game_pb2.AnswerResponse(answer_score=False, rating = self.users[request.username])

    def get_result_table(self, request, context):
        table = ''
        i = 0
        for user, score in sorted(self.users.items(), key=lambda item: item[1]):
            table += '{}) {} with score {}\n'.format(i, user, score)
            i += 1
        return game_pb2.TotalRating(total_rating=table)

    def get_question_stream(self, request, context):
        print('Now you will receive your first question')
        yield game_pb2.Question(number_question = self.current_question,
                                text_question = self.questions[self.current_question]['question'],
                                answers = self.questions[self.current_question]['answer'],
                                correct_answer =  self.questions[self.current_question]['correct_answer'])
        while True :
            print('Waiting for correct answer')
            self.new_question_event.wait()
            print('New question sending with id {}'.format(self.current_question))
            print(self.questions)
            print(
                self.current_question,
                self.questions[self.current_question]['question'],
                self.questions[self.current_question]['answer'],
                self.questions[self.current_question]['correct_answer']
            )
            to_send = game_pb2.Question(
                number_question = self.current_question,
                text_question = self.questions[self.current_question]['question'],
                answers = self.questions[self.current_question]['answer'],
                correct_answer =  self.questions[self.current_question]['correct_answer']
            )
            # to_send = game_pb2.Question(
            #     number_question=1,
            #     text_question='WHo are you?',
            #     answers=['human', 'ai', 'animal', 'god'],
            #     correct_answer=3
            # )
            print('To send:', to_send)
            yield to_send
            self.new_question_event.clear()

    def cleanup(self):
        self.rabbit_connection.close()

    def __del__(self):
        self.cleanup()



def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    game_pb2_grpc.add_GameServicer_to_server(GameServicer(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    # print(datetime.now().timestamp())
    print('Server started at port 8080')
    server.wait_for_termination()


if __name__ == '__main__':
    server()
