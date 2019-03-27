# gRPC

## Running it locally

#### Requirements

- [Python](https://www.python.org/) (latest)
- [Node.js](https://nodejs.org/) (latest)

First, you need to install `grpcio-tools`

```
python3 -m pip install grpcio-tools
```

And after

- to run the server, go to server folder and type: `python capitalize_server.py`

- to run the client, go to client folder and type: `npm install` and `node capitalize_client.js`

## Important

If for some reason you need to generete new ones gRPC stubs, run:

- Python

```
python3 -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/message.proto
```

- Node

The client in node uses [Protobuf.js](https://github.com/dcodeIO/ProtoBuf.js/) to serialize the code structure at runtime, so we don't need to create stubs statically.
