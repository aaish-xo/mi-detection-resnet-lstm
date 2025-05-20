import sys
import os

# ✅ Add project root (not just parent) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess import prepare_dataset

# Run A4C and A2C preprocessing
prepare_dataset(view="A4C")
prepare_dataset(view="A2C")
