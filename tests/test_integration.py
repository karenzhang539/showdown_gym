"""
Integration tests for Pokemon Showdown Gym.

These tests require a running Pokemon Showdown server and should be run locally.
They are skipped in CI environments.
"""

import pytest
import numpy as np
import os
from showdown_gym.showdown_environment import SingleShowdownWrapper


@pytest.mark.skipif(
    os.getenv("CI") == "true", 
    reason="Requires Pokemon Showdown server - skip in CI"
)
def test_full_environment_workflow():
    """Test complete environment workflow with server."""
    try:
        # Create environment
        env = SingleShowdownWrapper(team_type="random", opponent_type="random")
        
        # Test reset
        obs = env.reset()
        assert obs is not None
        assert isinstance(obs, np.ndarray)
        print("✅ Environment reset successful")
        
        # Test action space
        action = env.action_space.sample()
        assert isinstance(action, (int, np.integer))
        print("✅ Action space test passed")
        
        # Test step
        obs, reward, done, info = env.step(action)
        assert obs is not None
        assert isinstance(reward, (int, float))
        assert isinstance(done, bool)
        assert isinstance(info, dict)
        print("✅ Environment step successful")
        
        print("✅ Full environment workflow test passed")
        
    except Exception as e:
        print(f"❌ Full environment workflow test failed: {e}")
        print("Make sure Pokemon Showdown server is running on localhost:8000")
        raise


@pytest.mark.skipif(
    os.getenv("CI") == "true", 
    reason="Requires Pokemon Showdown server - skip in CI"
)
def test_environment_with_different_opponents():
    """Test environment with different opponent types."""
    opponent_types = ["random", "simple", "max"]
    
    for opponent_type in opponent_types:
        try:
            env = SingleShowdownWrapper(team_type="random", opponent_type=opponent_type)
            obs = env.reset()
            assert obs is not None
            print(f"✅ Environment with {opponent_type} opponent works")
        except Exception as e:
            print(f"❌ Environment with {opponent_type} opponent failed: {e}")
            raise


@pytest.mark.skipif(
    os.getenv("CI") == "true", 
    reason="Requires Pokemon Showdown server - skip in CI"
)
def test_environment_with_different_teams():
    """Test environment with different team types."""
    team_types = ["random", "nu", "ou", "ru", "uu", "uber"]
    
    for team_type in team_types:
        try:
            env = SingleShowdownWrapper(team_type=team_type, opponent_type="random")
            obs = env.reset()
            assert obs is not None
            print(f"✅ Environment with {team_type} team works")
        except Exception as e:
            print(f"❌ Environment with {team_type} team failed: {e}")
            raise


if __name__ == "__main__":
    # Only run if not in CI
    if os.getenv("CI") != "true":
        test_full_environment_workflow()
        test_environment_with_different_opponents()
        test_environment_with_different_teams()
        print("🎉 All integration tests passed!")
    else:
        print("⏭️  Skipping integration tests in CI environment")
