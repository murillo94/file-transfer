# gRPC

## Running it locally

First, you need to install `grpcio-tools`

```
python3 -m pip install grpcio-tools
```

### Server

Go to `python-server` folder and run `python3 capitalize_server.py`

### Client

#### Node

Go to `node-client` folder and run `npm i` and `node capitalize_client.js`

#### Python

Go to `python-client` folder and run `python3 capitalize_client.py`

#### Kotlin

Go to `android-client` and follow the instructions.

## Important

If for some reason you need to generete new ones gRPC stubs, run:

#### Python

```
python3 -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/message.proto
```

#### Node

The client in node uses [Protobuf.js](https://github.com/dcodeIO/ProtoBuf.js/) to serialize the code structure at runtime, so we don't need to create stubs statically.
