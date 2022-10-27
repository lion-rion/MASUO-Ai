"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import ssl_gc_common_pb2 as ssl__gc__common__pb2
from . import ssl_gc_geometry_pb2 as ssl__gc__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17ssl_gc_game_event.proto\x1a\x13ssl_gc_common.proto\x1a\x15ssl_gc_geometry.proto"\xa4>\n\tGameEvent\x12\x1d\n\x04type\x18( \x01(\x0e2\x0f.GameEvent.Type\x12\x0e\n\x06origin\x18) \x03(\t\x12>\n\x1aball_left_field_touch_line\x18\x06 \x01(\x0b2\x18.GameEvent.BallLeftFieldH\x00\x12=\n\x19ball_left_field_goal_line\x18\x07 \x01(\x0b2\x18.GameEvent.BallLeftFieldH\x00\x12.\n\x0caimless_kick\x18\x0b \x01(\x0b2\x16.GameEvent.AimlessKickH\x00\x12V\n"attacker_too_close_to_defense_area\x18\x13 \x01(\x0b2(.GameEvent.AttackerTooCloseToDefenseAreaH\x00\x12D\n\x18defender_in_defense_area\x18\x1f \x01(\x0b2 .GameEvent.DefenderInDefenseAreaH\x00\x128\n\x11boundary_crossing\x18+ \x01(\x0b2\x1b.GameEvent.BoundaryCrossingH\x00\x125\n\x10keeper_held_ball\x18\r \x01(\x0b2\x19.GameEvent.KeeperHeldBallH\x00\x12E\n\x19bot_dribbled_ball_too_far\x18\x11 \x01(\x0b2 .GameEvent.BotDribbledBallTooFarH\x00\x121\n\x0ebot_pushed_bot\x18\x18 \x01(\x0b2\x17.GameEvent.BotPushedBotH\x00\x12H\n\x1abot_held_ball_deliberately\x18\x1a \x01(\x0b2".GameEvent.BotHeldBallDeliberatelyH\x00\x123\n\x0fbot_tipped_over\x18\x1b \x01(\x0b2\x18.GameEvent.BotTippedOverH\x00\x12\\\n%attacker_touched_ball_in_defense_area\x18\x0f \x01(\x0b2+.GameEvent.AttackerTouchedBallInDefenseAreaH\x00\x12C\n\x18bot_kicked_ball_too_fast\x18\x12 \x01(\x0b2\x1f.GameEvent.BotKickedBallTooFastH\x00\x125\n\x10bot_crash_unique\x18\x16 \x01(\x0b2\x19.GameEvent.BotCrashUniqueH\x00\x123\n\x0fbot_crash_drawn\x18\x15 \x01(\x0b2\x18.GameEvent.BotCrashDrawnH\x00\x12R\n defender_too_close_to_kick_point\x18\x1d \x01(\x0b2&.GameEvent.DefenderTooCloseToKickPointH\x00\x12;\n\x14bot_too_fast_in_stop\x18\x1c \x01(\x0b2\x1b.GameEvent.BotTooFastInStopH\x00\x12E\n\x18bot_interfered_placement\x18\x14 \x01(\x0b2!.GameEvent.BotInterferedPlacementH\x00\x12(\n\rpossible_goal\x18\' \x01(\x0b2\x0f.GameEvent.GoalH\x00\x12\x1f\n\x04goal\x18\x08 \x01(\x0b2\x0f.GameEvent.GoalH\x00\x12\'\n\x0cinvalid_goal\x18, \x01(\x0b2\x0f.GameEvent.GoalH\x00\x12L\n\x1cattacker_double_touched_ball\x18\x0e \x01(\x0b2$.GameEvent.AttackerDoubleTouchedBallH\x00\x12<\n\x13placement_succeeded\x18\x05 \x01(\x0b2\x1d.GameEvent.PlacementSucceededH\x00\x12;\n\x13penalty_kick_failed\x18- \x01(\x0b2\x1c.GameEvent.PenaltyKickFailedH\x00\x12:\n\x13no_progress_in_game\x18\x02 \x01(\x0b2\x1b.GameEvent.NoProgressInGameH\x00\x126\n\x10placement_failed\x18\x03 \x01(\x0b2\x1a.GameEvent.PlacementFailedH\x00\x122\n\x0emultiple_cards\x18  \x01(\x0b2\x18.GameEvent.MultipleCardsH\x00\x122\n\x0emultiple_fouls\x18" \x01(\x0b2\x18.GameEvent.MultipleFoulsH\x00\x126\n\x10bot_substitution\x18% \x01(\x0b2\x1a.GameEvent.BotSubstitutionH\x00\x123\n\x0ftoo_many_robots\x18& \x01(\x0b2\x18.GameEvent.TooManyRobotsH\x00\x122\n\x0echallenge_flag\x18. \x01(\x0b2\x18.GameEvent.ChallengeFlagH\x00\x122\n\x0eemergency_stop\x18/ \x01(\x0b2\x18.GameEvent.EmergencyStopH\x00\x12G\n\x19unsporting_behavior_minor\x18# \x01(\x0b2".GameEvent.UnsportingBehaviorMinorH\x00\x12G\n\x19unsporting_behavior_major\x18$ \x01(\x0b2".GameEvent.UnsportingBehaviorMajorH\x00\x12+\n\x08prepared\x18\x01 \x01(\x0b2\x13.GameEvent.PreparedB\x02\x18\x01H\x00\x124\n\rindirect_goal\x18\t \x01(\x0b2\x17.GameEvent.IndirectGoalB\x02\x18\x01H\x00\x122\n\x0cchipped_goal\x18\n \x01(\x0b2\x16.GameEvent.ChippedGoalB\x02\x18\x01H\x00\x122\n\x0ckick_timeout\x18\x0c \x01(\x0b2\x16.GameEvent.KickTimeoutB\x02\x18\x01H\x00\x12h\n)attacker_touched_opponent_in_defense_area\x18\x10 \x01(\x0b2/.GameEvent.AttackerTouchedOpponentInDefenseAreaB\x02\x18\x01H\x00\x12p\n1attacker_touched_opponent_in_defense_area_skipped\x18* \x01(\x0b2/.GameEvent.AttackerTouchedOpponentInDefenseAreaB\x02\x18\x01H\x00\x12A\n\x18bot_crash_unique_skipped\x18\x17 \x01(\x0b2\x19.GameEvent.BotCrashUniqueB\x02\x18\x01H\x00\x12=\n\x16bot_pushed_bot_skipped\x18\x19 \x01(\x0b2\x17.GameEvent.BotPushedBotB\x02\x18\x01H\x00\x12[\n"defender_in_defense_area_partially\x18\x1e \x01(\x0b2).GameEvent.DefenderInDefenseAreaPartiallyB\x02\x18\x01H\x00\x12O\n\x1bmultiple_placement_failures\x18! \x01(\x0b2$.GameEvent.MultiplePlacementFailuresB\x02\x18\x01H\x00\x1aS\n\rBallLeftField\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x1ar\n\x0bAimlessKick\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x1f\n\rkick_location\x18\x04 \x01(\x0b2\x08.Vector2\x1a\xef\x01\n\x04Goal\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x1b\n\x0ckicking_team\x18\x06 \x01(\x0e2\x05.Team\x12\x13\n\x0bkicking_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x1f\n\rkick_location\x18\x04 \x01(\x0b2\x08.Vector2\x12\x17\n\x0fmax_ball_height\x18\x05 \x01(\x02\x12\x1a\n\x12num_robots_by_team\x18\x07 \x01(\r\x12\x1a\n\x12last_touch_by_team\x18\x08 \x01(\x04\x12\x0f\n\x07message\x18\t \x01(\t\x1as\n\x0cIndirectGoal\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x1f\n\rkick_location\x18\x04 \x01(\x0b2\x08.Vector2\x1a\x8b\x01\n\x0bChippedGoal\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x1f\n\rkick_location\x18\x04 \x01(\x0b2\x08.Vector2\x12\x17\n\x0fmax_ball_height\x18\x05 \x01(\x02\x1ae\n\x10BotTooFastInStop\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\r\n\x05speed\x18\x04 \x01(\x02\x1as\n\x1bDefenderTooCloseToKickPoint\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x10\n\x08distance\x18\x04 \x01(\x02\x1a\x8f\x01\n\rBotCrashDrawn\x12\x12\n\nbot_yellow\x18\x01 \x01(\r\x12\x10\n\x08bot_blue\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x13\n\x0bcrash_speed\x18\x04 \x01(\x02\x12\x12\n\nspeed_diff\x18\x05 \x01(\x02\x12\x13\n\x0bcrash_angle\x18\x06 \x01(\x02\x1a\xa4\x01\n\x0eBotCrashUnique\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x10\n\x08violator\x18\x02 \x01(\r\x12\x0e\n\x06victim\x18\x03 \x01(\r\x12\x1a\n\x08location\x18\x04 \x01(\x0b2\x08.Vector2\x12\x13\n\x0bcrash_speed\x18\x05 \x01(\x02\x12\x12\n\nspeed_diff\x18\x06 \x01(\x02\x12\x13\n\x0bcrash_angle\x18\x07 \x01(\x02\x1a}\n\x0cBotPushedBot\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x10\n\x08violator\x18\x02 \x01(\r\x12\x0e\n\x06victim\x18\x03 \x01(\r\x12\x1a\n\x08location\x18\x04 \x01(\x0b2\x08.Vector2\x12\x17\n\x0fpushed_distance\x18\x05 \x01(\x02\x1at\n\rBotTippedOver\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x1f\n\rball_location\x18\x04 \x01(\x0b2\x08.Vector2\x1am\n\x15DefenderInDefenseArea\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x10\n\x08distance\x18\x04 \x01(\x02\x1a\x97\x01\n\x1eDefenderInDefenseAreaPartially\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x10\n\x08distance\x18\x04 \x01(\x02\x12\x1f\n\rball_location\x18\x05 \x01(\x0b2\x08.Vector2\x1ax\n AttackerTouchedBallInDefenseArea\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x10\n\x08distance\x18\x04 \x01(\x02\x1a\x87\x01\n\x14BotKickedBallTooFast\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x1a\n\x12initial_ball_speed\x18\x04 \x01(\x02\x12\x0f\n\x07chipped\x18\x05 \x01(\x08\x1ao\n\x15BotDribbledBallTooFar\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x17\n\x05start\x18\x03 \x01(\x0b2\x08.Vector2\x12\x15\n\x03end\x18\x04 \x01(\x0b2\x08.Vector2\x1az\n$AttackerTouchedOpponentInDefenseArea\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x0e\n\x06victim\x18\x04 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x1a_\n\x19AttackerDoubleTouchedBall\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x1a\x96\x01\n\x1dAttackerTooCloseToDefenseArea\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x10\n\x08distance\x18\x04 \x01(\x02\x12\x1f\n\rball_location\x18\x05 \x01(\x0b2\x08.Vector2\x1ao\n\x17BotHeldBallDeliberately\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x12\x10\n\x08duration\x18\x04 \x01(\x02\x1a\\\n\x16BotInterferedPlacement\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06by_bot\x18\x02 \x01(\r\x12\x1a\n\x08location\x18\x03 \x01(\x0b2\x08.Vector2\x1a\'\n\rMultipleCards\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x1aO\n\rMultipleFouls\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12&\n\x12caused_game_events\x18\x02 \x03(\x0b2\n.GameEvent\x1a3\n\x19MultiplePlacementFailures\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x1aO\n\x0bKickTimeout\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x1a\n\x08location\x18\x02 \x01(\x0b2\x08.Vector2\x12\x0c\n\x04time\x18\x03 \x01(\x02\x1a<\n\x10NoProgressInGame\x12\x1a\n\x08location\x18\x01 \x01(\x0b2\x08.Vector2\x12\x0c\n\x04time\x18\x02 \x01(\x02\x1aE\n\x0fPlacementFailed\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x1a\n\x12remaining_distance\x18\x02 \x01(\x02\x1aA\n\x17UnsportingBehaviorMinor\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06reason\x18\x02 \x02(\t\x1aA\n\x17UnsportingBehaviorMajor\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x0e\n\x06reason\x18\x02 \x02(\t\x1aV\n\x0eKeeperHeldBall\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x1a\n\x08location\x18\x02 \x01(\x0b2\x08.Vector2\x12\x10\n\x08duration\x18\x03 \x01(\x02\x1ae\n\x12PlacementSucceeded\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x12\n\ntime_taken\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x10\n\x08distance\x18\x04 \x01(\x02\x1a\x1e\n\x08Prepared\x12\x12\n\ntime_taken\x18\x01 \x01(\x02\x1a)\n\x0fBotSubstitution\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x1a\'\n\rChallengeFlag\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x1a\'\n\rEmergencyStop\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x1a\x81\x01\n\rTooManyRobots\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x1a\n\x12num_robots_allowed\x18\x02 \x01(\x05\x12\x1b\n\x13num_robots_on_field\x18\x03 \x01(\x05\x12\x1f\n\rball_location\x18\x04 \x01(\x0b2\x08.Vector2\x1aF\n\x10BoundaryCrossing\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x1a\n\x08location\x18\x02 \x01(\x0b2\x08.Vector2\x1aG\n\x11PenaltyKickFailed\x12\x16\n\x07by_team\x18\x01 \x02(\x0e2\x05.Team\x12\x1a\n\x08location\x18\x02 \x01(\x0b2\x08.Vector2"\xe2\t\n\x04Type\x12\x1b\n\x17UNKNOWN_GAME_EVENT_TYPE\x10\x00\x12\x1e\n\x1aBALL_LEFT_FIELD_TOUCH_LINE\x10\x06\x12\x1d\n\x19BALL_LEFT_FIELD_GOAL_LINE\x10\x07\x12\x10\n\x0cAIMLESS_KICK\x10\x0b\x12&\n"ATTACKER_TOO_CLOSE_TO_DEFENSE_AREA\x10\x13\x12\x1c\n\x18DEFENDER_IN_DEFENSE_AREA\x10\x1f\x12\x15\n\x11BOUNDARY_CROSSING\x10)\x12\x14\n\x10KEEPER_HELD_BALL\x10\r\x12\x1d\n\x19BOT_DRIBBLED_BALL_TOO_FAR\x10\x11\x12\x12\n\x0eBOT_PUSHED_BOT\x10\x18\x12\x1e\n\x1aBOT_HELD_BALL_DELIBERATELY\x10\x1a\x12\x13\n\x0fBOT_TIPPED_OVER\x10\x1b\x12)\n%ATTACKER_TOUCHED_BALL_IN_DEFENSE_AREA\x10\x0f\x12\x1c\n\x18BOT_KICKED_BALL_TOO_FAST\x10\x12\x12\x14\n\x10BOT_CRASH_UNIQUE\x10\x16\x12\x13\n\x0fBOT_CRASH_DRAWN\x10\x15\x12$\n DEFENDER_TOO_CLOSE_TO_KICK_POINT\x10\x1d\x12\x18\n\x14BOT_TOO_FAST_IN_STOP\x10\x1c\x12\x1c\n\x18BOT_INTERFERED_PLACEMENT\x10\x14\x12\x11\n\rPOSSIBLE_GOAL\x10\'\x12\x08\n\x04GOAL\x10\x08\x12\x10\n\x0cINVALID_GOAL\x10*\x12 \n\x1cATTACKER_DOUBLE_TOUCHED_BALL\x10\x0e\x12\x17\n\x13PLACEMENT_SUCCEEDED\x10\x05\x12\x17\n\x13PENALTY_KICK_FAILED\x10+\x12\x17\n\x13NO_PROGRESS_IN_GAME\x10\x02\x12\x14\n\x10PLACEMENT_FAILED\x10\x03\x12\x12\n\x0eMULTIPLE_CARDS\x10 \x12\x12\n\x0eMULTIPLE_FOULS\x10"\x12\x14\n\x10BOT_SUBSTITUTION\x10%\x12\x13\n\x0fTOO_MANY_ROBOTS\x10&\x12\x12\n\x0eCHALLENGE_FLAG\x10,\x12\x12\n\x0eEMERGENCY_STOP\x10-\x12\x1d\n\x19UNSPORTING_BEHAVIOR_MINOR\x10#\x12\x1d\n\x19UNSPORTING_BEHAVIOR_MAJOR\x10$\x12\x10\n\x08PREPARED\x10\x01\x1a\x02\x08\x01\x12\x15\n\rINDIRECT_GOAL\x10\t\x1a\x02\x08\x01\x12\x14\n\x0cCHIPPED_GOAL\x10\n\x1a\x02\x08\x01\x12\x14\n\x0cKICK_TIMEOUT\x10\x0c\x1a\x02\x08\x01\x121\n)ATTACKER_TOUCHED_OPPONENT_IN_DEFENSE_AREA\x10\x10\x1a\x02\x08\x01\x129\n1ATTACKER_TOUCHED_OPPONENT_IN_DEFENSE_AREA_SKIPPED\x10(\x1a\x02\x08\x01\x12 \n\x18BOT_CRASH_UNIQUE_SKIPPED\x10\x17\x1a\x02\x08\x01\x12\x1e\n\x16BOT_PUSHED_BOT_SKIPPED\x10\x19\x1a\x02\x08\x01\x12*\n"DEFENDER_IN_DEFENSE_AREA_PARTIALLY\x10\x1e\x1a\x02\x08\x01\x12#\n\x1bMULTIPLE_PLACEMENT_FAILURES\x10!\x1a\x02\x08\x01B\x07\n\x05eventB?Z=github.com/RoboCup-SSL/ssl-game-controller/internal/app/state')
_GAMEEVENT = DESCRIPTOR.message_types_by_name['GameEvent']
_GAMEEVENT_BALLLEFTFIELD = _GAMEEVENT.nested_types_by_name['BallLeftField']
_GAMEEVENT_AIMLESSKICK = _GAMEEVENT.nested_types_by_name['AimlessKick']
_GAMEEVENT_GOAL = _GAMEEVENT.nested_types_by_name['Goal']
_GAMEEVENT_INDIRECTGOAL = _GAMEEVENT.nested_types_by_name['IndirectGoal']
_GAMEEVENT_CHIPPEDGOAL = _GAMEEVENT.nested_types_by_name['ChippedGoal']
_GAMEEVENT_BOTTOOFASTINSTOP = _GAMEEVENT.nested_types_by_name['BotTooFastInStop']
_GAMEEVENT_DEFENDERTOOCLOSETOKICKPOINT = _GAMEEVENT.nested_types_by_name['DefenderTooCloseToKickPoint']
_GAMEEVENT_BOTCRASHDRAWN = _GAMEEVENT.nested_types_by_name['BotCrashDrawn']
_GAMEEVENT_BOTCRASHUNIQUE = _GAMEEVENT.nested_types_by_name['BotCrashUnique']
_GAMEEVENT_BOTPUSHEDBOT = _GAMEEVENT.nested_types_by_name['BotPushedBot']
_GAMEEVENT_BOTTIPPEDOVER = _GAMEEVENT.nested_types_by_name['BotTippedOver']
_GAMEEVENT_DEFENDERINDEFENSEAREA = _GAMEEVENT.nested_types_by_name['DefenderInDefenseArea']
_GAMEEVENT_DEFENDERINDEFENSEAREAPARTIALLY = _GAMEEVENT.nested_types_by_name['DefenderInDefenseAreaPartially']
_GAMEEVENT_ATTACKERTOUCHEDBALLINDEFENSEAREA = _GAMEEVENT.nested_types_by_name['AttackerTouchedBallInDefenseArea']
_GAMEEVENT_BOTKICKEDBALLTOOFAST = _GAMEEVENT.nested_types_by_name['BotKickedBallTooFast']
_GAMEEVENT_BOTDRIBBLEDBALLTOOFAR = _GAMEEVENT.nested_types_by_name['BotDribbledBallTooFar']
_GAMEEVENT_ATTACKERTOUCHEDOPPONENTINDEFENSEAREA = _GAMEEVENT.nested_types_by_name['AttackerTouchedOpponentInDefenseArea']
_GAMEEVENT_ATTACKERDOUBLETOUCHEDBALL = _GAMEEVENT.nested_types_by_name['AttackerDoubleTouchedBall']
_GAMEEVENT_ATTACKERTOOCLOSETODEFENSEAREA = _GAMEEVENT.nested_types_by_name['AttackerTooCloseToDefenseArea']
_GAMEEVENT_BOTHELDBALLDELIBERATELY = _GAMEEVENT.nested_types_by_name['BotHeldBallDeliberately']
_GAMEEVENT_BOTINTERFEREDPLACEMENT = _GAMEEVENT.nested_types_by_name['BotInterferedPlacement']
_GAMEEVENT_MULTIPLECARDS = _GAMEEVENT.nested_types_by_name['MultipleCards']
_GAMEEVENT_MULTIPLEFOULS = _GAMEEVENT.nested_types_by_name['MultipleFouls']
_GAMEEVENT_MULTIPLEPLACEMENTFAILURES = _GAMEEVENT.nested_types_by_name['MultiplePlacementFailures']
_GAMEEVENT_KICKTIMEOUT = _GAMEEVENT.nested_types_by_name['KickTimeout']
_GAMEEVENT_NOPROGRESSINGAME = _GAMEEVENT.nested_types_by_name['NoProgressInGame']
_GAMEEVENT_PLACEMENTFAILED = _GAMEEVENT.nested_types_by_name['PlacementFailed']
_GAMEEVENT_UNSPORTINGBEHAVIORMINOR = _GAMEEVENT.nested_types_by_name['UnsportingBehaviorMinor']
_GAMEEVENT_UNSPORTINGBEHAVIORMAJOR = _GAMEEVENT.nested_types_by_name['UnsportingBehaviorMajor']
_GAMEEVENT_KEEPERHELDBALL = _GAMEEVENT.nested_types_by_name['KeeperHeldBall']
_GAMEEVENT_PLACEMENTSUCCEEDED = _GAMEEVENT.nested_types_by_name['PlacementSucceeded']
_GAMEEVENT_PREPARED = _GAMEEVENT.nested_types_by_name['Prepared']
_GAMEEVENT_BOTSUBSTITUTION = _GAMEEVENT.nested_types_by_name['BotSubstitution']
_GAMEEVENT_CHALLENGEFLAG = _GAMEEVENT.nested_types_by_name['ChallengeFlag']
_GAMEEVENT_EMERGENCYSTOP = _GAMEEVENT.nested_types_by_name['EmergencyStop']
_GAMEEVENT_TOOMANYROBOTS = _GAMEEVENT.nested_types_by_name['TooManyRobots']
_GAMEEVENT_BOUNDARYCROSSING = _GAMEEVENT.nested_types_by_name['BoundaryCrossing']
_GAMEEVENT_PENALTYKICKFAILED = _GAMEEVENT.nested_types_by_name['PenaltyKickFailed']
_GAMEEVENT_TYPE = _GAMEEVENT.enum_types_by_name['Type']
GameEvent = _reflection.GeneratedProtocolMessageType('GameEvent', (_message.Message,), {'BallLeftField': _reflection.GeneratedProtocolMessageType('BallLeftField', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BALLLEFTFIELD, '__module__': 'ssl_gc_game_event_pb2'}), 'AimlessKick': _reflection.GeneratedProtocolMessageType('AimlessKick', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_AIMLESSKICK, '__module__': 'ssl_gc_game_event_pb2'}), 'Goal': _reflection.GeneratedProtocolMessageType('Goal', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_GOAL, '__module__': 'ssl_gc_game_event_pb2'}), 'IndirectGoal': _reflection.GeneratedProtocolMessageType('IndirectGoal', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_INDIRECTGOAL, '__module__': 'ssl_gc_game_event_pb2'}), 'ChippedGoal': _reflection.GeneratedProtocolMessageType('ChippedGoal', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_CHIPPEDGOAL, '__module__': 'ssl_gc_game_event_pb2'}), 'BotTooFastInStop': _reflection.GeneratedProtocolMessageType('BotTooFastInStop', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTTOOFASTINSTOP, '__module__': 'ssl_gc_game_event_pb2'}), 'DefenderTooCloseToKickPoint': _reflection.GeneratedProtocolMessageType('DefenderTooCloseToKickPoint', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_DEFENDERTOOCLOSETOKICKPOINT, '__module__': 'ssl_gc_game_event_pb2'}), 'BotCrashDrawn': _reflection.GeneratedProtocolMessageType('BotCrashDrawn', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTCRASHDRAWN, '__module__': 'ssl_gc_game_event_pb2'}), 'BotCrashUnique': _reflection.GeneratedProtocolMessageType('BotCrashUnique', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTCRASHUNIQUE, '__module__': 'ssl_gc_game_event_pb2'}), 'BotPushedBot': _reflection.GeneratedProtocolMessageType('BotPushedBot', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTPUSHEDBOT, '__module__': 'ssl_gc_game_event_pb2'}), 'BotTippedOver': _reflection.GeneratedProtocolMessageType('BotTippedOver', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTTIPPEDOVER, '__module__': 'ssl_gc_game_event_pb2'}), 'DefenderInDefenseArea': _reflection.GeneratedProtocolMessageType('DefenderInDefenseArea', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_DEFENDERINDEFENSEAREA, '__module__': 'ssl_gc_game_event_pb2'}), 'DefenderInDefenseAreaPartially': _reflection.GeneratedProtocolMessageType('DefenderInDefenseAreaPartially', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_DEFENDERINDEFENSEAREAPARTIALLY, '__module__': 'ssl_gc_game_event_pb2'}), 'AttackerTouchedBallInDefenseArea': _reflection.GeneratedProtocolMessageType('AttackerTouchedBallInDefenseArea', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_ATTACKERTOUCHEDBALLINDEFENSEAREA, '__module__': 'ssl_gc_game_event_pb2'}), 'BotKickedBallTooFast': _reflection.GeneratedProtocolMessageType('BotKickedBallTooFast', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTKICKEDBALLTOOFAST, '__module__': 'ssl_gc_game_event_pb2'}), 'BotDribbledBallTooFar': _reflection.GeneratedProtocolMessageType('BotDribbledBallTooFar', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTDRIBBLEDBALLTOOFAR, '__module__': 'ssl_gc_game_event_pb2'}), 'AttackerTouchedOpponentInDefenseArea': _reflection.GeneratedProtocolMessageType('AttackerTouchedOpponentInDefenseArea', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_ATTACKERTOUCHEDOPPONENTINDEFENSEAREA, '__module__': 'ssl_gc_game_event_pb2'}), 'AttackerDoubleTouchedBall': _reflection.GeneratedProtocolMessageType('AttackerDoubleTouchedBall', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_ATTACKERDOUBLETOUCHEDBALL, '__module__': 'ssl_gc_game_event_pb2'}), 'AttackerTooCloseToDefenseArea': _reflection.GeneratedProtocolMessageType('AttackerTooCloseToDefenseArea', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_ATTACKERTOOCLOSETODEFENSEAREA, '__module__': 'ssl_gc_game_event_pb2'}), 'BotHeldBallDeliberately': _reflection.GeneratedProtocolMessageType('BotHeldBallDeliberately', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTHELDBALLDELIBERATELY, '__module__': 'ssl_gc_game_event_pb2'}), 'BotInterferedPlacement': _reflection.GeneratedProtocolMessageType('BotInterferedPlacement', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTINTERFEREDPLACEMENT, '__module__': 'ssl_gc_game_event_pb2'}), 'MultipleCards': _reflection.GeneratedProtocolMessageType('MultipleCards', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_MULTIPLECARDS, '__module__': 'ssl_gc_game_event_pb2'}), 'MultipleFouls': _reflection.GeneratedProtocolMessageType('MultipleFouls', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_MULTIPLEFOULS, '__module__': 'ssl_gc_game_event_pb2'}), 'MultiplePlacementFailures': _reflection.GeneratedProtocolMessageType('MultiplePlacementFailures', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_MULTIPLEPLACEMENTFAILURES, '__module__': 'ssl_gc_game_event_pb2'}), 'KickTimeout': _reflection.GeneratedProtocolMessageType('KickTimeout', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_KICKTIMEOUT, '__module__': 'ssl_gc_game_event_pb2'}), 'NoProgressInGame': _reflection.GeneratedProtocolMessageType('NoProgressInGame', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_NOPROGRESSINGAME, '__module__': 'ssl_gc_game_event_pb2'}), 'PlacementFailed': _reflection.GeneratedProtocolMessageType('PlacementFailed', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_PLACEMENTFAILED, '__module__': 'ssl_gc_game_event_pb2'}), 'UnsportingBehaviorMinor': _reflection.GeneratedProtocolMessageType('UnsportingBehaviorMinor', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_UNSPORTINGBEHAVIORMINOR, '__module__': 'ssl_gc_game_event_pb2'}), 'UnsportingBehaviorMajor': _reflection.GeneratedProtocolMessageType('UnsportingBehaviorMajor', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_UNSPORTINGBEHAVIORMAJOR, '__module__': 'ssl_gc_game_event_pb2'}), 'KeeperHeldBall': _reflection.GeneratedProtocolMessageType('KeeperHeldBall', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_KEEPERHELDBALL, '__module__': 'ssl_gc_game_event_pb2'}), 'PlacementSucceeded': _reflection.GeneratedProtocolMessageType('PlacementSucceeded', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_PLACEMENTSUCCEEDED, '__module__': 'ssl_gc_game_event_pb2'}), 'Prepared': _reflection.GeneratedProtocolMessageType('Prepared', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_PREPARED, '__module__': 'ssl_gc_game_event_pb2'}), 'BotSubstitution': _reflection.GeneratedProtocolMessageType('BotSubstitution', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOTSUBSTITUTION, '__module__': 'ssl_gc_game_event_pb2'}), 'ChallengeFlag': _reflection.GeneratedProtocolMessageType('ChallengeFlag', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_CHALLENGEFLAG, '__module__': 'ssl_gc_game_event_pb2'}), 'EmergencyStop': _reflection.GeneratedProtocolMessageType('EmergencyStop', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_EMERGENCYSTOP, '__module__': 'ssl_gc_game_event_pb2'}), 'TooManyRobots': _reflection.GeneratedProtocolMessageType('TooManyRobots', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_TOOMANYROBOTS, '__module__': 'ssl_gc_game_event_pb2'}), 'BoundaryCrossing': _reflection.GeneratedProtocolMessageType('BoundaryCrossing', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_BOUNDARYCROSSING, '__module__': 'ssl_gc_game_event_pb2'}), 'PenaltyKickFailed': _reflection.GeneratedProtocolMessageType('PenaltyKickFailed', (_message.Message,), {'DESCRIPTOR': _GAMEEVENT_PENALTYKICKFAILED, '__module__': 'ssl_gc_game_event_pb2'}), 'DESCRIPTOR': _GAMEEVENT, '__module__': 'ssl_gc_game_event_pb2'})
_sym_db.RegisterMessage(GameEvent)
_sym_db.RegisterMessage(GameEvent.BallLeftField)
_sym_db.RegisterMessage(GameEvent.AimlessKick)
_sym_db.RegisterMessage(GameEvent.Goal)
_sym_db.RegisterMessage(GameEvent.IndirectGoal)
_sym_db.RegisterMessage(GameEvent.ChippedGoal)
_sym_db.RegisterMessage(GameEvent.BotTooFastInStop)
_sym_db.RegisterMessage(GameEvent.DefenderTooCloseToKickPoint)
_sym_db.RegisterMessage(GameEvent.BotCrashDrawn)
_sym_db.RegisterMessage(GameEvent.BotCrashUnique)
_sym_db.RegisterMessage(GameEvent.BotPushedBot)
_sym_db.RegisterMessage(GameEvent.BotTippedOver)
_sym_db.RegisterMessage(GameEvent.DefenderInDefenseArea)
_sym_db.RegisterMessage(GameEvent.DefenderInDefenseAreaPartially)
_sym_db.RegisterMessage(GameEvent.AttackerTouchedBallInDefenseArea)
_sym_db.RegisterMessage(GameEvent.BotKickedBallTooFast)
_sym_db.RegisterMessage(GameEvent.BotDribbledBallTooFar)
_sym_db.RegisterMessage(GameEvent.AttackerTouchedOpponentInDefenseArea)
_sym_db.RegisterMessage(GameEvent.AttackerDoubleTouchedBall)
_sym_db.RegisterMessage(GameEvent.AttackerTooCloseToDefenseArea)
_sym_db.RegisterMessage(GameEvent.BotHeldBallDeliberately)
_sym_db.RegisterMessage(GameEvent.BotInterferedPlacement)
_sym_db.RegisterMessage(GameEvent.MultipleCards)
_sym_db.RegisterMessage(GameEvent.MultipleFouls)
_sym_db.RegisterMessage(GameEvent.MultiplePlacementFailures)
_sym_db.RegisterMessage(GameEvent.KickTimeout)
_sym_db.RegisterMessage(GameEvent.NoProgressInGame)
_sym_db.RegisterMessage(GameEvent.PlacementFailed)
_sym_db.RegisterMessage(GameEvent.UnsportingBehaviorMinor)
_sym_db.RegisterMessage(GameEvent.UnsportingBehaviorMajor)
_sym_db.RegisterMessage(GameEvent.KeeperHeldBall)
_sym_db.RegisterMessage(GameEvent.PlacementSucceeded)
_sym_db.RegisterMessage(GameEvent.Prepared)
_sym_db.RegisterMessage(GameEvent.BotSubstitution)
_sym_db.RegisterMessage(GameEvent.ChallengeFlag)
_sym_db.RegisterMessage(GameEvent.EmergencyStop)
_sym_db.RegisterMessage(GameEvent.TooManyRobots)
_sym_db.RegisterMessage(GameEvent.BoundaryCrossing)
_sym_db.RegisterMessage(GameEvent.PenaltyKickFailed)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/RoboCup-SSL/ssl-game-controller/internal/app/state'
    _GAMEEVENT_TYPE.values_by_name['PREPARED']._options = None
    _GAMEEVENT_TYPE.values_by_name['PREPARED']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['INDIRECT_GOAL']._options = None
    _GAMEEVENT_TYPE.values_by_name['INDIRECT_GOAL']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['CHIPPED_GOAL']._options = None
    _GAMEEVENT_TYPE.values_by_name['CHIPPED_GOAL']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['KICK_TIMEOUT']._options = None
    _GAMEEVENT_TYPE.values_by_name['KICK_TIMEOUT']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['ATTACKER_TOUCHED_OPPONENT_IN_DEFENSE_AREA']._options = None
    _GAMEEVENT_TYPE.values_by_name['ATTACKER_TOUCHED_OPPONENT_IN_DEFENSE_AREA']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['ATTACKER_TOUCHED_OPPONENT_IN_DEFENSE_AREA_SKIPPED']._options = None
    _GAMEEVENT_TYPE.values_by_name['ATTACKER_TOUCHED_OPPONENT_IN_DEFENSE_AREA_SKIPPED']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['BOT_CRASH_UNIQUE_SKIPPED']._options = None
    _GAMEEVENT_TYPE.values_by_name['BOT_CRASH_UNIQUE_SKIPPED']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['BOT_PUSHED_BOT_SKIPPED']._options = None
    _GAMEEVENT_TYPE.values_by_name['BOT_PUSHED_BOT_SKIPPED']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['DEFENDER_IN_DEFENSE_AREA_PARTIALLY']._options = None
    _GAMEEVENT_TYPE.values_by_name['DEFENDER_IN_DEFENSE_AREA_PARTIALLY']._serialized_options = b'\x08\x01'
    _GAMEEVENT_TYPE.values_by_name['MULTIPLE_PLACEMENT_FAILURES']._options = None
    _GAMEEVENT_TYPE.values_by_name['MULTIPLE_PLACEMENT_FAILURES']._serialized_options = b'\x08\x01'
    _GAMEEVENT.fields_by_name['prepared']._options = None
    _GAMEEVENT.fields_by_name['prepared']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['indirect_goal']._options = None
    _GAMEEVENT.fields_by_name['indirect_goal']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['chipped_goal']._options = None
    _GAMEEVENT.fields_by_name['chipped_goal']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['kick_timeout']._options = None
    _GAMEEVENT.fields_by_name['kick_timeout']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['attacker_touched_opponent_in_defense_area']._options = None
    _GAMEEVENT.fields_by_name['attacker_touched_opponent_in_defense_area']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['attacker_touched_opponent_in_defense_area_skipped']._options = None
    _GAMEEVENT.fields_by_name['attacker_touched_opponent_in_defense_area_skipped']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['bot_crash_unique_skipped']._options = None
    _GAMEEVENT.fields_by_name['bot_crash_unique_skipped']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['bot_pushed_bot_skipped']._options = None
    _GAMEEVENT.fields_by_name['bot_pushed_bot_skipped']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['defender_in_defense_area_partially']._options = None
    _GAMEEVENT.fields_by_name['defender_in_defense_area_partially']._serialized_options = b'\x18\x01'
    _GAMEEVENT.fields_by_name['multiple_placement_failures']._options = None
    _GAMEEVENT.fields_by_name['multiple_placement_failures']._serialized_options = b'\x18\x01'
    _GAMEEVENT._serialized_start = 72
    _GAMEEVENT._serialized_end = 8044
    _GAMEEVENT_BALLLEFTFIELD._serialized_start = 2937
    _GAMEEVENT_BALLLEFTFIELD._serialized_end = 3020
    _GAMEEVENT_AIMLESSKICK._serialized_start = 3022
    _GAMEEVENT_AIMLESSKICK._serialized_end = 3136
    _GAMEEVENT_GOAL._serialized_start = 3139
    _GAMEEVENT_GOAL._serialized_end = 3378
    _GAMEEVENT_INDIRECTGOAL._serialized_start = 3380
    _GAMEEVENT_INDIRECTGOAL._serialized_end = 3495
    _GAMEEVENT_CHIPPEDGOAL._serialized_start = 3498
    _GAMEEVENT_CHIPPEDGOAL._serialized_end = 3637
    _GAMEEVENT_BOTTOOFASTINSTOP._serialized_start = 3639
    _GAMEEVENT_BOTTOOFASTINSTOP._serialized_end = 3740
    _GAMEEVENT_DEFENDERTOOCLOSETOKICKPOINT._serialized_start = 3742
    _GAMEEVENT_DEFENDERTOOCLOSETOKICKPOINT._serialized_end = 3857
    _GAMEEVENT_BOTCRASHDRAWN._serialized_start = 3860
    _GAMEEVENT_BOTCRASHDRAWN._serialized_end = 4003
    _GAMEEVENT_BOTCRASHUNIQUE._serialized_start = 4006
    _GAMEEVENT_BOTCRASHUNIQUE._serialized_end = 4170
    _GAMEEVENT_BOTPUSHEDBOT._serialized_start = 4172
    _GAMEEVENT_BOTPUSHEDBOT._serialized_end = 4297
    _GAMEEVENT_BOTTIPPEDOVER._serialized_start = 4299
    _GAMEEVENT_BOTTIPPEDOVER._serialized_end = 4415
    _GAMEEVENT_DEFENDERINDEFENSEAREA._serialized_start = 4417
    _GAMEEVENT_DEFENDERINDEFENSEAREA._serialized_end = 4526
    _GAMEEVENT_DEFENDERINDEFENSEAREAPARTIALLY._serialized_start = 4529
    _GAMEEVENT_DEFENDERINDEFENSEAREAPARTIALLY._serialized_end = 4680
    _GAMEEVENT_ATTACKERTOUCHEDBALLINDEFENSEAREA._serialized_start = 4682
    _GAMEEVENT_ATTACKERTOUCHEDBALLINDEFENSEAREA._serialized_end = 4802
    _GAMEEVENT_BOTKICKEDBALLTOOFAST._serialized_start = 4805
    _GAMEEVENT_BOTKICKEDBALLTOOFAST._serialized_end = 4940
    _GAMEEVENT_BOTDRIBBLEDBALLTOOFAR._serialized_start = 4942
    _GAMEEVENT_BOTDRIBBLEDBALLTOOFAR._serialized_end = 5053
    _GAMEEVENT_ATTACKERTOUCHEDOPPONENTINDEFENSEAREA._serialized_start = 5055
    _GAMEEVENT_ATTACKERTOUCHEDOPPONENTINDEFENSEAREA._serialized_end = 5177
    _GAMEEVENT_ATTACKERDOUBLETOUCHEDBALL._serialized_start = 5179
    _GAMEEVENT_ATTACKERDOUBLETOUCHEDBALL._serialized_end = 5274
    _GAMEEVENT_ATTACKERTOOCLOSETODEFENSEAREA._serialized_start = 5277
    _GAMEEVENT_ATTACKERTOOCLOSETODEFENSEAREA._serialized_end = 5427
    _GAMEEVENT_BOTHELDBALLDELIBERATELY._serialized_start = 5429
    _GAMEEVENT_BOTHELDBALLDELIBERATELY._serialized_end = 5540
    _GAMEEVENT_BOTINTERFEREDPLACEMENT._serialized_start = 5542
    _GAMEEVENT_BOTINTERFEREDPLACEMENT._serialized_end = 5634
    _GAMEEVENT_MULTIPLECARDS._serialized_start = 5636
    _GAMEEVENT_MULTIPLECARDS._serialized_end = 5675
    _GAMEEVENT_MULTIPLEFOULS._serialized_start = 5677
    _GAMEEVENT_MULTIPLEFOULS._serialized_end = 5756
    _GAMEEVENT_MULTIPLEPLACEMENTFAILURES._serialized_start = 5758
    _GAMEEVENT_MULTIPLEPLACEMENTFAILURES._serialized_end = 5809
    _GAMEEVENT_KICKTIMEOUT._serialized_start = 5811
    _GAMEEVENT_KICKTIMEOUT._serialized_end = 5890
    _GAMEEVENT_NOPROGRESSINGAME._serialized_start = 5892
    _GAMEEVENT_NOPROGRESSINGAME._serialized_end = 5952
    _GAMEEVENT_PLACEMENTFAILED._serialized_start = 5954
    _GAMEEVENT_PLACEMENTFAILED._serialized_end = 6023
    _GAMEEVENT_UNSPORTINGBEHAVIORMINOR._serialized_start = 6025
    _GAMEEVENT_UNSPORTINGBEHAVIORMINOR._serialized_end = 6090
    _GAMEEVENT_UNSPORTINGBEHAVIORMAJOR._serialized_start = 6092
    _GAMEEVENT_UNSPORTINGBEHAVIORMAJOR._serialized_end = 6157
    _GAMEEVENT_KEEPERHELDBALL._serialized_start = 6159
    _GAMEEVENT_KEEPERHELDBALL._serialized_end = 6245
    _GAMEEVENT_PLACEMENTSUCCEEDED._serialized_start = 6247
    _GAMEEVENT_PLACEMENTSUCCEEDED._serialized_end = 6348
    _GAMEEVENT_PREPARED._serialized_start = 6350
    _GAMEEVENT_PREPARED._serialized_end = 6380
    _GAMEEVENT_BOTSUBSTITUTION._serialized_start = 6382
    _GAMEEVENT_BOTSUBSTITUTION._serialized_end = 6423
    _GAMEEVENT_CHALLENGEFLAG._serialized_start = 6425
    _GAMEEVENT_CHALLENGEFLAG._serialized_end = 6464
    _GAMEEVENT_EMERGENCYSTOP._serialized_start = 6466
    _GAMEEVENT_EMERGENCYSTOP._serialized_end = 6505
    _GAMEEVENT_TOOMANYROBOTS._serialized_start = 6508
    _GAMEEVENT_TOOMANYROBOTS._serialized_end = 6637
    _GAMEEVENT_BOUNDARYCROSSING._serialized_start = 6639
    _GAMEEVENT_BOUNDARYCROSSING._serialized_end = 6709
    _GAMEEVENT_PENALTYKICKFAILED._serialized_start = 6711
    _GAMEEVENT_PENALTYKICKFAILED._serialized_end = 6782
    _GAMEEVENT_TYPE._serialized_start = 6785
    _GAMEEVENT_TYPE._serialized_end = 8035