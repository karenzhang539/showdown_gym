"""
Basic tests for Pokemon Showdown Gym.
"""

import pytest
import numpy as np
from showdown_gym.showdown_environment import SingleShowdownWrapper


def test_environment_creation():
    """Test that environment can be created."""
    try:
        env = SingleShowdownWrapper(team_type="random", opponent_type="random")
        assert env is not None
        print("✅ Environment creation test passed")
    except Exception as e:
        print(f"❌ Environment creation test failed: {e}")
        raise


def test_environment_reset():
    """Test environment reset functionality."""
    try:
        env = SingleShowdownWrapper(team_type="random", opponent_type="random")
        obs = env.reset()
        assert obs is not None
        assert isinstance(obs, np.ndarray)
        print("✅ Environment reset test passed")
    except Exception as e:
        print(f"❌ Environment reset test failed: {e}")
        raise


def test_action_space():
    """Test action space functionality."""
    try:
        env = SingleShowdownWrapper(team_type="random", opponent_type="random")
        action = env.action_space.sample()
        assert isinstance(action, (int, np.integer))
        print("✅ Action space test passed")
    except Exception as e:
        print(f"❌ Action space test failed: {e}")
        raise


if __name__ == "__main__":
    test_environment_creation()
    test_environment_reset()
    test_action_space()
    print("🎉 All tests passed!")
