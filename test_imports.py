#!/usr/bin/env python3
"""
Test script to verify all required packages are installed correctly
"""

def test_imports():
    """Test importing all required packages"""
    
    packages_to_test = [
        'pandas',
        'numpy', 
        'poke_env',
        'gymnasium',
        'torch',
        'matplotlib',
        'seaborn',
        'tqdm',
        'wandb',
        'tensorboard'
    ]
    
    print("🔍 Testing package imports...")
    print("=" * 50)
    
    success_count = 0
    total_count = len(packages_to_test)
    
    for package in packages_to_test:
        try:
            # Try to import the package
            module = __import__(package)
            
            # Try to get version if available
            version = "unknown"
            if hasattr(module, '__version__'):
                version = module.__version__
            elif hasattr(module, 'version'):
                version = module.version
                
            print(f"✅ {package:<15} - Version: {version}")
            success_count += 1
            
        except ImportError as e:
            print(f"❌ {package:<15} - FAILED: {e}")
        except Exception as e:
            print(f"⚠️  {package:<15} - ERROR: {e}")
    
    print("=" * 50)
    print(f"📊 Results: {success_count}/{total_count} packages working")
    
    if success_count == total_count:
        print("🎉 All packages installed successfully!")
        return True
    else:
        print("⚠️  Some packages need attention")
        return False

def test_showdown_gym():
    """Test if showdown_gym can be imported"""
    try:
        from showdown_gym import ShowdownEnvironment
        print("✅ showdown_gym - ShowdownEnvironment imported successfully")
        return True
    except ImportError as e:
        print(f"❌ showdown_gym - FAILED: {e}")
        return False

def test_cares_rl():
    """Test if cares_reinforcement_learning can be imported"""
    try:
        from cares_reinforcement_learning import TD3, DQN
        print("✅ cares_reinforcement_learning - TD3, DQN imported successfully")
        return True
    except ImportError as e:
        print(f"❌ cares_reinforcement_learning - FAILED: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Python Package Installation Test")
    print("=" * 50)
    
    # Test basic packages
    basic_success = test_imports()
    
    print("\n🔬 Testing project-specific packages...")
    print("=" * 50)
    
    # Test project packages
    showdown_success = test_showdown_gym()
    cares_success = test_cares_rl()
    
    print("\n📋 Summary:")
    print("=" * 50)
    if basic_success and showdown_success and cares_success:
        print("🎉 All tests passed! Your environment is ready.")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        print("\n💡 Common fixes:")
        print("   - Run: pip3 install -r requirements.txt")
        print("   - Run: pip3 install --editable .")
        print("   - Check if you're in the right virtual environment")