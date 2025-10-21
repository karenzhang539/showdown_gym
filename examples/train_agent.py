"""
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
    
    print(f"\nEvaluation Results:")
    print(f"Average Reward: {total_reward / 10:.2f}")
    print(f"Win Rate: {wins / 10 * 100:.1f}% ({wins}/10)")


if __name__ == "__main__":
    # Train the agent
    model = train_agent()
    
    # Evaluate the agent
    evaluate_agent()
