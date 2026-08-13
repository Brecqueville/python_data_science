from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """Load, crop, and display a grayscale part of an image."""
    array = ft_load("animal.jpeg")
    if array is None:
        return
    print(array)
    array_slice = array[100:500, 400:800, 0]
    print(f"New shape after slicing: {array_slice.shape}")
    print(array_slice)

    plt.imshow(array_slice, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
