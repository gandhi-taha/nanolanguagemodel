import sys
import os

# Add current directory to path so we can import the local package
sys.path.append(os.getcwd())

print("Importing daisynlm...")
import daisynlm as nlm

print(f"Version: {nlm.__version__}")
print("Running a simple test query...")

try:
    # Use a small model for quick testing if possible, or just default
    nlm.config["max_ram"] = 0.5 # Uncomment to force small model if needed
    
    response = nlm.do("What is 2 + 2?")
    print(f"\nResponse: {response}")
    print("\n✅ It works!")
except Exception as e:
    print(f"\n❌ Error: {e}")
