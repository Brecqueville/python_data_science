def square(x: int | float) -> int | float:
    """Return the square of the given number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the exponentiation of the number by itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return an inner function that applies function iteratively to x."""
    count = 0

    def inner() -> float:
        """Calculate and return the result of repeated function calls."""
        nonlocal count
        count += 1
        res = x
        for _ in range(count):
            res = function(res)
        return res
    return (inner)
