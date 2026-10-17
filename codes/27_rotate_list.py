"""Program 27: Rotate a list by k positions."""

def rotate_list(items, k):
    """Return a new list rotated by k positions."""
    if not items:
        return []

    k = k % len(items)

    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]


if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))