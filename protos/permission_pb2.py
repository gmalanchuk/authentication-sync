# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/permission.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17protos/permission.proto\x12\npermission\"\"\n\x11PermissionRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\"\n\x12PermissionResponse\x12\x0c\n\x04role\x18\x01 \x01(\t2`\n\nPermission\x12R\n\x0f\x43heckPermission\x12\x1d.permission.PermissionRequest\x1a\x1e.permission.PermissionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.permission_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PERMISSIONREQUEST']._serialized_start=39
  _globals['_PERMISSIONREQUEST']._serialized_end=73
  _globals['_PERMISSIONRESPONSE']._serialized_start=75
  _globals['_PERMISSIONRESPONSE']._serialized_end=109
  _globals['_PERMISSION']._serialized_start=111
  _globals['_PERMISSION']._serialized_end=207
# @@protoc_insertion_point(module_scope)
