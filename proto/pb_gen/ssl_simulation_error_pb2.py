"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1assl_simulation_error.proto"/\n\x0eSimulatorError\x12\x0c\n\x04code\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\tB8Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim')
_SIMULATORERROR = DESCRIPTOR.message_types_by_name['SimulatorError']
SimulatorError = _reflection.GeneratedProtocolMessageType('SimulatorError', (_message.Message,), {'DESCRIPTOR': _SIMULATORERROR, '__module__': 'ssl_simulation_error_pb2'})
_sym_db.RegisterMessage(SimulatorError)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/RoboCup-SSL/ssl-simulation-protocol/pkg/sim'
    _SIMULATORERROR._serialized_start = 30
    _SIMULATORERROR._serialized_end = 77