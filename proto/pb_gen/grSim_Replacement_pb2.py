"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17grSim_Replacement.proto"k\n\x16grSim_RobotReplacement\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\x0b\n\x03dir\x18\x03 \x02(\x01\x12\n\n\x02id\x18\x04 \x02(\r\x12\x12\n\nyellowteam\x18\x05 \x02(\x08\x12\x0e\n\x06turnon\x18\x06 \x01(\x08"E\n\x15grSim_BallReplacement\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\n\n\x02vx\x18\x03 \x01(\x01\x12\n\n\x02vy\x18\x04 \x01(\x01"b\n\x11grSim_Replacement\x12$\n\x04ball\x18\x01 \x01(\x0b2\x16.grSim_BallReplacement\x12\'\n\x06robots\x18\x02 \x03(\x0b2\x17.grSim_RobotReplacement')
_GRSIM_ROBOTREPLACEMENT = DESCRIPTOR.message_types_by_name['grSim_RobotReplacement']
_GRSIM_BALLREPLACEMENT = DESCRIPTOR.message_types_by_name['grSim_BallReplacement']
_GRSIM_REPLACEMENT = DESCRIPTOR.message_types_by_name['grSim_Replacement']
grSim_RobotReplacement = _reflection.GeneratedProtocolMessageType('grSim_RobotReplacement', (_message.Message,), {'DESCRIPTOR': _GRSIM_ROBOTREPLACEMENT, '__module__': 'grSim_Replacement_pb2'})
_sym_db.RegisterMessage(grSim_RobotReplacement)
grSim_BallReplacement = _reflection.GeneratedProtocolMessageType('grSim_BallReplacement', (_message.Message,), {'DESCRIPTOR': _GRSIM_BALLREPLACEMENT, '__module__': 'grSim_Replacement_pb2'})
_sym_db.RegisterMessage(grSim_BallReplacement)
grSim_Replacement = _reflection.GeneratedProtocolMessageType('grSim_Replacement', (_message.Message,), {'DESCRIPTOR': _GRSIM_REPLACEMENT, '__module__': 'grSim_Replacement_pb2'})
_sym_db.RegisterMessage(grSim_Replacement)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GRSIM_ROBOTREPLACEMENT._serialized_start = 27
    _GRSIM_ROBOTREPLACEMENT._serialized_end = 134
    _GRSIM_BALLREPLACEMENT._serialized_start = 136
    _GRSIM_BALLREPLACEMENT._serialized_end = 205
    _GRSIM_REPLACEMENT._serialized_start = 207
    _GRSIM_REPLACEMENT._serialized_end = 305