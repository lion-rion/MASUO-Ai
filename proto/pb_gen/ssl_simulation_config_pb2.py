"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import ssl_gc_common_pb2 as ssl__gc__common__pb2
from . import ssl_vision_geometry_pb2 as ssl__vision__geometry__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bssl_simulation_config.proto\x1a\x13ssl_gc_common.proto\x1a\x19ssl_vision_geometry.proto\x1a\x19google/protobuf/any.proto"\xc2\x01\n\x0bRobotLimits\x12 \n\x18acc_speedup_absolute_max\x18\x01 \x01(\x02\x12\x1f\n\x17acc_speedup_angular_max\x18\x02 \x01(\x02\x12\x1e\n\x16acc_brake_absolute_max\x18\x03 \x01(\x02\x12\x1d\n\x15acc_brake_angular_max\x18\x04 \x01(\x02\x12\x18\n\x10vel_absolute_max\x18\x05 \x01(\x02\x12\x17\n\x0fvel_angular_max\x18\x06 \x01(\x02"b\n\x10RobotWheelAngles\x12\x13\n\x0bfront_right\x18\x01 \x02(\x02\x12\x12\n\nback_right\x18\x02 \x02(\x02\x12\x11\n\tback_left\x18\x03 \x02(\x02\x12\x12\n\nfront_left\x18\x04 \x02(\x02"\xa1\x02\n\nRobotSpecs\x12\x14\n\x02id\x18\x01 \x02(\x0b2\x08.RobotId\x12\x14\n\x06radius\x18\x02 \x01(\x02:\x040.09\x12\x14\n\x06height\x18\x03 \x01(\x02:\x040.15\x12\x0c\n\x04mass\x18\x04 \x01(\x02\x12\x1d\n\x15max_linear_kick_speed\x18\x07 \x01(\x02\x12\x1b\n\x13max_chip_kick_speed\x18\x08 \x01(\x02\x12\x1a\n\x12center_to_dribbler\x18\t \x01(\x02\x12\x1c\n\x06limits\x18\n \x01(\x0b2\x0c.RobotLimits\x12\'\n\x0cwheel_angles\x18\r \x01(\x0b2\x11.RobotWheelAngles\x12$\n\x06custom\x18\x0e \x03(\x0b2\x14.google.protobuf.Any"5\n\rRealismConfig\x12$\n\x06custom\x18\x01 \x03(\x0b2\x14.google.protobuf.Any"\x95\x01\n\x0fSimulatorConfig\x12#\n\x08geometry\x18\x01 \x01(\x0b2\x11.SSL_GeometryData\x12 \n\x0brobot_specs\x18\x02 \x03(\x0b2\x0b.RobotSpecs\x12&\n\x0erealism_config\x18\x03 \x01(\x0b2\x0e.RealismConfig\x12\x13\n\x0bvision_port\x18\x04 \x01(\rB8Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim')
_ROBOTLIMITS = DESCRIPTOR.message_types_by_name['RobotLimits']
_ROBOTWHEELANGLES = DESCRIPTOR.message_types_by_name['RobotWheelAngles']
_ROBOTSPECS = DESCRIPTOR.message_types_by_name['RobotSpecs']
_REALISMCONFIG = DESCRIPTOR.message_types_by_name['RealismConfig']
_SIMULATORCONFIG = DESCRIPTOR.message_types_by_name['SimulatorConfig']
RobotLimits = _reflection.GeneratedProtocolMessageType('RobotLimits', (_message.Message,), {'DESCRIPTOR': _ROBOTLIMITS, '__module__': 'ssl_simulation_config_pb2'})
_sym_db.RegisterMessage(RobotLimits)
RobotWheelAngles = _reflection.GeneratedProtocolMessageType('RobotWheelAngles', (_message.Message,), {'DESCRIPTOR': _ROBOTWHEELANGLES, '__module__': 'ssl_simulation_config_pb2'})
_sym_db.RegisterMessage(RobotWheelAngles)
RobotSpecs = _reflection.GeneratedProtocolMessageType('RobotSpecs', (_message.Message,), {'DESCRIPTOR': _ROBOTSPECS, '__module__': 'ssl_simulation_config_pb2'})
_sym_db.RegisterMessage(RobotSpecs)
RealismConfig = _reflection.GeneratedProtocolMessageType('RealismConfig', (_message.Message,), {'DESCRIPTOR': _REALISMCONFIG, '__module__': 'ssl_simulation_config_pb2'})
_sym_db.RegisterMessage(RealismConfig)
SimulatorConfig = _reflection.GeneratedProtocolMessageType('SimulatorConfig', (_message.Message,), {'DESCRIPTOR': _SIMULATORCONFIG, '__module__': 'ssl_simulation_config_pb2'})
_sym_db.RegisterMessage(SimulatorConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim'
    _ROBOTLIMITS._serialized_start = 107
    _ROBOTLIMITS._serialized_end = 301
    _ROBOTWHEELANGLES._serialized_start = 303
    _ROBOTWHEELANGLES._serialized_end = 401
    _ROBOTSPECS._serialized_start = 404
    _ROBOTSPECS._serialized_end = 693
    _REALISMCONFIG._serialized_start = 695
    _REALISMCONFIG._serialized_end = 748
    _SIMULATORCONFIG._serialized_start = 751
    _SIMULATORCONFIG._serialized_end = 900