import sys
import os

# 🔍 Debug: Show paths being added
current_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(os.path.dirname(current_file), '..'))

print("📄 Current file:", current_file)
print("📁 Adding project root to sys.path:", project_root)

sys.path.insert(0, project_root)

print("🔎 sys.path now contains:")
for p in sys.path:
    print("  ", p)

# Try importing
from src.preprocess import prepare_dataset

# Run A4C and A2C preprocessing
prepare_dataset(view="A4C")
prepare_dataset(view="A2C")
