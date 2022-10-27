"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1assl_vision_detection.proto"x\n\x11SSL_DetectionBall\x12\x12\n\nconfidence\x18\x01 \x02(\x02\x12\x0c\n\x04area\x18\x02 \x01(\r\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\x12\t\n\x01z\x18\x05 \x01(\x02\x12\x0f\n\x07pixel_x\x18\x06 \x02(\x02\x12\x0f\n\x07pixel_y\x18\x07 \x02(\x02"\x97\x01\n\x12SSL_DetectionRobot\x12\x12\n\nconfidence\x18\x01 \x02(\x02\x12\x10\n\x08robot_id\x18\x02 \x01(\r\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\x12\x13\n\x0borientation\x18\x05 \x01(\x02\x12\x0f\n\x07pixel_x\x18\x06 \x02(\x02\x12\x0f\n\x07pixel_y\x18\x07 \x02(\x02\x12\x0e\n\x06height\x18\x08 \x01(\x02"\xd9\x01\n\x12SSL_DetectionFrame\x12\x14\n\x0cframe_number\x18\x01 \x02(\r\x12\x11\n\tt_capture\x18\x02 \x02(\x01\x12\x0e\n\x06t_sent\x18\x03 \x02(\x01\x12\x11\n\tcamera_id\x18\x04 \x02(\r\x12!\n\x05balls\x18\x05 \x03(\x0b2\x12.SSL_DetectionBall\x12*\n\rrobots_yellow\x18\x06 \x03(\x0b2\x13.SSL_DetectionRobot\x12(\n\x0brobots_blue\x18\x07 \x03(\x0b2\x13.SSL_DetectionRobotB8Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim')
_SSL_DETECTIONBALL = DESCRIPTOR.message_types_by_name['SSL_DetectionBall']
_SSL_DETECTIONROBOT = DESCRIPTOR.message_types_by_name['SSL_DetectionRobot']
_SSL_DETECTIONFRAME = DESCRIPTOR.message_types_by_name['SSL_DetectionFrame']
SSL_DetectionBall = _reflection.GeneratedProtocolMessageType('SSL_DetectionBall', (_message.Message,), {'DESCRIPTOR': _SSL_DETECTIONBALL, '__module__': 'ssl_vision_detection_pb2'})
_sym_db.RegisterMessage(SSL_DetectionBall)
SSL_DetectionRobot = _reflection.GeneratedProtocolMessageType('SSL_DetectionRobot', (_message.Message,), {'DESCRIPTOR': _SSL_DETECTIONROBOT, '__module__': 'ssl_vision_detection_pb2'})
_sym_db.RegisterMessage(SSL_DetectionRobot)
SSL_DetectionFrame = _reflection.GeneratedProtocolMessageType('SSL_DetectionFrame', (_message.Message,), {'DESCRIPTOR': _SSL_DETECTIONFRAME, '__module__': 'ssl_vision_detection_pb2'})
_sym_db.RegisterMessage(SSL_DetectionFrame)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim'
    _SSL_DETECTIONBALL._serialized_start = 30
    _SSL_DETECTIONBALL._serialized_end = 150
    _SSL_DETECTIONROBOT._serialized_start = 153
    _SSL_DETECTIONROBOT._serialized_end = 304
    _SSL_DETECTIONFRAME._serialized_start = 307
    _SSL_DETECTIONFRAME._serialized_end = 524