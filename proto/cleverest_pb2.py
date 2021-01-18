# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cleverest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cleverest.proto',
  package='cleverest',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63leverest.proto\x12\tcleverest\"\x07\n\x05\x45mpty\"%\n\x11\x43onnectionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\".\n\x06Status\x12\r\n\x05is_ok\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"K\n\x12\x43onnectionResponse\x12\x12\n\nuser_token\x18\x01 \x01(\t\x12!\n\x06status\x18\x02 \x01(\x0b\x32\x11.cleverest.Status\"M\n\x10QuestionResponse\x12\x17\n\x0fnumber_question\x18\x01 \x01(\x05\x12\x10\n\x08question\x18\x02 \x01(\t\x12\x0e\n\x06\x41nswer\x18\x03 \x03(\t\"/\n\x0fSendUserAnswers\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\"B\n\x0bUserResults\x12\x0e\n\x06result\x18\x01 \x03(\t\x12\x0f\n\x07\x61nswers\x18\x02 \x03(\t\x12\x12\n\npercentage\x18\x03 \x01(\t\"\x1f\n\x0fLoadUserRanking\x12\x0c\n\x04user\x18\x01 \x01(\t\"8\n\x11ReturnUserRanking\x12\r\n\x05score\x18\x01 \x01(\t\x12\x14\n\x0cscoreOverall\x18\x02 \x01(\t\"\xc5\x01\n\x06\x41\x63tion\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x31\n\x0b\x61\x63tion_type\x18\x02 \x01(\x0e\x32\x1c.cleverest.Action.ActionType\x12\x0f\n\x07payload\x18\x03 \x01(\t\"e\n\nActionType\x12\x0b\n\x07\x43ONNECT\x10\x00\x12\x0e\n\nDISCONNECT\x10\x01\x12\x13\n\x0f\x41NSWER_QUESTION\x10\x02\x12\x10\n\x0c\x43HECK_ANSWER\x10\x03\x12\x13\n\x0fGET_USER_RATING\x10\x04\x32\xef\x02\n\tCleverest\x12I\n\nConnection\x12\x1c.cleverest.ConnectionRequest\x1a\x1d.cleverest.ConnectionResponse\x12\x46\n\x0b\x41skQuestion\x12\x1b.cleverest.QuestionResponse\x1a\x1a.cleverest.SendUserAnswers\x12\x45\n\x0f\x43heckUserAnswer\x12\x1a.cleverest.SendUserAnswers\x1a\x16.cleverest.UserResults\x12L\n\x10\x43heckUserRanking\x12\x1a.cleverest.LoadUserRanking\x1a\x1c.cleverest.ReturnUserRanking\x12:\n\x0fget_game_stream\x12\x10.cleverest.Empty\x1a\x11.cleverest.Action\"\x00\x30\x01\x62\x06proto3'
)



_ACTION_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='cleverest.Action.ActionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONNECT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISCONNECT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANSWER_QUESTION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHECK_ANSWER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GET_USER_RATING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=587,
  serialized_end=688,
)
_sym_db.RegisterEnumDescriptor(_ACTION_ACTIONTYPE)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='cleverest.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=30,
  serialized_end=37,
)


_CONNECTIONREQUEST = _descriptor.Descriptor(
  name='ConnectionRequest',
  full_name='cleverest.ConnectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='cleverest.ConnectionRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=39,
  serialized_end=76,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='cleverest.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_ok', full_name='cleverest.Status.is_ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='cleverest.Status.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=78,
  serialized_end=124,
)


_CONNECTIONRESPONSE = _descriptor.Descriptor(
  name='ConnectionResponse',
  full_name='cleverest.ConnectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_token', full_name='cleverest.ConnectionResponse.user_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='cleverest.ConnectionResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=126,
  serialized_end=201,
)


_QUESTIONRESPONSE = _descriptor.Descriptor(
  name='QuestionResponse',
  full_name='cleverest.QuestionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_question', full_name='cleverest.QuestionResponse.number_question', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='question', full_name='cleverest.QuestionResponse.question', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Answer', full_name='cleverest.QuestionResponse.Answer', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=203,
  serialized_end=280,
)


_SENDUSERANSWERS = _descriptor.Descriptor(
  name='SendUserAnswers',
  full_name='cleverest.SendUserAnswers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer', full_name='cleverest.SendUserAnswers.answer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='cleverest.SendUserAnswers.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=282,
  serialized_end=329,
)


_USERRESULTS = _descriptor.Descriptor(
  name='UserResults',
  full_name='cleverest.UserResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='cleverest.UserResults.result', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='answers', full_name='cleverest.UserResults.answers', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='percentage', full_name='cleverest.UserResults.percentage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=331,
  serialized_end=397,
)


