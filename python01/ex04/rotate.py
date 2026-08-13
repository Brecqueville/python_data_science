from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Load, crop, transpose, and display part of an image."""
    array = ft_load("animal.jpeg")
    if array is None:
        return
    array_slice = array[100:500, 400:800, 0]
    print(f"The shape of image is: {array_slice.shape}")
    print(array_slice)

    height = array_slice.shape[1]
    width = array_slice.shape[0]
    array_transpose = np.empty((height, width), dtype=array.dtype)
    for x in range(array_slice.shape[0]):
        for y in range(array_slice.shape[1]):
            array_transpose[x, y] = array_slice[y, x]

    print(f"New shape after Transpose: {array_transpose.shape}")
    print(array_transpose)

    plt.imshow(array_transpose, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
