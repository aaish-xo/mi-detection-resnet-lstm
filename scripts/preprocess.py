import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess import prepare_dataset

prepare_dataset(view="A4C")
prepare_dataset(view="A2C")
