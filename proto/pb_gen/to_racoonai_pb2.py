"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11to_racoonai.proto"\xc9\x02\n\x0bRobot_Infos\x12\x10\n\x08robot_id\x18\x01 \x02(\r\x12\t\n\x01x\x18\x02 \x02(\x02\x12\t\n\x01y\x18\x03 \x02(\x02\x12\r\n\x05theta\x18\x04 \x02(\x02\x12\x1b\n\x13distance_ball_robot\x18\x05 \x01(\x02\x12\x19\n\x11radian_ball_robot\x18\x06 \x01(\x02\x12\x0e\n\x06diff_x\x18\x07 \x02(\x02\x12\x0e\n\x06diff_y\x18\x08 \x02(\x02\x12\x12\n\ndiff_theta\x18\t \x02(\x02\x12\r\n\x05speed\x18\n \x02(\x02\x12\r\n\x05slope\x18\x0b \x02(\x02\x12\x11\n\tintercept\x18\x0c \x02(\x02\x12\x18\n\x10angular_velocity\x18\r \x02(\x02\x12\x0f\n\x07visible\x18\x0e \x02(\x08\x12\x12\n\nball_catch\x18\x0f \x01(\x08\x12\x0e\n\x06online\x18\x10 \x01(\x08\x12\x17\n\x0fbattery_voltage\x18\x11 \x01(\x02"\xbb\x01\n\tBall_Info\x12\x12\n\nfiltered_x\x18\x01 \x02(\x02\x12\x12\n\nfiltered_y\x18\x02 \x02(\x02\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\x12\t\n\x01z\x18\x05 \x02(\x02\x12\x0e\n\x06diff_x\x18\x06 \x02(\x02\x12\x0e\n\x06diff_y\x18\x07 \x02(\x02\x12\x14\n\x0cslope_radian\x18\x08 \x02(\x02\x12\x11\n\tintercept\x18\t \x02(\x02\x12\r\n\x05speed\x18\n \x02(\x02\x12\r\n\x05slope\x18\x0b \x02(\x02"\xf1\x02\n\rGeometry_Info\x12\x14\n\x0cfield_length\x18\x01 \x02(\x05\x12\x13\n\x0bfield_width\x18\x02 \x02(\x05\x12\x12\n\ngoal_width\x18\x03 \x02(\x05\x12\x12\n\ngoal_depth\x18\x04 \x02(\x05\x12\x16\n\x0eboundary_width\x18\x05 \x02(\x05\x12\x1a\n\x12penalty_area_depth\x18\x06 \x01(\x05\x12\x1a\n\x12penalty_area_width\x18\x07 \x01(\x05\x12\x1c\n\x14center_circle_radius\x18\x08 \x01(\x05\x12\x16\n\x0eline_thickness\x18\t \x01(\x05\x12#\n\x1bgoal_center_to_penalty_mark\x18\n \x01(\x05\x12\x13\n\x0bgoal_height\x18\x0b \x01(\x05\x12\x13\n\x0bball_radius\x18\x0c \x01(\x02\x12\x18\n\x10max_robot_radius\x18\r \x01(\x02\x12\x0e\n\x06goal_x\x18\x0e \x02(\x02\x12\x0e\n\x06goal_y\x18\x0f \x02(\x02"\xf5\x07\n\x0cReferee_Info\x12&\n\x07command\x18\x01 \x02(\x0e2\x15.Referee_Info.Command\x12"\n\x05stage\x18\x02 \x02(\x0e2\x13.Referee_Info.Stage\x12\x14\n\x0cyellow_cards\x18\x03 \x02(\r\x12\x11\n\tred_cards\x18\x04 \x02(\r\x12*\n\x0bpre_command\x18\x05 \x01(\x0e2\x15.Referee_Info.Command\x12+\n\x0cnext_command\x18\x06 \x01(\x0e2\x15.Referee_Info.Command\x12\x18\n\x10ball_placement_x\x18\x07 \x01(\x02\x12\x18\n\x10ball_placement_y\x18\x08 \x01(\x02"\x8e\x03\n\x07Command\x12\x08\n\x04HALT\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\x10\n\x0cNORMAL_START\x10\x02\x12\x0f\n\x0bFORCE_START\x10\x03\x12\x1a\n\x16PREPARE_KICKOFF_YELLOW\x10\x04\x12\x18\n\x14PREPARE_KICKOFF_BLUE\x10\x05\x12\x1a\n\x16PREPARE_PENALTY_YELLOW\x10\x06\x12\x18\n\x14PREPARE_PENALTY_BLUE\x10\x07\x12\x16\n\x12DIRECT_FREE_YELLOW\x10\x08\x12\x14\n\x10DIRECT_FREE_BLUE\x10\t\x12\x18\n\x14INDIRECT_FREE_YELLOW\x10\n\x12\x16\n\x12INDIRECT_FREE_BLUE\x10\x0b\x12\x12\n\x0eTIMEOUT_YELLOW\x10\x0c\x12\x10\n\x0cTIMEOUT_BLUE\x10\r\x12\x13\n\x0bGOAL_YELLOW\x10\x0e\x1a\x02\x08\x01\x12\x11\n\tGOAL_BLUE\x10\x0f\x1a\x02\x08\x01\x12\x19\n\x15BALL_PLACEMENT_YELLOW\x10\x10\x12\x17\n\x13BALL_PLACEMENT_BLUE\x10\x11"\xd1\x02\n\x05Stage\x12\x19\n\x15NORMAL_FIRST_HALF_PRE\x10\x00\x12\x15\n\x11NORMAL_FIRST_HALF\x10\x01\x12\x14\n\x10NORMAL_HALF_TIME\x10\x02\x12\x1a\n\x16NORMAL_SECOND_HALF_PRE\x10\x03\x12\x16\n\x12NORMAL_SECOND_HALF\x10\x04\x12\x14\n\x10EXTRA_TIME_BREAK\x10\x05\x12\x18\n\x14EXTRA_FIRST_HALF_PRE\x10\x06\x12\x14\n\x10EXTRA_FIRST_HALF\x10\x07\x12\x13\n\x0fEXTRA_HALF_TIME\x10\x08\x12\x19\n\x15EXTRA_SECOND_HALF_PRE\x10\t\x12\x15\n\x11EXTRA_SECOND_HALF\x10\n\x12\x1a\n\x16PENALTY_SHOOTOUT_BREAK\x10\x0b\x12\x14\n\x10PENALTY_SHOOTOUT\x10\x0c\x12\r\n\tPOST_GAME\x10\r"\xa4\x01\n\x0bOther_Infos\x12\x16\n\x0enum_of_cameras\x18\x01 \x02(\x05\x12\x19\n\x11num_of_our_robots\x18\x02 \x02(\x05\x12\x1b\n\x13num_of_enemy_robots\x18\x03 \x02(\x05\x12\x13\n\x0bsecperframe\x18\x04 \x02(\x02\x12\x16\n\x0eis_vision_recv\x18\x05 \x02(\x08\x12\x18\n\x10attack_direction\x18\x06 \x02(\x05"\xcf\x01\n\x0fRacoonMW_Packet\x12 \n\nour_robots\x18\x01 \x03(\x0b2\x0c.Robot_Infos\x12"\n\x0cenemy_robots\x18\x02 \x03(\x0b2\x0c.Robot_Infos\x12 \n\x08geometry\x18\x03 \x02(\x0b2\x0e.Geometry_Info\x12\x18\n\x04ball\x18\x04 \x02(\x0b2\n.Ball_Info\x12\x1e\n\x07referee\x18\x05 \x02(\x0b2\r.Referee_Info\x12\x1a\n\x04info\x18\x06 \x02(\x0b2\x0c.Other_InfosB-Z+github.com/Rione-SSL/RACOON-Pi/proto/pb_gen')
_ROBOT_INFOS = DESCRIPTOR.message_types_by_name['Robot_Infos']
_BALL_INFO = DESCRIPTOR.message_types_by_name['Ball_Info']
_GEOMETRY_INFO = DESCRIPTOR.message_types_by_name['Geometry_Info']
_REFEREE_INFO = DESCRIPTOR.message_types_by_name['Referee_Info']
_OTHER_INFOS = DESCRIPTOR.message_types_by_name['Other_Infos']
_RACOONMW_PACKET = DESCRIPTOR.message_types_by_name['RacoonMW_Packet']
_REFEREE_INFO_COMMAND = _REFEREE_INFO.enum_types_by_name['Command']
_REFEREE_INFO_STAGE = _REFEREE_INFO.enum_types_by_name['Stage']
Robot_Infos = _reflection.GeneratedProtocolMessageType('Robot_Infos', (_message.Message,), {'DESCRIPTOR': _ROBOT_INFOS, '__module__': 'to_racoonai_pb2'})
_sym_db.RegisterMessage(Robot_Infos)
Ball_Info = _reflection.GeneratedProtocolMessageType('Ball_Info', (_message.Message,), {'DESCRIPTOR': _BALL_INFO, '__module__': 'to_racoonai_pb2'})
_sym_db.RegisterMessage(Ball_Info)
Geometry_Info = _reflection.GeneratedProtocolMessageType('Geometry_Info', (_message.Message,), {'DESCRIPTOR': _GEOMETRY_INFO, '__module__': 'to_racoonai_pb2'})
_sym_db.RegisterMessage(Geometry_Info)
Referee_Info = _reflection.GeneratedProtocolMessageType('Referee_Info', (_message.Message,), {'DESCRIPTOR': _REFEREE_INFO, '__module__': 'to_racoonai_pb2'})
_sym_db.RegisterMessage(Referee_Info)
Other_Infos = _reflection.GeneratedProtocolMessageType('Other_Infos', (_message.Message,), {'DESCRIPTOR': _OTHER_INFOS, '__module__': 'to_racoonai_pb2'})
_sym_db.RegisterMessage(Other_Infos)
RacoonMW_Packet = _reflection.GeneratedProtocolMessageType('RacoonMW_Packet', (_message.Message,), {'DESCRIPTOR': _RACOONMW_PACKET, '__module__': 'to_racoonai_pb2'})
_sym_db.RegisterMessage(RacoonMW_Packet)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/Rione-SSL/RACOON-Pi/proto/pb_gen'
    _REFEREE_INFO_COMMAND.values_by_name['GOAL_YELLOW']._options = None
    _REFEREE_INFO_COMMAND.values_by_name['GOAL_YELLOW']._serialized_options = b'\x08\x01'
    _REFEREE_INFO_COMMAND.values_by_name['GOAL_BLUE']._options = None
    _REFEREE_INFO_COMMAND.values_by_name['GOAL_BLUE']._serialized_options = b'\x08\x01'
    _ROBOT_INFOS._serialized_start = 22
    _ROBOT_INFOS._serialized_end = 351
    _BALL_INFO._serialized_start = 354
    _BALL_INFO._serialized_end = 541
    _GEOMETRY_INFO._serialized_start = 544
    _GEOMETRY_INFO._serialized_end = 913
    _REFEREE_INFO._serialized_start = 916
    _REFEREE_INFO._serialized_end = 1929
    _REFEREE_INFO_COMMAND._serialized_start = 1191
    _REFEREE_INFO_COMMAND._serialized_end = 1589
    _REFEREE_INFO_STAGE._serialized_start = 1592
    _REFEREE_INFO_STAGE._serialized_end = 1929
    _OTHER_INFOS._serialized_start = 1932
    _OTHER_INFOS._serialized_end = 2096
    _RACOONMW_PACKET._serialized_start = 2099
    _RACOONMW_PACKET._serialized_end = 2306