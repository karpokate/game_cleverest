
from concurrent import futures
from datetime import datetime
import threading
import uuid
import json

import grpc
import pika
from loguru import logger

from ..proto import cleverest_pb2 as clever_pb2
from ..proto import cleverest_pb2_grpc as clever_pb2_grpc

class CleverestGame (cleverest_pb2_grpc.CleverestServicer):

    def answerQuestion(self):
        ''''''
        pass


def main ():
    pass





if __name__ == '__main__':
    main()