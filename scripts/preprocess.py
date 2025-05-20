import sys
import os

# 🔍 Print debug info
print("Current file:", __file__)
print("Adding to sys.path:", os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("sys.path is now:")
for p in sys.path:
    print("  ", p)

# Try importing
from src.preprocess import prepare_dataset

# Run A4C and A2C preprocessing
prepare_dataset(view="A4C")
prepare_dataset(view="A2_
