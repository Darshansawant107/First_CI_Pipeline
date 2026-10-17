"""Program 26: Calculate the sum without using sum()."""


def sum_of_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


if __name__ == "__main__":
    print(sum_of_list([1, 2, 3, 4, 5]))