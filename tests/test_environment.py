"""
Basic tests for Pokemon Showdown Gym.
"""

import pytest
import numpy as np
import os
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


@pytest.mark.skipif(
    os.getenv("CI") == "true", 
    reason="Requires Pokemon Showdown server - skip in CI"
)
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


def test_environment_import():
    """Test that all required modules can be imported."""
    try:
        from showdown_gym.showdown_environment import ShowdownEnvironment, SingleShowdownWrapper
        from showdown_gym.base_environment import BaseShowdownEnv
        print("✅ All imports successful")
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        raise


if __name__ == "__main__":
    test_environment_creation()
    test_environment_reset()
    test_action_space()
    test_environment_import()
    print("🎉 All tests passed!")
