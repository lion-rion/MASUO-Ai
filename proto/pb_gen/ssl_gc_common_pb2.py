"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13ssl_gc_common.proto"*\n\x07RobotId\x12\n\n\x02id\x18\x01 \x01(\r\x12\x13\n\x04team\x18\x02 \x01(\x0e2\x05.Team*)\n\x04Team\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06YELLOW\x10\x01\x12\x08\n\x04BLUE\x10\x02*1\n\x08Division\x12\x0f\n\x0bDIV_UNKNOWN\x10\x00\x12\t\n\x05DIV_A\x10\x01\x12\t\n\x05DIV_B\x10\x02B8Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim')
_TEAM = DESCRIPTOR.enum_types_by_name['Team']
Team = enum_type_wrapper.EnumTypeWrapper(_TEAM)
_DIVISION = DESCRIPTOR.enum_types_by_name['Division']
Division = enum_type_wrapper.EnumTypeWrapper(_DIVISION)
UNKNOWN = 0
YELLOW = 1
BLUE = 2
DIV_UNKNOWN = 0
DIV_A = 1
DIV_B = 2
_ROBOTID = DESCRIPTOR.message_types_by_name['RobotId']
RobotId = _reflection.GeneratedProtocolMessageType('RobotId', (_message.Message,), {'DESCRIPTOR': _ROBOTID, '__module__': 'ssl_gc_common_pb2'})
_sym_db.RegisterMessage(RobotId)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim'
    _TEAM._serialized_start = 67
    _TEAM._serialized_end = 108
    _DIVISION._serialized_start = 110
    _DIVISION._serialized_end = 159
    _ROBOTID._serialized_start = 23
    _ROBOTID._serialized_end = 65