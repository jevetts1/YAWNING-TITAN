from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any

from yawning_titan.config.game_config.config_group_class import ConfigGroupABC
from yawning_titan.envs.generic.core import reward_functions
from yawning_titan.envs.generic.helpers.environment_input_validation import check_type


@dataclass
class RewardsConfig(ConfigGroupABC):
    """
    Class that validates and stores Rewards Configuration
    """

    reward_loss: float = field(
        metadata={
            "description": "Reward for the blue agent losing",
            "alias": "rewards_for_loss",
        }
    )
    """Reward for the blue agent losing"""

    reward_success: float = field(
        metadata={
            "description": "Reward for the blue agent winning",
            "alias": "rewards_for_reaching_max_steps",
        }
    )
    """Reward for the blue agent winning"""

    reward_end_multiplier: bool = field(
        metadata={
            "description": "Is true if reward is multiplied by percentage of nodes not compromised",
            "alias": "end_rewards_are_multiplied_by_end_state",
        }
    )
    """Is true if reward is multiplied by percentage of nodes not compromised"""

    reward_reduce_negative_rewards: bool = field(
        metadata={
            "description": "Is true if red agent rewards are reduced the closer to the end timesteps the game ends at",
            "alias": "reduce_negative_rewards_for_closer_fails",
        }
    )
    """Is true if red agent rewards are reduced the closer to the end timesteps the game ends at"""

    reward_function: str = field(
        metadata={
            "description": """
            The reward method used for giving rewards:
            - standard_rewards
            - experimental_rewards
            - one_per_timestep
            - zero_reward
            - safe_nodes_give_rewards
            - punish_bad_actions
            - num_nodes_safe
            - dcbo_cost_func
            """,
            "alias": "reward_function",
        }
    )
    """
    The reward method used for giving rewards:
    - standard_rewards
    - experimental_rewards
    - one_per_timestep
    - zero_reward
    - safe_nodes_give_rewards
    - punish_bad_actions
    - num_nodes_safe
    - dcbo_cost_func
    """

    @classmethod
    def create(cls, settings: Dict[str, Any]) -> RewardsConfig:
        cls._validate(settings)

        rewards = RewardsConfig(
            reward_loss=settings["rewards_for_loss"],
            reward_success=settings["rewards_for_reaching_max_steps"],
            reward_end_multiplier=settings["end_rewards_are_multiplied_by_end_state"],
            reward_reduce_negative_rewards=settings[
                "reduce_negative_rewards_for_closer_fails"
            ],
            reward_function=settings["reward_function"],
        )

        return rewards

    @classmethod
    def _validate(cls, data: dict):
        # validate types
        check_type(data, "rewards_for_loss", [int, float])
        check_type(data, "rewards_for_reaching_max_steps", [int, float])
        check_type(data, "end_rewards_are_multiplied_by_end_state", [bool])
        check_type(data, "reduce_negative_rewards_for_closer_fails", [bool])

        # make sure the reward type exists
        if not hasattr(reward_functions, data["reward_function"]):
            raise ValueError(
                "The reward function '"
                + data["reward_function"]
                + "' does not exist inside: yawning_titan.envs.helpers.reward_functions"
            )