_LOADUSERRANKING = _descriptor.Descriptor(
  name='LoadUserRanking',
  full_name='cleverest.LoadUserRanking',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='cleverest.LoadUserRanking.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=399,
  serialized_end=430,
)


_RETURNUSERRANKING = _descriptor.Descriptor(
  name='ReturnUserRanking',
  full_name='cleverest.ReturnUserRanking',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='cleverest.ReturnUserRanking.score', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scoreOverall', full_name='cleverest.ReturnUserRanking.scoreOverall', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=432,
  serialized_end=488,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='cleverest.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='cleverest.Action.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action_type', full_name='cleverest.Action.action_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='cleverest.Action.payload', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACTION_ACTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=491,
  serialized_end=688,
)

_CONNECTIONRESPONSE.fields_by_name['status'].message_type = _STATUS
_ACTION.fields_by_name['action_type'].enum_type = _ACTION_ACTIONTYPE
_ACTION_ACTIONTYPE.containing_type = _ACTION
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['ConnectionRequest'] = _CONNECTIONREQUEST
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['ConnectionResponse'] = _CONNECTIONRESPONSE
DESCRIPTOR.message_types_by_name['QuestionResponse'] = _QUESTIONRESPONSE
DESCRIPTOR.message_types_by_name['SendUserAnswers'] = _SENDUSERANSWERS
DESCRIPTOR.message_types_by_name['UserResults'] = _USERRESULTS
DESCRIPTOR.message_types_by_name['LoadUserRanking'] = _LOADUSERRANKING
DESCRIPTOR.message_types_by_name['ReturnUserRanking'] = _RETURNUSERRANKING
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.Empty)
  })
_sym_db.RegisterMessage(Empty)

ConnectionRequest = _reflection.GeneratedProtocolMessageType('ConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONREQUEST,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.ConnectionRequest)
  })
_sym_db.RegisterMessage(ConnectionRequest)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.Status)
  })
_sym_db.RegisterMessage(Status)

ConnectionResponse = _reflection.GeneratedProtocolMessageType('ConnectionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONRESPONSE,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.ConnectionResponse)
  })
_sym_db.RegisterMessage(ConnectionResponse)

QuestionResponse = _reflection.GeneratedProtocolMessageType('QuestionResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONRESPONSE,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.QuestionResponse)
  })
_sym_db.RegisterMessage(QuestionResponse)

SendUserAnswers = _reflection.GeneratedProtocolMessageType('SendUserAnswers', (_message.Message,), {
  'DESCRIPTOR' : _SENDUSERANSWERS,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.SendUserAnswers)
  })
_sym_db.RegisterMessage(SendUserAnswers)

UserResults = _reflection.GeneratedProtocolMessageType('UserResults', (_message.Message,), {
  'DESCRIPTOR' : _USERRESULTS,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.UserResults)
  })
_sym_db.RegisterMessage(UserResults)

LoadUserRanking = _reflection.GeneratedProtocolMessageType('LoadUserRanking', (_message.Message,), {
  'DESCRIPTOR' : _LOADUSERRANKING,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.LoadUserRanking)
  })
_sym_db.RegisterMessage(LoadUserRanking)

ReturnUserRanking = _reflection.GeneratedProtocolMessageType('ReturnUserRanking', (_message.Message,), {
  'DESCRIPTOR' : _RETURNUSERRANKING,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.ReturnUserRanking)
  })
_sym_db.RegisterMessage(ReturnUserRanking)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.Action)
  })
_sym_db.RegisterMessage(Action)



_CLEVEREST = _descriptor.ServiceDescriptor(
  name='Cleverest',
  full_name='cleverest.Cleverest',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=691,
  serialized_end=1058,
  methods=[
  _descriptor.MethodDescriptor(
    name='Connection',
    full_name='cleverest.Cleverest.Connection',
    index=0,
    containing_service=None,
    input_type=_CONNECTIONREQUEST,
    output_type=_CONNECTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AskQuestion',
    full_name='cleverest.Cleverest.AskQuestion',
    index=1,
    containing_service=None,
    input_type=_QUESTIONRESPONSE,
    output_type=_SENDUSERANSWERS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckUserAnswer',
    full_name='cleverest.Cleverest.CheckUserAnswer',
    index=2,
    containing_service=None,
    input_type=_SENDUSERANSWERS,
    output_type=_USERRESULTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckUserRanking',
    full_name='cleverest.Cleverest.CheckUserRanking',
    index=3,
    containing_service=None,
    input_type=_LOADUSERRANKING,
    output_type=_RETURNUSERRANKING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_game_stream',
    full_name='cleverest.Cleverest.get_game_stream',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_ACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLEVEREST)

DESCRIPTOR.services_by_name['Cleverest'] = _CLEVEREST

# @@protoc_insertion_point(module_scope)
