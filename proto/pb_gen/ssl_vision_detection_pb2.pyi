"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SSL_DetectionBall(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONFIDENCE_FIELD_NUMBER: builtins.int
    AREA_FIELD_NUMBER: builtins.int
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    PIXEL_X_FIELD_NUMBER: builtins.int
    PIXEL_Y_FIELD_NUMBER: builtins.int
    confidence: builtins.float = ...
    area: builtins.int = ...
    x: builtins.float = ...
    y: builtins.float = ...
    z: builtins.float = ...
    pixel_x: builtins.float = ...
    pixel_y: builtins.float = ...

    def __init__(self, *, confidence: typing.Optional[builtins.float]=..., area: typing.Optional[builtins.int]=..., x: typing.Optional[builtins.float]=..., y: typing.Optional[builtins.float]=..., z: typing.Optional[builtins.float]=..., pixel_x: typing.Optional[builtins.float]=..., pixel_y: typing.Optional[builtins.float]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['area', b'area', 'confidence', b'confidence', 'pixel_x', b'pixel_x', 'pixel_y', b'pixel_y', 'x', b'x', 'y', b'y', 'z', b'z']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['area', b'area', 'confidence', b'confidence', 'pixel_x', b'pixel_x', 'pixel_y', b'pixel_y', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
        ...
global___SSL_DetectionBall = SSL_DetectionBall

class SSL_DetectionRobot(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONFIDENCE_FIELD_NUMBER: builtins.int
    ROBOT_ID_FIELD_NUMBER: builtins.int
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    ORIENTATION_FIELD_NUMBER: builtins.int
    PIXEL_X_FIELD_NUMBER: builtins.int
    PIXEL_Y_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    confidence: builtins.float = ...
    robot_id: builtins.int = ...
    x: builtins.float = ...
    y: builtins.float = ...
    orientation: builtins.float = ...
    pixel_x: builtins.float = ...
    pixel_y: builtins.float = ...
    height: builtins.float = ...

    def __init__(self, *, confidence: typing.Optional[builtins.float]=..., robot_id: typing.Optional[builtins.int]=..., x: typing.Optional[builtins.float]=..., y: typing.Optional[builtins.float]=..., orientation: typing.Optional[builtins.float]=..., pixel_x: typing.Optional[builtins.float]=..., pixel_y: typing.Optional[builtins.float]=..., height: typing.Optional[builtins.float]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['confidence', b'confidence', 'height', b'height', 'orientation', b'orientation', 'pixel_x', b'pixel_x', 'pixel_y', b'pixel_y', 'robot_id', b'robot_id', 'x', b'x', 'y', b'y']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['confidence', b'confidence', 'height', b'height', 'orientation', b'orientation', 'pixel_x', b'pixel_x', 'pixel_y', b'pixel_y', 'robot_id', b'robot_id', 'x', b'x', 'y', b'y']) -> None:
        ...
global___SSL_DetectionRobot = SSL_DetectionRobot

class SSL_DetectionFrame(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FRAME_NUMBER_FIELD_NUMBER: builtins.int
    T_CAPTURE_FIELD_NUMBER: builtins.int
    T_SENT_FIELD_NUMBER: builtins.int
    CAMERA_ID_FIELD_NUMBER: builtins.int
    BALLS_FIELD_NUMBER: builtins.int
    ROBOTS_YELLOW_FIELD_NUMBER: builtins.int
    ROBOTS_BLUE_FIELD_NUMBER: builtins.int
    frame_number: builtins.int = ...
    t_capture: builtins.float = ...
    t_sent: builtins.float = ...
    camera_id: builtins.int = ...

    @property
    def balls(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SSL_DetectionBall]:
        ...

    @property
    def robots_yellow(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SSL_DetectionRobot]:
        ...

    @property
    def robots_blue(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SSL_DetectionRobot]:
        ...

    def __init__(self, *, frame_number: typing.Optional[builtins.int]=..., t_capture: typing.Optional[builtins.float]=..., t_sent: typing.Optional[builtins.float]=..., camera_id: typing.Optional[builtins.int]=..., balls: typing.Optional[typing.Iterable[global___SSL_DetectionBall]]=..., robots_yellow: typing.Optional[typing.Iterable[global___SSL_DetectionRobot]]=..., robots_blue: typing.Optional[typing.Iterable[global___SSL_DetectionRobot]]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['camera_id', b'camera_id', 'frame_number', b'frame_number', 't_capture', b't_capture', 't_sent', b't_sent']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['balls', b'balls', 'camera_id', b'camera_id', 'frame_number', b'frame_number', 'robots_blue', b'robots_blue', 'robots_yellow', b'robots_yellow', 't_capture', b't_capture', 't_sent', b't_sent']) -> None:
        ...
global___SSL_DetectionFrame = SSL_DetectionFrame