# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='rpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rmessage.proto\x12\x03rpc\"#\n\x07Payload\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x32\x33\n\x05\x46\x65tch\x12*\n\nCapitalize\x12\x0c.rpc.Payload\x1a\x0c.rpc.Payload\"\x00\x62\x06proto3')
)




_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='rpc.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rpc.Payload.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='rpc.Payload.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=57,
)

DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
  DESCRIPTOR = _PAYLOAD,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Payload)
  ))
_sym_db.RegisterMessage(Payload)



_FETCH = _descriptor.ServiceDescriptor(
  name='Fetch',
  full_name='rpc.Fetch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=59,
  serialized_end=110,
  methods=[
  _descriptor.MethodDescriptor(
    name='Capitalize',
    full_name='rpc.Fetch.Capitalize',
    index=0,
    containing_service=None,
    input_type=_PAYLOAD,
    output_type=_PAYLOAD,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FETCH)

DESCRIPTOR.services_by_name['Fetch'] = _FETCH

# @@protoc_insertion_point(module_scope)
