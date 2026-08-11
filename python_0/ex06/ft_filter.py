def ft_filter(function, iterable):
    """Return items for which function(item) is true."""
    if function is None:
        result = [item for item in iterable if item]
    else:
        result = [item for item in iterable if function(item)]
    return (result)


# def test(item):
#     if (item % 2 == 0):
#         return True
#     else:
#         return False


# result = ft_filter(test, [1, 2, 3, 4, 5])
# print(result)
