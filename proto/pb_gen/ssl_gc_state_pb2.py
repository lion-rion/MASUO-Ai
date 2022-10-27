"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import ssl_gc_common_pb2 as ssl__gc__common__pb2
from . import ssl_gc_geometry_pb2 as ssl__gc__geometry__pb2
from . import ssl_gc_game_event_pb2 as ssl__gc__game__event__pb2
from . import ssl_gc_referee_message_pb2 as ssl__gc__referee__message__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12ssl_gc_state.proto\x1a\x13ssl_gc_common.proto\x1a\x15ssl_gc_geometry.proto\x1a\x17ssl_gc_game_event.proto\x1a\x1cssl_gc_referee_message.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"u\n\nYellowCard\x12\n\n\x02id\x18\x01 \x01(\r\x12(\n\x14caused_by_game_event\x18\x02 \x01(\x0b2\n.GameEvent\x121\n\x0etime_remaining\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration"?\n\x07RedCard\x12\n\n\x02id\x18\x01 \x01(\r\x12(\n\x14caused_by_game_event\x18\x02 \x01(\x0b2\n.GameEvent"k\n\x04Foul\x12\n\n\x02id\x18\x01 \x01(\r\x12(\n\x14caused_by_game_event\x18\x02 \x01(\x0b2\n.GameEvent\x12-\n\ttimestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xe1\x01\n\x07Command\x12\x1b\n\x04type\x18\x01 \x02(\x0e2\r.Command.Type\x12\x17\n\x08for_team\x18\x02 \x01(\x0e2\x05.Team"\x9f\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04HALT\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\x10\n\x0cNORMAL_START\x10\x03\x12\x0f\n\x0bFORCE_START\x10\x04\x12\n\n\x06DIRECT\x10\x05\x12\x0c\n\x08INDIRECT\x10\x06\x12\x0b\n\x07KICKOFF\x10\x07\x12\x0b\n\x07PENALTY\x10\x08\x12\x0b\n\x07TIMEOUT\x10\t\x12\x12\n\x0eBALL_PLACEMENT\x10\n"\xc3\x01\n\tGameState\x12\x1d\n\x04type\x18\x01 \x02(\x0e2\x0f.GameState.Type\x12\x17\n\x08for_team\x18\x02 \x01(\x0e2\x05.Team"~\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04HALT\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\r\n\tFREE_KICK\x10\x04\x12\x0b\n\x07KICKOFF\x10\x05\x12\x0b\n\x07PENALTY\x10\x06\x12\x0b\n\x07TIMEOUT\x10\x07\x12\x12\n\x0eBALL_PLACEMENT\x10\x08"Y\n\x08Proposal\x12-\n\ttimestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1e\n\ngame_event\x18\x02 \x01(\x0b2\n.GameEvent"?\n\rProposalGroup\x12\x1c\n\tproposals\x18\x01 \x03(\x0b2\t.Proposal\x12\x10\n\x08accepted\x18\x02 \x01(\x08"\xd1\x04\n\x08TeamInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05goals\x18\x02 \x01(\x05\x12\x12\n\ngoalkeeper\x18\x03 \x01(\x05\x12!\n\x0cyellow_cards\x18\x04 \x03(\x0b2\x0b.YellowCard\x12\x1b\n\tred_cards\x18\x05 \x03(\x0b2\x08.RedCard\x12\x15\n\rtimeouts_left\x18\x06 \x01(\x05\x124\n\x11timeout_time_left\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration\x12\x18\n\x10on_positive_half\x18\x08 \x01(\x08\x12\x14\n\x05fouls\x18\t \x03(\x0b2\x05.Foul\x12\x1f\n\x17ball_placement_failures\x18\n \x01(\x05\x12\'\n\x1fball_placement_failures_reached\x18\x0b \x01(\x08\x12\x16\n\x0ecan_place_ball\x18\x0c \x01(\x08\x12\x18\n\x10max_allowed_bots\x18\r \x01(\x05\x12C\n\x1frequests_bot_substitution_since\x18\x0e \x01(\x0b2\x1a.google.protobuf.Timestamp\x12:\n\x16requests_timeout_since\x18\x0f \x01(\x0b2\x1a.google.protobuf.Timestamp\x12A\n\x1drequests_emergency_stop_since\x18\x10 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fchallenge_flags\x18\x11 \x01(\x05"\xae\x05\n\x05State\x12\x1d\n\x05stage\x18\x01 \x01(\x0e2\x0e.Referee.Stage\x12\x19\n\x07command\x18\x02 \x01(\x0b2\x08.Command\x12\x1e\n\ngame_state\x18\x13 \x01(\x0b2\n.GameState\x125\n\x12stage_time_elapsed\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fstage_time_left\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x124\n\x10match_time_start\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12)\n\nteam_state\x18\x08 \x03(\x0b2\x15.State.TeamStateEntry\x12\x1f\n\rplacement_pos\x18\t \x01(\x0b2\x08.Vector2\x12\x1e\n\x0cnext_command\x18\n \x01(\x0b2\x08.Command\x12@\n\x1dcurrent_action_time_remaining\x18\x0c \x01(\x0b2\x19.google.protobuf.Duration\x12\x1f\n\x0bgame_events\x18\r \x03(\x0b2\n.GameEvent\x12\'\n\x0fproposal_groups\x18\x0e \x03(\x0b2\x0e.ProposalGroup\x12\x1b\n\x08division\x18\x0f \x01(\x0e2\t.Division\x12\x15\n\rauto_continue\x18\x10 \x01(\x08\x12!\n\x12first_kickoff_team\x18\x11 \x01(\x0e2\x05.Team\x12\x1e\n\nmatch_type\x18\x12 \x01(\x0e2\n.MatchType\x1a;\n\x0eTeamStateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b2\t.TeamInfo:\x028\x01B?Z=github.com/RoboCup-SSL/ssl-game-controller/internal/app/state')
_YELLOWCARD = DESCRIPTOR.message_types_by_name['YellowCard']
_REDCARD = DESCRIPTOR.message_types_by_name['RedCard']
_FOUL = DESCRIPTOR.message_types_by_name['Foul']
_COMMAND = DESCRIPTOR.message_types_by_name['Command']
_GAMESTATE = DESCRIPTOR.message_types_by_name['GameState']
_PROPOSAL = DESCRIPTOR.message_types_by_name['Proposal']
_PROPOSALGROUP = DESCRIPTOR.message_types_by_name['ProposalGroup']
_TEAMINFO = DESCRIPTOR.message_types_by_name['TeamInfo']
_STATE = DESCRIPTOR.message_types_by_name['State']
_STATE_TEAMSTATEENTRY = _STATE.nested_types_by_name['TeamStateEntry']
_COMMAND_TYPE = _COMMAND.enum_types_by_name['Type']
_GAMESTATE_TYPE = _GAMESTATE.enum_types_by_name['Type']
YellowCard = _reflection.GeneratedProtocolMessageType('YellowCard', (_message.Message,), {'DESCRIPTOR': _YELLOWCARD, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(YellowCard)
RedCard = _reflection.GeneratedProtocolMessageType('RedCard', (_message.Message,), {'DESCRIPTOR': _REDCARD, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(RedCard)
Foul = _reflection.GeneratedProtocolMessageType('Foul', (_message.Message,), {'DESCRIPTOR': _FOUL, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(Foul)
Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {'DESCRIPTOR': _COMMAND, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(Command)
GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {'DESCRIPTOR': _GAMESTATE, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(GameState)
Proposal = _reflection.GeneratedProtocolMessageType('Proposal', (_message.Message,), {'DESCRIPTOR': _PROPOSAL, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(Proposal)
ProposalGroup = _reflection.GeneratedProtocolMessageType('ProposalGroup', (_message.Message,), {'DESCRIPTOR': _PROPOSALGROUP, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(ProposalGroup)
TeamInfo = _reflection.GeneratedProtocolMessageType('TeamInfo', (_message.Message,), {'DESCRIPTOR': _TEAMINFO, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(TeamInfo)
State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {'TeamStateEntry': _reflection.GeneratedProtocolMessageType('TeamStateEntry', (_message.Message,), {'DESCRIPTOR': _STATE_TEAMSTATEENTRY, '__module__': 'ssl_gc_state_pb2'}), 'DESCRIPTOR': _STATE, '__module__': 'ssl_gc_state_pb2'})
_sym_db.RegisterMessage(State)
_sym_db.RegisterMessage(State.TeamStateEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/RoboCup-SSL/ssl-game-controller/internal/app/state'
    _STATE_TEAMSTATEENTRY._options = None
    _STATE_TEAMSTATEENTRY._serialized_options = b'8\x01'
    _YELLOWCARD._serialized_start = 186
    _YELLOWCARD._serialized_end = 303
    _REDCARD._serialized_start = 305
    _REDCARD._serialized_end = 368
    _FOUL._serialized_start = 370
    _FOUL._serialized_end = 477
    _COMMAND._serialized_start = 480
    _COMMAND._serialized_end = 705
    _COMMAND_TYPE._serialized_start = 546
    _COMMAND_TYPE._serialized_end = 705
    _GAMESTATE._serialized_start = 708
    _GAMESTATE._serialized_end = 903
    _GAMESTATE_TYPE._serialized_start = 777
    _GAMESTATE_TYPE._serialized_end = 903
    _PROPOSAL._serialized_start = 905
    _PROPOSAL._serialized_end = 994
    _PROPOSALGROUP._serialized_start = 996
    _PROPOSALGROUP._serialized_end = 1059
    _TEAMINFO._serialized_start = 1062
    _TEAMINFO._serialized_end = 1655
    _STATE._serialized_start = 1658
    _STATE._serialized_end = 2344
    _STATE_TEAMSTATEENTRY._serialized_start = 2285
    _STATE_TEAMSTATEENTRY._serialized_end = 2344