from src.preprocess import prepare_dataset

# Run preprocessing for both A4C and A2C views
prepare_dataset(view="A4C")
prepare_dataset(view="A2C")

