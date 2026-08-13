import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    result = 255 - array
    plt.imshow(result)
    plt.show()
    return result


def ft_red(array) -> np.ndarray:
    """Keep only the red channel of the image received."""
    result = array.copy()
    result[:, :, 1:] = 0
    plt.imshow(result)
    plt.show()
    return result


def ft_green(array) -> np.ndarray:
    """Keep only the green channel of the image received."""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    plt.imshow(result)
    plt.show()
    return result


def ft_blue(array) -> np.ndarray:
    """Keep only the blue channel of the image received."""
    result = array.copy()
    result[:, :, 0:2] = 0
    plt.imshow(result)
    plt.show()
    return result


def ft_grey(array) -> np.ndarray:
    """Convert the image received to greyscale."""
    result = array.copy()
    grey = result.sum(axis=2) / 3
    result[:, :, :] = grey[:, :, None]
    plt.imshow(result)
    plt.show()
    return result
