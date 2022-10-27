"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import ssl_vision_detection_pb2 as ssl__vision__detection__pb2
from . import ssl_vision_geometry_pb2 as ssl__vision__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18ssl_vision_wrapper.proto\x1a\x1assl_vision_detection.proto\x1a\x19ssl_vision_geometry.proto"`\n\x11SSL_WrapperPacket\x12&\n\tdetection\x18\x01 \x01(\x0b2\x13.SSL_DetectionFrame\x12#\n\x08geometry\x18\x02 \x01(\x0b2\x11.SSL_GeometryData')
_SSL_WRAPPERPACKET = DESCRIPTOR.message_types_by_name['SSL_WrapperPacket']
SSL_WrapperPacket = _reflection.GeneratedProtocolMessageType('SSL_WrapperPacket', (_message.Message,), {'DESCRIPTOR': _SSL_WRAPPERPACKET, '__module__': 'ssl_vision_wrapper_pb2'})
_sym_db.RegisterMessage(SSL_WrapperPacket)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SSL_WRAPPERPACKET._serialized_start = 83
    _SSL_WRAPPERPACKET._serialized_end = 179