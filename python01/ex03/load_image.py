import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray | None:
    """Load an image in RGB format and return its pixels as an array."""
    assert isinstance(path, str), "path must be a str"

    try:
        with Image.open(path) as img:
            img_rgb = img.convert("RGB")
            array = np.array(img_rgb)
            print(f"The shape of image is: {array.shape}")
    except OSError as e:
        print(f"Error: {e}")
        return None

    return array
