#!/usr/bin/env python3
"""
Setup script for Google Colab auto-deployment of Pokemon Showdown Gym.

This script helps set up the necessary files and configurations for
automatic deployment to Google Colab.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Any

# Set UTF-8 encoding for stdout on Windows
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())


def create_directory_structure() -> None:
    """Create the necessary directory structure."""
    directories = [
        ".github/workflows",
        "tests",
        "examples",
        "docs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")


def create_test_files() -> None:
    """Create basic test files."""
    test_content = '''"""
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
'''
    
    with open("tests/test_environment.py", "w", encoding="utf-8") as f:
        f.write(test_content)
    print("✅ Created test file: tests/test_environment.py")


def create_example_scripts() -> None:
    """Create example training scripts."""
    example_content = '''"""
Example training script for Pokemon Showdown Gym.
"""

import sys
sys.path.append('.')

from showdown_gym.showdown_environment import SingleShowdownWrapper
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
import matplotlib.pyplot as plt


def train_agent():
    """Train a DQN agent on the Pokemon Showdown environment."""
    
    # Create environment
    def make_env():
        return SingleShowdownWrapper(team_type="random", opponent_type="random")
    
    env = make_vec_env(make_env, n_envs=1)
    
    # Create DQN agent
    model = DQN(
        "MlpPolicy",
        env,
        verbose=1,
        learning_rate=0.001,
        buffer_size=10000,
        learning_starts=1000,
        batch_size=32
    )
    
    # Train the agent
    print("Starting training...")
    model.learn(total_timesteps=10000)
    
    # Save the model
    model.save("pokemon_dqn_model")
    print("Model saved as 'pokemon_dqn_model'")
    
    return model


def evaluate_agent(model_path: str = "pokemon_dqn_model"):
    """Evaluate the trained agent."""
    
    # Load the model
    model = DQN.load(model_path)
    
    # Create evaluation environment
    env = SingleShowdownWrapper(team_type="random", opponent_type="max")
    
    # Run evaluation
    obs = env.reset()
    total_reward = 0
    wins = 0
    
    for episode in range(10):
        obs = env.reset()
        done = False
        episode_reward = 0
        
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, done, info = env.step(action)
            episode_reward += reward
        
        total_reward += episode_reward
        
        if 'win' in info and info['win']:
            wins += 1
        
        print(f"Episode {episode + 1}: Reward = {episode_reward:.2f}")
    
    print(f"\\nEvaluation Results:")
    print(f"Average Reward: {total_reward / 10:.2f}")
    print(f"Win Rate: {wins / 10 * 100:.1f}% ({wins}/10)")


if __name__ == "__main__":
    # Train the agent
    model = train_agent()
    
    # Evaluate the agent
    evaluate_agent()
'''
    
    with open("examples/train_agent.py", "w", encoding="utf-8") as f:
        f.write(example_content)
    print("✅ Created example script: examples/train_agent.py")


def update_readme() -> None:
    """Update README with Colab badge and instructions."""
    readme_path = Path("README.md")
    
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
        
        # Add Colab badge if not present
        if "colab-badge" not in content:
            colab_section = """

## 🚀 Quick Start with Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UoA-CARES/showdown_gym/blob/main/colab_setup.ipynb)

Click the badge above to open this repository directly in Google Colab!

"""
            content += colab_section
            readme_path.write_text(content, encoding="utf-8")
            print("✅ Updated README with Colab badge")
    else:
        print("⚠️  README.md not found, skipping update")


def validate_setup() -> bool:
    """Validate that all required files are present."""
    required_files = [
        "colab_setup.ipynb",
        "colab_environment.py", 
        "requirements-colab.txt",
        ".github/workflows/colab-deployment.yml",
        "COLAB_SETUP.md"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files present")
        return True


def main():
    """Main setup function."""
    print("🚀 Setting up Google Colab auto-deployment for Pokemon Showdown Gym...")
    
    # Create directory structure
    create_directory_structure()
    
    # Create test files
    create_test_files()
    
    # Create example scripts
    create_example_scripts()
    
    # Update README
    update_readme()
    
    # Validate setup
    if validate_setup():
        print("\\n🎉 Setup complete! Your repository is ready for Google Colab deployment.")
        print("\\nNext steps:")
        print("1. Commit and push your changes to GitHub")
        print("2. Check the Actions tab to see if the workflow runs")
        print("3. Test the Colab notebook by clicking the badge in README")
        print("4. Customize the notebook and environment as needed")
    else:
        print("\\n❌ Setup incomplete. Please check the missing files.")
        sys.exit(1)


if __name__ == "__main__":
    main()
