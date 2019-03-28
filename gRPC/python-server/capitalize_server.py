import sys
sys.path.insert(0, '..')

from concurrent import futures
import time

import grpc

import message_pb2_grpc
import message_pb2


class Capitalize(message_pb2_grpc.FetchServicer):

    def Capitalize(self, request, context):
        print('Received and Sending...')
        return message_pb2.Payload(data=request.data.upper())


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_FetchServicer_to_server(Capitalize(), server)
    server.add_insecure_port('[::]:9778')
    server.start()

    try:
        while True:
            time.sleep(60 * 60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()
