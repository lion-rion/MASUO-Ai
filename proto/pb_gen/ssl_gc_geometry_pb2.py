"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15ssl_gc_geometry.proto"\x1f\n\x07Vector2\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02B>Z<github.com/RoboCup-SSL/ssl-game-controller/internal/app/geom')
_VECTOR2 = DESCRIPTOR.message_types_by_name['Vector2']
_VECTOR3 = DESCRIPTOR.message_types_by_name['Vector3']
Vector2 = _reflection.GeneratedProtocolMessageType('Vector2', (_message.Message,), {'DESCRIPTOR': _VECTOR2, '__module__': 'ssl_gc_geometry_pb2'})
_sym_db.RegisterMessage(Vector2)
Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), {'DESCRIPTOR': _VECTOR3, '__module__': 'ssl_gc_geometry_pb2'})
_sym_db.RegisterMessage(Vector3)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/RoboCup-SSL/ssl-game-controller/internal/app/geom'
    _VECTOR2._serialized_start = 25
    _VECTOR2._serialized_end = 56
    _VECTOR3._serialized_start = 58
    _VECTOR3._serialized_end = 100