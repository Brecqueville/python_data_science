from typing import Any


def callLimit(limit: int):
    """Decorator factory to limit the number of calls to a function."""
    count = 0

    def callLimiter(function):
        """Decorate a function to enforce the call limit."""

        def limit_function(*args: Any, **kwds: Any):
            """Wrapper function that tracks call count and blocks execution above limit."""
            nonlocal count

            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
