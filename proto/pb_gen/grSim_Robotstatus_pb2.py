"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17grSim_Robotstatus.proto"5\n\rRobots_Status\x12$\n\rrobots_status\x18\x01 \x03(\x0b2\r.Robot_Status"X\n\x0cRobot_Status\x12\x10\n\x08robot_id\x18\x01 \x02(\x05\x12\x10\n\x08infrared\x18\x02 \x02(\x08\x12\x11\n\tflat_kick\x18\x03 \x02(\x08\x12\x11\n\tchip_kick\x18\x04 \x02(\x08')
_ROBOTS_STATUS = DESCRIPTOR.message_types_by_name['Robots_Status']
_ROBOT_STATUS = DESCRIPTOR.message_types_by_name['Robot_Status']
Robots_Status = _reflection.GeneratedProtocolMessageType('Robots_Status', (_message.Message,), {'DESCRIPTOR': _ROBOTS_STATUS, '__module__': 'grSim_Robotstatus_pb2'})
_sym_db.RegisterMessage(Robots_Status)
Robot_Status = _reflection.GeneratedProtocolMessageType('Robot_Status', (_message.Message,), {'DESCRIPTOR': _ROBOT_STATUS, '__module__': 'grSim_Robotstatus_pb2'})
_sym_db.RegisterMessage(Robot_Status)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ROBOTS_STATUS._serialized_start = 27
    _ROBOTS_STATUS._serialized_end = 80
    _ROBOT_STATUS._serialized_start = 82
    _ROBOT_STATUS._serialized_end = 170