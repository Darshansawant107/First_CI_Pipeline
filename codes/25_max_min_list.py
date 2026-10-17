"""Program 25: Find maximum and minimum without max() or min()."""

def find_max_min(numbers):
    """Return the maximum and minimum values in a list."""
    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return maximum, minimum


if __name__ == "__main__":
    print(find_max_min([4, 1, 9, 2, 7]))