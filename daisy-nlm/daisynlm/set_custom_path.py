import os
from daisynlm.config import config
import daisynlm

# Example: Setting a custom path for model storage
# By default, it is now set to ./models in the current directory.
# You can override this by setting config["cache_dir"] BEFORE running any inference.

# Let's set it to a specific folder named "my_custom_models"
custom_path = os.path.abspath("my_custom_models")
config["cache_dir"] = custom_path

print(f"Models will be stored in: {config['cache_dir']}")

# Now when you run a command, it will use this directory.
# Note: The first time you run this, it will download the models to this new folder.
print("Running a test completion...")
try:
    response = daisynlm.complete("Hello, how are you?")
    print(f"Response: {response}")
except Exception as e:
    print(f"An error occurred (likely downloading): {e}")

print(f"\nCheck the folder '{custom_path}' to see the downloaded model files.")
