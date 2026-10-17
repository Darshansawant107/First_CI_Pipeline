
"""Program 23: Sort a list without using sort()."""


def bubble_sort(numbers):
    """Return the numbers sorted in ascending order using bubble sort."""
    result = numbers.copy()

    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


if __name__ == "__main__":
    numbers = [5, 2, 8, 1, 3]
    print("Sorted list:", bubble_sort(numbers))
