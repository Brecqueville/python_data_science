import os


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while yielding each item."""
    total = len(lst)
    current = 0

    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    suffix = f"0/{total}"
    char_empty = " " * (terminal_width - len(suffix) - 8)
    print(f"\r  0%|{char_empty}| {suffix}", end="", flush=True)

    for item in lst:
        yield item
        current += 1

        percentage = (100 * current) // total
        prefix = f"{percentage:3}%"
        suffix = f"{current}/{total}"
        bar_width = terminal_width - len(prefix) - len(suffix) - 4

        filled = current * bar_width // total
        empty = bar_width - filled

        char_bar = "=" * filled + " " * empty

        print(f"\r{prefix}|{char_bar}| {suffix}", end="", flush=True)
