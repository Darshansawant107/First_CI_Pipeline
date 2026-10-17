
"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    """Return True if the strings are anagrams, ignoring case and spaces."""
    first_clean = first.replace(" ", "").lower()
    second_clean = second.replace(" ", "").lower()

    return sorted(first_clean) == sorted(second_clean)


if __name__ == "__main__":
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")

    print("Anagram:", is_anagram(first, second))
