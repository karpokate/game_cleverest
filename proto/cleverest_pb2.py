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
  serialized_pb=b'\n\x0f\x63leverest.proto\x12\tcleverest\"\x11\n\x0fQuestionRequest\"4\n\x10QuestionResponse\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x0e\n\x06\x61nswer\x18\x02 \x01(\t\"\x13\n\x11LoadQuestionsList\";\n\x13ReturnQuestionsList\x12$\n\x06result\x18\x01 \x03(\x0b\x32\x14.cleverest.Questions\"?\n\tQuestions\x12\x10\n\x08Question\x18\x02 \x01(\t\x12\x0f\n\x07\x43orrect\x18\x03 \x01(\t\x12\x0f\n\x07\x41nswers\x18\x04 \x03(\t\"0\n\x0fSendUserAnswers\x12\x0f\n\x07\x61nswers\x18\x01 \x03(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\"B\n\x0bUserResults\x12\x0e\n\x06result\x18\x01 \x03(\t\x12\x0f\n\x07\x61nswers\x18\x02 \x03(\t\x12\x12\n\npercentage\x18\x03 \x01(\t\"\x1f\n\x0fLoadUserRanking\x12\x0c\n\x04user\x18\x01 \x01(\t\"8\n\x11ReturnUserRanking\x12\r\n\x05score\x18\x01 \x01(\t\x12\x14\n\x0cscoreOverall\x18\x02 \x01(\t2\xb9\x02\n\tCleverest\x12O\n\x0fGetAllQuestions\x12\x1c.cleverest.LoadQuestionsList\x1a\x1e.cleverest.ReturnQuestionsList\x12\x46\n\x0b\x41skQuestion\x12\x1a.cleverest.QuestionRequest\x1a\x1b.cleverest.QuestionResponse\x12\x45\n\x0f\x43heckUserAnswer\x12\x1a.cleverest.SendUserAnswers\x1a\x16.cleverest.UserResults\x12L\n\x10\x43heckUserRanking\x12\x1a.cleverest.LoadUserRanking\x1a\x1c.cleverest.ReturnUserRankingb\x06proto3'
)




_QUESTIONREQUEST = _descriptor.Descriptor(
  name='QuestionRequest',
  full_name='cleverest.QuestionRequest',
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
  serialized_end=47,
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
      name='question', full_name='cleverest.QuestionResponse.question', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='answer', full_name='cleverest.QuestionResponse.answer', index=1,
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
  serialized_start=49,
  serialized_end=101,
)


_LOADQUESTIONSLIST = _descriptor.Descriptor(
  name='LoadQuestionsList',
  full_name='cleverest.LoadQuestionsList',
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
  serialized_start=103,
  serialized_end=122,
)


_RETURNQUESTIONSLIST = _descriptor.Descriptor(
  name='ReturnQuestionsList',
  full_name='cleverest.ReturnQuestionsList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='cleverest.ReturnQuestionsList.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=124,
  serialized_end=183,
)


_QUESTIONS = _descriptor.Descriptor(
  name='Questions',
  full_name='cleverest.Questions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Question', full_name='cleverest.Questions.Question', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Correct', full_name='cleverest.Questions.Correct', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Answers', full_name='cleverest.Questions.Answers', index=2,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=185,
  serialized_end=248,
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
      name='answers', full_name='cleverest.SendUserAnswers.answers', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=250,
  serialized_end=298,
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
  serialized_start=300,
  serialized_end=366,
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
  serialized_start=368,
  serialized_end=399,
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
  serialized_start=401,
  serialized_end=457,
)

_RETURNQUESTIONSLIST.fields_by_name['result'].message_type = _QUESTIONS
DESCRIPTOR.message_types_by_name['QuestionRequest'] = _QUESTIONREQUEST
DESCRIPTOR.message_types_by_name['QuestionResponse'] = _QUESTIONRESPONSE
DESCRIPTOR.message_types_by_name['LoadQuestionsList'] = _LOADQUESTIONSLIST
DESCRIPTOR.message_types_by_name['ReturnQuestionsList'] = _RETURNQUESTIONSLIST
DESCRIPTOR.message_types_by_name['Questions'] = _QUESTIONS
DESCRIPTOR.message_types_by_name['SendUserAnswers'] = _SENDUSERANSWERS
DESCRIPTOR.message_types_by_name['UserResults'] = _USERRESULTS
DESCRIPTOR.message_types_by_name['LoadUserRanking'] = _LOADUSERRANKING
DESCRIPTOR.message_types_by_name['ReturnUserRanking'] = _RETURNUSERRANKING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestionRequest = _reflection.GeneratedProtocolMessageType('QuestionRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONREQUEST,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.QuestionRequest)
  })
_sym_db.RegisterMessage(QuestionRequest)

QuestionResponse = _reflection.GeneratedProtocolMessageType('QuestionResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONRESPONSE,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.QuestionResponse)
  })
_sym_db.RegisterMessage(QuestionResponse)

LoadQuestionsList = _reflection.GeneratedProtocolMessageType('LoadQuestionsList', (_message.Message,), {
  'DESCRIPTOR' : _LOADQUESTIONSLIST,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.LoadQuestionsList)
  })
_sym_db.RegisterMessage(LoadQuestionsList)

ReturnQuestionsList = _reflection.GeneratedProtocolMessageType('ReturnQuestionsList', (_message.Message,), {
  'DESCRIPTOR' : _RETURNQUESTIONSLIST,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.ReturnQuestionsList)
  })
_sym_db.RegisterMessage(ReturnQuestionsList)

Questions = _reflection.GeneratedProtocolMessageType('Questions', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONS,
  '__module__' : 'cleverest_pb2'
  # @@protoc_insertion_point(class_scope:cleverest.Questions)
  })
_sym_db.RegisterMessage(Questions)

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



_CLEVEREST = _descriptor.ServiceDescriptor(
  name='Cleverest',
  full_name='cleverest.Cleverest',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=460,
  serialized_end=773,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllQuestions',
    full_name='cleverest.Cleverest.GetAllQuestions',
    index=0,
    containing_service=None,
    input_type=_LOADQUESTIONSLIST,
    output_type=_RETURNQUESTIONSLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AskQuestion',
    full_name='cleverest.Cleverest.AskQuestion',
    index=1,
    containing_service=None,
    input_type=_QUESTIONREQUEST,
    output_type=_QUESTIONRESPONSE,
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
])
_sym_db.RegisterServiceDescriptor(_CLEVEREST)

DESCRIPTOR.services_by_name['Cleverest'] = _CLEVEREST

# @@protoc_insertion_point(module_scope)