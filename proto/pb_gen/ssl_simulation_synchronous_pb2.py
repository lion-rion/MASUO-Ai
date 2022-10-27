"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import ssl_vision_detection_pb2 as ssl__vision__detection__pb2
from . import ssl_simulation_robot_feedback_pb2 as ssl__simulation__robot__feedback__pb2
from . import ssl_simulation_robot_control_pb2 as ssl__simulation__robot__control__pb2
from . import ssl_simulation_control_pb2 as ssl__simulation__control__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ssl_simulation_synchronous.proto\x1a\x1assl_vision_detection.proto\x1a#ssl_simulation_robot_feedback.proto\x1a"ssl_simulation_robot_control.proto\x1a\x1cssl_simulation_control.proto"}\n\x15SimulationSyncRequest\x12\x10\n\x08sim_step\x18\x01 \x01(\x02\x12,\n\x11simulator_command\x18\x02 \x01(\x0b2\x11.SimulatorCommand\x12$\n\rrobot_control\x18\x03 \x01(\x0b2\r.RobotControl"w\n\x16SimulationSyncResponse\x12&\n\tdetection\x18\x01 \x03(\x0b2\x13.SSL_DetectionFrame\x125\n\x16robot_control_response\x18\x02 \x01(\x0b2\x15.RobotControlResponseB8Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim')
_SIMULATIONSYNCREQUEST = DESCRIPTOR.message_types_by_name['SimulationSyncRequest']
_SIMULATIONSYNCRESPONSE = DESCRIPTOR.message_types_by_name['SimulationSyncResponse']
SimulationSyncRequest = _reflection.GeneratedProtocolMessageType('SimulationSyncRequest', (_message.Message,), {'DESCRIPTOR': _SIMULATIONSYNCREQUEST, '__module__': 'ssl_simulation_synchronous_pb2'})
_sym_db.RegisterMessage(SimulationSyncRequest)
SimulationSyncResponse = _reflection.GeneratedProtocolMessageType('SimulationSyncResponse', (_message.Message,), {'DESCRIPTOR': _SIMULATIONSYNCRESPONSE, '__module__': 'ssl_simulation_synchronous_pb2'})
_sym_db.RegisterMessage(SimulationSyncResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim'
    _SIMULATIONSYNCREQUEST._serialized_start = 167
    _SIMULATIONSYNCREQUEST._serialized_end = 292
    _SIMULATIONSYNCRESPONSE._serialized_start = 294
    _SIMULATIONSYNCRESPONSE._serialized_end = 413