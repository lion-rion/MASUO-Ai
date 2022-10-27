"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import ssl_gc_common_pb2 as ssl__gc__common__pb2
from . import ssl_simulation_config_pb2 as ssl__simulation__config__pb2
from . import ssl_simulation_error_pb2 as ssl__simulation__error__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cssl_simulation_control.proto\x1a\x13ssl_gc_common.proto\x1a\x1bssl_simulation_config.proto\x1a\x1assl_simulation_error.proto"\xa1\x01\n\x0cTeleportBall\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\n\n\x02vx\x18\x04 \x01(\x02\x12\n\n\x02vy\x18\x05 \x01(\x02\x12\n\n\x02vz\x18\x06 \x01(\x02\x12\x1e\n\x0fteleport_safely\x18\x07 \x01(\x08:\x05false\x12\x13\n\x04roll\x18\x08 \x01(\x08:\x05false\x12\x17\n\x08by_force\x18\t \x01(\x08:\x05false"\xb0\x01\n\rTeleportRobot\x12\x14\n\x02id\x18\x01 \x02(\x0b2\x08.RobotId\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\x13\n\x0borientation\x18\x04 \x01(\x02\x12\x0e\n\x03v_x\x18\x05 \x01(\x02:\x010\x12\x0e\n\x03v_y\x18\x06 \x01(\x02:\x010\x12\x14\n\tv_angular\x18\x07 \x01(\x02:\x010\x12\x0f\n\x07present\x18\x08 \x01(\x08\x12\x17\n\x08by_force\x18\t \x01(\x08:\x05false"z\n\x10SimulatorControl\x12$\n\rteleport_ball\x18\x01 \x01(\x0b2\r.TeleportBall\x12&\n\x0eteleport_robot\x18\x02 \x03(\x0b2\x0e.TeleportRobot\x12\x18\n\x10simulation_speed\x18\x03 \x01(\x02"X\n\x10SimulatorCommand\x12"\n\x07control\x18\x01 \x01(\x0b2\x11.SimulatorControl\x12 \n\x06config\x18\x02 \x01(\x0b2\x10.SimulatorConfig"4\n\x11SimulatorResponse\x12\x1f\n\x06errors\x18\x01 \x03(\x0b2\x0f.SimulatorErrorB8Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim')
_TELEPORTBALL = DESCRIPTOR.message_types_by_name['TeleportBall']
_TELEPORTROBOT = DESCRIPTOR.message_types_by_name['TeleportRobot']
_SIMULATORCONTROL = DESCRIPTOR.message_types_by_name['SimulatorControl']
_SIMULATORCOMMAND = DESCRIPTOR.message_types_by_name['SimulatorCommand']
_SIMULATORRESPONSE = DESCRIPTOR.message_types_by_name['SimulatorResponse']
TeleportBall = _reflection.GeneratedProtocolMessageType('TeleportBall', (_message.Message,), {'DESCRIPTOR': _TELEPORTBALL, '__module__': 'ssl_simulation_control_pb2'})
_sym_db.RegisterMessage(TeleportBall)
TeleportRobot = _reflection.GeneratedProtocolMessageType('TeleportRobot', (_message.Message,), {'DESCRIPTOR': _TELEPORTROBOT, '__module__': 'ssl_simulation_control_pb2'})
_sym_db.RegisterMessage(TeleportRobot)
SimulatorControl = _reflection.GeneratedProtocolMessageType('SimulatorControl', (_message.Message,), {'DESCRIPTOR': _SIMULATORCONTROL, '__module__': 'ssl_simulation_control_pb2'})
_sym_db.RegisterMessage(SimulatorControl)
SimulatorCommand = _reflection.GeneratedProtocolMessageType('SimulatorCommand', (_message.Message,), {'DESCRIPTOR': _SIMULATORCOMMAND, '__module__': 'ssl_simulation_control_pb2'})
_sym_db.RegisterMessage(SimulatorCommand)
SimulatorResponse = _reflection.GeneratedProtocolMessageType('SimulatorResponse', (_message.Message,), {'DESCRIPTOR': _SIMULATORRESPONSE, '__module__': 'ssl_simulation_control_pb2'})
_sym_db.RegisterMessage(SimulatorResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim'
    _TELEPORTBALL._serialized_start = 111
    _TELEPORTBALL._serialized_end = 272
    _TELEPORTROBOT._serialized_start = 275
    _TELEPORTROBOT._serialized_end = 451
    _SIMULATORCONTROL._serialized_start = 453
    _SIMULATORCONTROL._serialized_end = 575
    _SIMULATORCOMMAND._serialized_start = 577
    _SIMULATORCOMMAND._serialized_end = 665
    _SIMULATORRESPONSE._serialized_start = 667
    _SIMULATORRESPONSE._serialized_end = 719