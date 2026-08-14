import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Print the dataset dimensions and return it."""
    try:
        dataset = pd.read_csv(path)
    except Exception as error:
        print(f"Error: {error}")
        return None

    print(f"Loading dataset of dimensions {dataset.shape}")
    return (dataset)
