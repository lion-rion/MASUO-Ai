"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import grSim_Commands_pb2 as grSim__Commands__pb2
from . import grSim_Replacement_pb2 as grSim__Replacement__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12grSim_Packet.proto\x1a\x14grSim_Commands.proto\x1a\x17grSim_Replacement.proto"Z\n\x0cgrSim_Packet\x12!\n\x08commands\x18\x01 \x01(\x0b2\x0f.grSim_Commands\x12\'\n\x0breplacement\x18\x02 \x01(\x0b2\x12.grSim_Replacement')
_GRSIM_PACKET = DESCRIPTOR.message_types_by_name['grSim_Packet']
grSim_Packet = _reflection.GeneratedProtocolMessageType('grSim_Packet', (_message.Message,), {'DESCRIPTOR': _GRSIM_PACKET, '__module__': 'grSim_Packet_pb2'})
_sym_db.RegisterMessage(grSim_Packet)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GRSIM_PACKET._serialized_start = 69
    _GRSIM_PACKET._serialized_end = 159