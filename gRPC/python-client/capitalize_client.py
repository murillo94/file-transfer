import sys
sys.path.insert(0, '..')

import message_pb2
import message_pb2_grpc
import grpc

def main():
    channel = grpc.insecure_channel('localhost:9778')
    stub = message_pb2_grpc.FetchStub(channel)

    while True:
        lineIn = input('> ')
        capitalized = stub.Capitalize(message_pb2.Payload(
            data=bytes(lineIn, encoding='utf-8')))
        print('< %s\n' % (capitalized.data.decode('utf-8')))


if __name__ == '__main__':
    main()
