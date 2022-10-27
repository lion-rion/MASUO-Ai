"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
from . import ssl_gc_common_pb2
from . import ssl_gc_game_event_pb2
from . import ssl_gc_geometry_pb2
from . import ssl_gc_referee_message_pb2
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class YellowCard(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    CAUSED_BY_GAME_EVENT_FIELD_NUMBER: builtins.int
    TIME_REMAINING_FIELD_NUMBER: builtins.int
    id: builtins.int = ...

    @property
    def caused_by_game_event(self) -> ssl_gc_game_event_pb2.GameEvent:
        ...

    @property
    def time_remaining(self) -> google.protobuf.duration_pb2.Duration:
        ...

    def __init__(self, *, id: typing.Optional[builtins.int]=..., caused_by_game_event: typing.Optional[ssl_gc_game_event_pb2.GameEvent]=..., time_remaining: typing.Optional[google.protobuf.duration_pb2.Duration]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['caused_by_game_event', b'caused_by_game_event', 'id', b'id', 'time_remaining', b'time_remaining']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['caused_by_game_event', b'caused_by_game_event', 'id', b'id', 'time_remaining', b'time_remaining']) -> None:
        ...
global___YellowCard = YellowCard

class RedCard(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    CAUSED_BY_GAME_EVENT_FIELD_NUMBER: builtins.int
    id: builtins.int = ...

    @property
    def caused_by_game_event(self) -> ssl_gc_game_event_pb2.GameEvent:
        ...

    def __init__(self, *, id: typing.Optional[builtins.int]=..., caused_by_game_event: typing.Optional[ssl_gc_game_event_pb2.GameEvent]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['caused_by_game_event', b'caused_by_game_event', 'id', b'id']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['caused_by_game_event', b'caused_by_game_event', 'id', b'id']) -> None:
        ...
global___RedCard = RedCard

class Foul(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    CAUSED_BY_GAME_EVENT_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    id: builtins.int = ...

    @property
    def caused_by_game_event(self) -> ssl_gc_game_event_pb2.GameEvent:
        ...

    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    def __init__(self, *, id: typing.Optional[builtins.int]=..., caused_by_game_event: typing.Optional[ssl_gc_game_event_pb2.GameEvent]=..., timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['caused_by_game_event', b'caused_by_game_event', 'id', b'id', 'timestamp', b'timestamp']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['caused_by_game_event', b'caused_by_game_event', 'id', b'id', 'timestamp', b'timestamp']) -> None:
        ...
global___Foul = Foul

class Command(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNKNOWN: Command.Type.ValueType = ...
        HALT: Command.Type.ValueType = ...
        STOP: Command.Type.ValueType = ...
        NORMAL_START: Command.Type.ValueType = ...
        FORCE_START: Command.Type.ValueType = ...
        DIRECT: Command.Type.ValueType = ...
        INDIRECT: Command.Type.ValueType = ...
        KICKOFF: Command.Type.ValueType = ...
        PENALTY: Command.Type.ValueType = ...
        TIMEOUT: Command.Type.ValueType = ...
        BALL_PLACEMENT: Command.Type.ValueType = ...

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass
    UNKNOWN: Command.Type.ValueType = ...
    HALT: Command.Type.ValueType = ...
    STOP: Command.Type.ValueType = ...
    NORMAL_START: Command.Type.ValueType = ...
    FORCE_START: Command.Type.ValueType = ...
    DIRECT: Command.Type.ValueType = ...
    INDIRECT: Command.Type.ValueType = ...
    KICKOFF: Command.Type.ValueType = ...
    PENALTY: Command.Type.ValueType = ...
    TIMEOUT: Command.Type.ValueType = ...
    BALL_PLACEMENT: Command.Type.ValueType = ...
    TYPE_FIELD_NUMBER: builtins.int
    FOR_TEAM_FIELD_NUMBER: builtins.int
    type: global___Command.Type.ValueType = ...
    for_team: ssl_gc_common_pb2.Team.ValueType = ...

    def __init__(self, *, type: typing.Optional[global___Command.Type.ValueType]=..., for_team: typing.Optional[ssl_gc_common_pb2.Team.ValueType]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['for_team', b'for_team', 'type', b'type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['for_team', b'for_team', 'type', b'type']) -> None:
        ...
global___Command = Command

class GameState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNKNOWN: GameState.Type.ValueType = ...
        HALT: GameState.Type.ValueType = ...
        STOP: GameState.Type.ValueType = ...
        RUNNING: GameState.Type.ValueType = ...
        FREE_KICK: GameState.Type.ValueType = ...
        KICKOFF: GameState.Type.ValueType = ...
        PENALTY: GameState.Type.ValueType = ...
        TIMEOUT: GameState.Type.ValueType = ...
        BALL_PLACEMENT: GameState.Type.ValueType = ...

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass
    UNKNOWN: GameState.Type.ValueType = ...
    HALT: GameState.Type.ValueType = ...
    STOP: GameState.Type.ValueType = ...
    RUNNING: GameState.Type.ValueType = ...
    FREE_KICK: GameState.Type.ValueType = ...
    KICKOFF: GameState.Type.ValueType = ...
    PENALTY: GameState.Type.ValueType = ...
    TIMEOUT: GameState.Type.ValueType = ...
    BALL_PLACEMENT: GameState.Type.ValueType = ...
    TYPE_FIELD_NUMBER: builtins.int
    FOR_TEAM_FIELD_NUMBER: builtins.int
    type: global___GameState.Type.ValueType = ...
    for_team: ssl_gc_common_pb2.Team.ValueType = ...

    def __init__(self, *, type: typing.Optional[global___GameState.Type.ValueType]=..., for_team: typing.Optional[ssl_gc_common_pb2.Team.ValueType]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['for_team', b'for_team', 'type', b'type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['for_team', b'for_team', 'type', b'type']) -> None:
        ...
global___GameState = GameState

class Proposal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIMESTAMP_FIELD_NUMBER: builtins.int
    GAME_EVENT_FIELD_NUMBER: builtins.int

    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp when the game event proposal occurred"""
        pass

    @property
    def game_event(self) -> ssl_gc_game_event_pb2.GameEvent:
        """The proposed game event."""
        pass

    def __init__(self, *, timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp]=..., game_event: typing.Optional[ssl_gc_game_event_pb2.GameEvent]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['game_event', b'game_event', 'timestamp', b'timestamp']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['game_event', b'game_event', 'timestamp', b'timestamp']) -> None:
        ...
global___Proposal = Proposal

class ProposalGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROPOSALS_FIELD_NUMBER: builtins.int
    ACCEPTED_FIELD_NUMBER: builtins.int

    @property
    def proposals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Proposal]:
        """List of proposals in this group"""
        pass
    accepted: builtins.bool = ...
    'Whether the proposal group was accepted'

    def __init__(self, *, proposals: typing.Optional[typing.Iterable[global___Proposal]]=..., accepted: typing.Optional[builtins.bool]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['accepted', b'accepted']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['accepted', b'accepted', 'proposals', b'proposals']) -> None:
        ...
global___ProposalGroup = ProposalGroup

class TeamInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    GOALS_FIELD_NUMBER: builtins.int
    GOALKEEPER_FIELD_NUMBER: builtins.int
    YELLOW_CARDS_FIELD_NUMBER: builtins.int
    RED_CARDS_FIELD_NUMBER: builtins.int
    TIMEOUTS_LEFT_FIELD_NUMBER: builtins.int
    TIMEOUT_TIME_LEFT_FIELD_NUMBER: builtins.int
    ON_POSITIVE_HALF_FIELD_NUMBER: builtins.int
    FOULS_FIELD_NUMBER: builtins.int
    BALL_PLACEMENT_FAILURES_FIELD_NUMBER: builtins.int
    BALL_PLACEMENT_FAILURES_REACHED_FIELD_NUMBER: builtins.int
    CAN_PLACE_BALL_FIELD_NUMBER: builtins.int
    MAX_ALLOWED_BOTS_FIELD_NUMBER: builtins.int
    REQUESTS_BOT_SUBSTITUTION_SINCE_FIELD_NUMBER: builtins.int
    REQUESTS_TIMEOUT_SINCE_FIELD_NUMBER: builtins.int
    REQUESTS_EMERGENCY_STOP_SINCE_FIELD_NUMBER: builtins.int
    CHALLENGE_FLAGS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    goals: builtins.int = ...
    goalkeeper: builtins.int = ...

    @property
    def yellow_cards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___YellowCard]:
        ...

    @property
    def red_cards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RedCard]:
        ...
    timeouts_left: builtins.int = ...

    @property
    def timeout_time_left(self) -> google.protobuf.duration_pb2.Duration:
        ...
    on_positive_half: builtins.bool = ...

    @property
    def fouls(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Foul]:
        ...
    ball_placement_failures: builtins.int = ...
    ball_placement_failures_reached: builtins.bool = ...
    can_place_ball: builtins.bool = ...
    max_allowed_bots: builtins.int = ...

    @property
    def requests_bot_substitution_since(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def requests_timeout_since(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def requests_emergency_stop_since(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    challenge_flags: builtins.int = ...

    def __init__(self, *, name: typing.Optional[typing.Text]=..., goals: typing.Optional[builtins.int]=..., goalkeeper: typing.Optional[builtins.int]=..., yellow_cards: typing.Optional[typing.Iterable[global___YellowCard]]=..., red_cards: typing.Optional[typing.Iterable[global___RedCard]]=..., timeouts_left: typing.Optional[builtins.int]=..., timeout_time_left: typing.Optional[google.protobuf.duration_pb2.Duration]=..., on_positive_half: typing.Optional[builtins.bool]=..., fouls: typing.Optional[typing.Iterable[global___Foul]]=..., ball_placement_failures: typing.Optional[builtins.int]=..., ball_placement_failures_reached: typing.Optional[builtins.bool]=..., can_place_ball: typing.Optional[builtins.bool]=..., max_allowed_bots: typing.Optional[builtins.int]=..., requests_bot_substitution_since: typing.Optional[google.protobuf.timestamp_pb2.Timestamp]=..., requests_timeout_since: typing.Optional[google.protobuf.timestamp_pb2.Timestamp]=..., requests_emergency_stop_since: typing.Optional[google.protobuf.timestamp_pb2.Timestamp]=..., challenge_flags: typing.Optional[builtins.int]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['ball_placement_failures', b'ball_placement_failures', 'ball_placement_failures_reached', b'ball_placement_failures_reached', 'can_place_ball', b'can_place_ball', 'challenge_flags', b'challenge_flags', 'goalkeeper', b'goalkeeper', 'goals', b'goals', 'max_allowed_bots', b'max_allowed_bots', 'name', b'name', 'on_positive_half', b'on_positive_half', 'requests_bot_substitution_since', b'requests_bot_substitution_since', 'requests_emergency_stop_since', b'requests_emergency_stop_since', 'requests_timeout_since', b'requests_timeout_since', 'timeout_time_left', b'timeout_time_left', 'timeouts_left', b'timeouts_left']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['ball_placement_failures', b'ball_placement_failures', 'ball_placement_failures_reached', b'ball_placement_failures_reached', 'can_place_ball', b'can_place_ball', 'challenge_flags', b'challenge_flags', 'fouls', b'fouls', 'goalkeeper', b'goalkeeper', 'goals', b'goals', 'max_allowed_bots', b'max_allowed_bots', 'name', b'name', 'on_positive_half', b'on_positive_half', 'red_cards', b'red_cards', 'requests_bot_substitution_since', b'requests_bot_substitution_since', 'requests_emergency_stop_since', b'requests_emergency_stop_since', 'requests_timeout_since', b'requests_timeout_since', 'timeout_time_left', b'timeout_time_left', 'timeouts_left', b'timeouts_left', 'yellow_cards', b'yellow_cards']) -> None:
        ...
global___TeamInfo = TeamInfo

class State(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    class TeamStateEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> global___TeamInfo:
            ...

        def __init__(self, *, key: typing.Optional[typing.Text]=..., value: typing.Optional[global___TeamInfo]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    STAGE_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    GAME_STATE_FIELD_NUMBER: builtins.int
    STAGE_TIME_ELAPSED_FIELD_NUMBER: builtins.int
    STAGE_TIME_LEFT_FIELD_NUMBER: builtins.int
    MATCH_TIME_START_FIELD_NUMBER: builtins.int
    TEAM_STATE_FIELD_NUMBER: builtins.int
    PLACEMENT_POS_FIELD_NUMBER: builtins.int
    NEXT_COMMAND_FIELD_NUMBER: builtins.int
    CURRENT_ACTION_TIME_REMAINING_FIELD_NUMBER: builtins.int
    GAME_EVENTS_FIELD_NUMBER: builtins.int
    PROPOSAL_GROUPS_FIELD_NUMBER: builtins.int
    DIVISION_FIELD_NUMBER: builtins.int
    AUTO_CONTINUE_FIELD_NUMBER: builtins.int
    FIRST_KICKOFF_TEAM_FIELD_NUMBER: builtins.int
    MATCH_TYPE_FIELD_NUMBER: builtins.int
    stage: ssl_gc_referee_message_pb2.Referee.Stage.ValueType = ...

    @property
    def command(self) -> global___Command:
        ...

    @property
    def game_state(self) -> global___GameState:
        ...

    @property
    def stage_time_elapsed(self) -> google.protobuf.duration_pb2.Duration:
        ...

    @property
    def stage_time_left(self) -> google.protobuf.duration_pb2.Duration:
        ...

    @property
    def match_time_start(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def team_state(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___TeamInfo]:
        ...

    @property
    def placement_pos(self) -> ssl_gc_geometry_pb2.Vector2:
        ...

    @property
    def next_command(self) -> global___Command:
        ...

    @property
    def current_action_time_remaining(self) -> google.protobuf.duration_pb2.Duration:
        ...

    @property
    def game_events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ssl_gc_game_event_pb2.GameEvent]:
        ...

    @property
    def proposal_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProposalGroup]:
        ...
    division: ssl_gc_common_pb2.Division.ValueType = ...
    auto_continue: builtins.bool = ...
    first_kickoff_team: ssl_gc_common_pb2.Team.ValueType = ...
    match_type: ssl_gc_referee_message_pb2.MatchType.ValueType = ...

    def __init__(self, *, stage: typing.Optional[ssl_gc_referee_message_pb2.Referee.Stage.ValueType]=..., command: typing.Optional[global___Command]=..., game_state: typing.Optional[global___GameState]=..., stage_time_elapsed: typing.Optional[google.protobuf.duration_pb2.Duration]=..., stage_time_left: typing.Optional[google.protobuf.duration_pb2.Duration]=..., match_time_start: typing.Optional[google.protobuf.timestamp_pb2.Timestamp]=..., team_state: typing.Optional[typing.Mapping[typing.Text, global___TeamInfo]]=..., placement_pos: typing.Optional[ssl_gc_geometry_pb2.Vector2]=..., next_command: typing.Optional[global___Command]=..., current_action_time_remaining: typing.Optional[google.protobuf.duration_pb2.Duration]=..., game_events: typing.Optional[typing.Iterable[ssl_gc_game_event_pb2.GameEvent]]=..., proposal_groups: typing.Optional[typing.Iterable[global___ProposalGroup]]=..., division: typing.Optional[ssl_gc_common_pb2.Division.ValueType]=..., auto_continue: typing.Optional[builtins.bool]=..., first_kickoff_team: typing.Optional[ssl_gc_common_pb2.Team.ValueType]=..., match_type: typing.Optional[ssl_gc_referee_message_pb2.MatchType.ValueType]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['auto_continue', b'auto_continue', 'command', b'command', 'current_action_time_remaining', b'current_action_time_remaining', 'division', b'division', 'first_kickoff_team', b'first_kickoff_team', 'game_state', b'game_state', 'match_time_start', b'match_time_start', 'match_type', b'match_type', 'next_command', b'next_command', 'placement_pos', b'placement_pos', 'stage', b'stage', 'stage_time_elapsed', b'stage_time_elapsed', 'stage_time_left', b'stage_time_left']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['auto_continue', b'auto_continue', 'command', b'command', 'current_action_time_remaining', b'current_action_time_remaining', 'division', b'division', 'first_kickoff_team', b'first_kickoff_team', 'game_events', b'game_events', 'game_state', b'game_state', 'match_time_start', b'match_time_start', 'match_type', b'match_type', 'next_command', b'next_command', 'placement_pos', b'placement_pos', 'proposal_groups', b'proposal_groups', 'stage', b'stage', 'stage_time_elapsed', b'stage_time_elapsed', 'stage_time_left', b'stage_time_left', 'team_state', b'team_state']) -> None:
        ...
global___State = State