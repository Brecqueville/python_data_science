import sys
import string


def main():
    """tests and error handling"""

    text = ""
    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.read()
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    count_text(text)


def count_text(text):
    """Count and display each type of character in text."""
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_space = 0
    count_punctuation = 0

    for char in text:
        if (char.isupper()):
            count_upper += 1
        elif (char.islower()):
            count_lower += 1
        elif (char.isdigit()):
            count_digit += 1
        elif (char.isspace()):
            count_space += 1
        elif char in string.punctuation:
            count_punctuation += 1

    print("The text contains", len(text), "characters:")
    print(count_upper, "upper letters")
    print(count_lower, "lower letters")
    print(count_punctuation, "punctuation marks")
    print(count_space, "spaces")
    print(count_digit, "digits")


if __name__ == "__main__":
    main()
