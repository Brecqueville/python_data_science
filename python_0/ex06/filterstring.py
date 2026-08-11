import sys
import ft_filter


def main():
    """Filter words according to the given maximum length."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        words = text.split()

        try:
            integer = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        print(ft_filter.ft_filter(lambda word: len(word) > integer, words))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


if __name__ == "__main__":
    main()
