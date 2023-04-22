from rlgym.utils.reward_functions import CombinedReward
from rlgym.utils.reward_functions.common_rewards import EventReward, TouchBallReward, SaveBoostReward, BallYCoordinateReward, VelocityBallToGoalReward, RewardIfClosestToBall, RewardIfTouchedLast, ConstantReward, FaceBallReward

class BotNameRewards():
    def __init__(self):
        self.weights = {
            "event": 1,
            "touch_ball": 0.5,
            "save_boost": 0.2,
            "ball_y": 0.1,
            "velocity_ball_to_goal": 0.1,
            "if_closest_to_ball": 0.3,
            "if_touched_last_vel_ball_to_goal": 0.4,
            "face_ball_reward": 0.1
        }

    def get_reward_function(self):
        weights = [self.weights[key] for key in self.weights]
        weights = tuple(weights)
        return CombinedReward(
            (
                EventReward(
                    team_goal=100.0,
                    concede=-100.0,
                    shot=5.0,
                    save=30.0,
                    demo=10.0,
                    boost_pickup=20.0
                ),
                TouchBallReward(),
                SaveBoostReward(),
                BallYCoordinateReward(),
                VelocityBallToGoalReward(),
                RewardIfClosestToBall(ConstantReward()),
                RewardIfTouchedLast(VelocityBallToGoalReward()),
                FaceBallReward()
            ),
            weights
            )