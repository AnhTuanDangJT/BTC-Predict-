"""
Simple script to run the main.py file with proper path setup
"""
import os
import sys

# Get the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))
market_test_dir = os.path.join(project_root, 'market_test')

# Change to market_test directory
os.chdir(market_test_dir)

# Add market_test to path
sys.path.insert(0, market_test_dir)

# Import and run main
if __name__ == "__main__":
    print("=" * 80)
    print("BTC Prediction Project - Main Script Runner")
    print("=" * 80)
    print(f"Working directory: {os.getcwd()}")
    print(f"Project root: {project_root}")
    print("=" * 80)
    print()
    
    # Check if .env file exists
    env_file = os.path.join(project_root, '.env')
    if not os.path.exists(env_file):
        print("⚠️  WARNING: .env file not found!")
        print(f"   Please create .env file at: {env_file}")
        print("   Required variables: API_KEY, NESTQUANT_API_ENDPOINT")
        print()
    
    # Check if data directory exists
    data_dir = os.path.join(project_root, 'data')
    if not os.path.exists(data_dir):
        print("⚠️  WARNING: data/ directory not found!")
        print("   Please run data crawling first:")
        print("   python market_test/crawlAsubmit/crawling.py")
        print()
    
    # Check if required directories exist
    realtime_data_dir = os.path.join(market_test_dir, 'realtimeData')
    model_dir = os.path.join(market_test_dir, 'model')
    
    os.makedirs(realtime_data_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)
    print(f"✓ Created/verified directories: realtimeData, model")
    print()
    
    print("Starting main script...")
    print("=" * 80)
    print()
    
    # Import and run
    try:
        from main import main
        if __name__ == "__main__":
            # If main.py has a main() function, call it
            # Otherwise, the code in if __name__ == "__main__" will run automatically
            pass
    except ImportError:
        # If no main() function, just execute the file
        import subprocess
        main_file = os.path.join(market_test_dir, 'main', 'main.py')
        subprocess.run([sys.executable, main_file])

