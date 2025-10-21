"""
Colab-specific environment configuration for Pokemon Showdown Gym.

This module provides optimized configurations and utilities for running
the Pokemon Showdown environment in Google Colab.
"""

import os
import subprocess
import time
import signal
from typing import Optional, Dict, Any
import numpy as np
from pathlib import Path


class ColabEnvironmentManager:
    """
    Manages the Pokemon Showdown environment setup in Google Colab.
    
    This class handles:
    - Server installation and configuration
    - Background process management
    - Environment testing and validation
    - Resource optimization for Colab
    """
    
    def __init__(self, base_path: str = "/content"):
        """
        Initialize the Colab environment manager.
        
        Args:
            base_path: Base path for installations (default: /content for Colab)
        """
        self.base_path = Path(base_path)
        self.showdown_path = self.base_path / "pokemon-showdown"
        self.gym_path = self.base_path / "showdown_gym"
        self.server_process: Optional[subprocess.Popen] = None
        
    def install_dependencies(self) -> bool:
        """
        Install all required system and Python dependencies.
        
        Returns:
            bool: True if installation successful, False otherwise
        """
        try:
            # Install system dependencies
            subprocess.run([
                "apt-get", "update"
            ], check=True, capture_output=True)
            
            subprocess.run([
                "apt-get", "install", "-y", "nodejs", "npm"
            ], check=True, capture_output=True)
            
            # Install Python packages
            subprocess.run([
                "pip", "install", "-q", "-r", "requirements-colab.txt"
            ], check=True, capture_output=True)
            
            print("✅ All dependencies installed successfully!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing dependencies: {e}")
            return False
    
    def setup_showdown_server(self) -> bool:
        """
        Clone and configure the Pokemon Showdown server.
        
        Returns:
            bool: True if setup successful, False otherwise
        """
        try:
            # Clone Pokemon Showdown if not exists
            if not self.showdown_path.exists():
                subprocess.run([
                    "git", "clone", 
                    "https://github.com/smogon/pokemon-showdown.git"
                ], check=True, cwd=self.base_path)
            
            # Install Node.js dependencies
            subprocess.run([
                "npm", "install"
            ], check=True, cwd=self.showdown_path)
            
            # Copy configuration
            config_src = self.showdown_path / "config" / "config-example.js"
            config_dst = self.showdown_path / "config" / "config.js"
            
            if config_src.exists() and not config_dst.exists():
                subprocess.run([
                    "cp", str(config_src), str(config_dst)
                ], check=True)
            
            print("✅ Pokemon Showdown server setup complete!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error setting up Pokemon Showdown server: {e}")
            return False
    
    def start_server(self, port: int = 8000) -> bool:
        """
        Start the Pokemon Showdown server in the background.
        
        Args:
            port: Port number for the server
            
        Returns:
            bool: True if server started successfully, False otherwise
        """
        try:
            # Kill existing server if running
            self.stop_server()
            
            # Start new server
            self.server_process = subprocess.Popen([
                "node", "pokemon-showdown", "start", "--no-security", f"--port={port}"
            ], 
            cwd=self.showdown_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid
            )
            
            # Wait for server to start
            time.sleep(5)
            
            # Check if server is running
            if self.server_process.poll() is None:
                print(f"✅ Pokemon Showdown server started on port {port}!")
                return True
            else:
                print("❌ Failed to start Pokemon Showdown server")
                return False
                
        except Exception as e:
            print(f"❌ Error starting server: {e}")
            return False
    
    def stop_server(self) -> None:
        """
        Stop the Pokemon Showdown server.
        """
        if self.server_process and self.server_process.poll() is None:
            try:
                os.killpg(os.getpgid(self.server_process.pid), signal.SIGTERM)
                self.server_process.wait(timeout=5)
            except (ProcessLookupError, subprocess.TimeoutExpired):
                try:
                    os.killpg(os.getpgid(self.server_process.pid), signal.SIGKILL)
                except ProcessLookupError:
                    pass
            finally:
                self.server_process = None
    
    def test_environment(self) -> Dict[str, Any]:
        """
        Test the Pokemon Showdown environment setup.
        
        Returns:
            Dict containing test results and environment info
        """
        results = {
            "server_running": False,
            "environment_working": False,
            "observation_shape": None,
            "action_space_size": None,
            "error": None
        }
        
        try:
            # Test server connection
            if self.server_process and self.server_process.poll() is None:
                results["server_running"] = True
            
            # Test environment import and creation
            import sys
            sys.path.append(str(self.gym_path))
            
            from showdown_gym.showdown_environment import SingleShowdownWrapper
            
            # Create test environment
            env = SingleShowdownWrapper(team_type="random", opponent_type="random")
            
            # Test environment reset
            obs = env.reset()
            results["observation_shape"] = obs.shape
            results["action_space_size"] = env.action_space.n
            
            # Test a random action
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            
            results["environment_working"] = True
            results["test_reward"] = reward
            
            print("✅ Environment test successful!")
            
        except Exception as e:
            results["error"] = str(e)
            print(f"❌ Environment test failed: {e}")
        
        return results
    
    def optimize_for_colab(self) -> None:
        """
        Apply optimizations for Google Colab environment.
        """
        # Set environment variables for better performance
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["MKL_NUM_THREADS"] = "1"
        os.environ["NUMEXPR_NUM_THREADS"] = "1"
        
        # Configure matplotlib for Colab
        import matplotlib
        matplotlib.use('Agg')
        
        print("✅ Colab optimizations applied!")
    
    def get_colab_info(self) -> Dict[str, Any]:
        """
        Get information about the current Colab environment.
        
        Returns:
            Dict containing environment information
        """
        import platform
        import psutil
        
        return {
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "cpu_count": psutil.cpu_count(),
            "memory_total": psutil.virtual_memory().total,
            "memory_available": psutil.virtual_memory().available,
            "disk_usage": psutil.disk_usage('/').percent,
            "gpu_available": self._check_gpu_availability()
        }
    
    def _check_gpu_availability(self) -> bool:
        """
        Check if GPU is available in the Colab environment.
        
        Returns:
            bool: True if GPU is available, False otherwise
        """
        try:
            import torch
            return torch.cuda.is_available()
        except ImportError:
            return False


def setup_colab_environment() -> ColabEnvironmentManager:
    """
    Convenience function to set up the complete Colab environment.
    
    Returns:
        ColabEnvironmentManager: Configured environment manager
    """
    manager = ColabEnvironmentManager()
    
    print("🚀 Setting up Pokemon Showdown Gym for Google Colab...")
    
    # Install dependencies
    if not manager.install_dependencies():
        raise RuntimeError("Failed to install dependencies")
    
    # Setup Pokemon Showdown server
    if not manager.setup_showdown_server():
        raise RuntimeError("Failed to setup Pokemon Showdown server")
    
    # Start server
    if not manager.start_server():
        raise RuntimeError("Failed to start Pokemon Showdown server")
    
    # Apply Colab optimizations
    manager.optimize_for_colab()
    
    # Test environment
    test_results = manager.test_environment()
    if not test_results["environment_working"]:
        raise RuntimeError(f"Environment test failed: {test_results.get('error', 'Unknown error')}")
    
    print("🎉 Pokemon Showdown Gym setup complete!")
    print(f"Environment info: {manager.get_colab_info()}")
    
    return manager


# Example usage
if __name__ == "__main__":
    # Setup the environment
    env_manager = setup_colab_environment()
    
    # Get environment information
    info = env_manager.get_colab_info()
    print(f"Colab Environment Info: {info}")
    
    # Test the environment
    test_results = env_manager.test_environment()
    print(f"Test Results: {test_results}")
