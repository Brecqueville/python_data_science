from typing import Any


def mean(numbers: tuple):
    """Calculates and returns the arithmetic mean of a sequence of numbers."""
    return sum(numbers) / len(numbers)


def median(numbers: tuple):
    """Calculates and returns the median value of a sequence of numbers."""
    lenght = len(numbers)
    sort = sorted(numbers)
    if lenght % 2 == 1:
        return sort[lenght // 2]
    return sum([sort[lenght // 2], sort[lenght // 2 - 1]]) / 2


def quartile(numbers: tuple):
    """Calculates and returns the 25% (Q1) and 75% (Q3) quartiles."""
    sort = sorted(numbers)
    Q1 = int(len(numbers) * 0.25)
    Q2 = int(len(numbers) * 0.75)
    return [float(sort[Q1]), float(sort[Q2])]


def var(numbers: tuple):
    """Calculates and returns the variance of a sequence of numbers."""
    mean_list = mean(numbers)
    sort = sorted(numbers)
    return sum((x - mean_list) ** 2 for x in sort) / len(sort)


def std(numbers: tuple):
    """Calculates and returns the standard deviation of sequence of numbers."""
    return var(numbers) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Computes and prints requested statistics (*args) based on **kwargs."""
    for x in args:
        if not isinstance(x, (int, float)):
            print("ERROR")
            return

    stats = ("mean", "median", "quartile", "std", "var")
    no_numbers = len(args) == 0
    for value in kwargs.values():
        if value not in stats:
            continue
        if no_numbers:
            print("ERROR")
            continue

        if value == "mean":
            print(f"mean : {mean(args)}")
        elif value == "median":
            print(f"median : {median(args)}")
        elif value == "quartile":
            print(f"quartile : {quartile(args)}")
        elif value == "var":
            print(f"var : {var(args)}")
        elif value == "std":
            print(f"std : {std(args)}")
