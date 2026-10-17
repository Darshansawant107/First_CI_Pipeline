
"""Program 29: Check whether a number is an Armstrong number."""


def is_armstrong(number):
    """Return True if the number is an Armstrong number."""
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number


if __name__ == "__main__":
    print(is_armstrong(153))
