def power(x, y):
    """Recursively computes the power of a number.

    Args:
        x: The base number.
        y: The power to which the base number is being raised.

    Returns:
        The power of the base number.
    """

    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * power(x, y - 1)

def cat_ears(n):
    """Recursively computes the total number of ears based on the number of cats.

    Args:
        n: The total number of cats.

    Returns:
        The total number of cat ears.
    """

    if n == 0:
        return 0
    else:
        return 2 + cat_ears(n - 1)

def alien_ears(n):
    """Recursively returns the total number of alien ears.

    Args:
        n: The total number of aliens.

    Returns:
        The total number of alien ears.
    """

    if n == 1:
        return 3
    elif n % 2 == 0:
        return alien_ears(n - 1) + 2
    else:
        return alien_ears(n - 1) + 3

print(power(2, 3))
print(power(-2, 3))  # This will give a negative result since the base is negative
print(power(1, 5))

print(cat_ears(0))
print(cat_ears(1))
print(cat_ears(2))

print(alien_ears(1))
print(alien_ears(2))
