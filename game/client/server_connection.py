import grpc
import threading

from ..proto import game_pb2
from ..proto import game_pb2_grpc

class ServerConnection():
    def __init__(self, target):
        self.target = target
        self.channel = grpc.insecure_channel(self.target)
        self.stub = game_pb2_grpc.GameStub(self.channel)
        self.username = None
        print('Initialization')

    def connect_user (self, username):
        conn_resp = self.stub.connection(
            game_pb2.User(
                username=username))
        self.username = username
        print('Connected')
        return conn_resp.result

    def disconnect_user(self):
        result = self.stub.disconnection(
            game_pb2.User(
                username=self.username))
        self.username = None
        return result.result

    def answer_question (self, number_question, answer):
        result = self.stub.answer_question(
            game_pb2.AnswerRequest(
                number_question= number_question,
                username = self.username,
                user_answer = answer
            )
        )
        return result

    def get_result_table(self):
        result = self.stub.get_result_table(game_pb2.Empty())
        return result.total_rating;

    def actions_listener(self, callback):
        try:
            for action in self.stub.get_question_stream(game_pb2.Empty()):
                callback(action)
        except grpc._channel._MultiThreadedRendezvous:
            print('connection is closed')
            # connection is closed
            return

    def start_message_listener(self, callback):
        threading.Thread(
            target=self.actions_listener,
            args=(callback,)).start()

    def cleanup(self):
        if self.channel is not None:
            self.channel.close()

    def __del__(self):
        self.cleanup()


