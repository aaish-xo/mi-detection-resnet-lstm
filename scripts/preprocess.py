import sys
import os

# 🔧 Add the parent directory to sys.path so it can find 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess import prepare_dataset

# Run A4C and A2C preprocessing
prepare_dataset(view="A4C")
prepare_dataset(view="A2C")
