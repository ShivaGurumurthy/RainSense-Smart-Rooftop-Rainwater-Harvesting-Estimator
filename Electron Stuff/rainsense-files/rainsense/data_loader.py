import os
import pandas as pd

def load_dataset():
    """
    Load rainfall dataset.
    If not found locally, download using KaggleHub.
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    dataset_path = os.path.join(data_dir, "district wise rainfall normal.csv")

    # If dataset not present, download with kagglehub
    if not os.path.exists(dataset_path):
        try:
            import kagglehub
            print("Local dataset not found. Downloading via KaggleHub...")
            kaggle_path = kagglehub.dataset_download("rajanand/rainfall-in-india")
            kaggle_file = os.path.join(kaggle_path, "district wise rainfall normal.csv")

            if os.path.exists(kaggle_file):
                import shutil
                shutil.copy(kaggle_file, dataset_path)
                print("Dataset downloaded and saved locally.")
            else:
                raise FileNotFoundError("District-level rainfall file not found in Kaggle dataset.")
        except Exception as e:
            raise RuntimeError(f"Dataset could not be downloaded: {e}")

    # Load dataset
    df = pd.read_csv(dataset_path)
    return df
