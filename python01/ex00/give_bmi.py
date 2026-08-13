import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Calculate the BMI for each pair of heights and weights."""
    assert len(height) == len(weight), "lists have different sizes"

    assert all(
        isinstance(item, (int, float))
        for item in height
    ), "height must be a number"

    assert all(
            isinstance(item, (int, float))
            for item in weight
    ), "weight must be a number"

    heights = np.array(height)
    weights = np.array(weight)
    assert np.all(heights != 0), "height cannot be zero"
    result = weights / (heights * heights)

    return result.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return whether each BMI value is greater than the given limit."""
    assert isinstance(limit, int), "limit must be a number"

    assert all(
        isinstance(item, (int, float))
        for item in bmi
    ), "bmi must be a number"

    result = np.array(bmi) > limit

    return result.tolist()
