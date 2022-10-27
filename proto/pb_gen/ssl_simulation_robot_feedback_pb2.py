"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import ssl_simulation_error_pb2 as ssl__simulation__error__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#ssl_simulation_robot_feedback.proto\x1a\x1assl_simulation_error.proto\x1a\x19google/protobuf/any.proto"`\n\rRobotFeedback\x12\n\n\x02id\x18\x01 \x02(\r\x12\x1d\n\x15dribbler_ball_contact\x18\x02 \x01(\x08\x12$\n\x06custom\x18\x03 \x01(\x0b2\x14.google.protobuf.Any"Y\n\x14RobotControlResponse\x12\x1f\n\x06errors\x18\x01 \x03(\x0b2\x0f.SimulatorError\x12 \n\x08feedback\x18\x02 \x03(\x0b2\x0e.RobotFeedbackB8Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim')
_ROBOTFEEDBACK = DESCRIPTOR.message_types_by_name['RobotFeedback']
_ROBOTCONTROLRESPONSE = DESCRIPTOR.message_types_by_name['RobotControlResponse']
RobotFeedback = _reflection.GeneratedProtocolMessageType('RobotFeedback', (_message.Message,), {'DESCRIPTOR': _ROBOTFEEDBACK, '__module__': 'ssl_simulation_robot_feedback_pb2'})
_sym_db.RegisterMessage(RobotFeedback)
RobotControlResponse = _reflection.GeneratedProtocolMessageType('RobotControlResponse', (_message.Message,), {'DESCRIPTOR': _ROBOTCONTROLRESPONSE, '__module__': 'ssl_simulation_robot_feedback_pb2'})
_sym_db.RegisterMessage(RobotControlResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim'
    _ROBOTFEEDBACK._serialized_start = 94
    _ROBOTFEEDBACK._serialized_end = 190
    _ROBOTCONTROLRESPONSE._serialized_start = 192
    _ROBOTCONTROLRESPONSE._serialized_end = 281