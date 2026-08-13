import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a two-dimensional list and display its shapes."""
    assert isinstance(family, list), "family must be a list"
    assert all(
        isinstance(item, list) for item in family
    ), "item in family must be a list"

    if len(family) > 0:
        assert all(
            len(family[0]) == len(item) for item in family
        ), "lists are not the same size"

    array = np.array(family)
    print(f"My shape is : {array.shape}")
    array_slice = array[start:end]
    print(f"My new shape is : {array_slice.shape}")

    return array_slice.tolist()
