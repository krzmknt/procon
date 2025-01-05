def is_positive_integer(n) -> bool:
    """
    Return True if n is positive integer.

    Parameters:
    n: any object

    Returns:
    bool: True if n is positive integer, False otherwise

    Examples:
    is_positive_integer(1) -> True
    is_positive_integer(0) -> False
    is_positive_integer(-1) -> False
    """

    return isinstance(n, int) and 0 < n


def factorize(n) -> list[int]:
    """
    Factorize positive integer and return its factors.

    Parameters
    n: positive integer

    Returns:
    list[int]: the list of factors of n

    Raises:
    ValueError: if n is not positive integer

    Examples:
    factorize(24) -> [2, 2, 2, 3]
    factorize(1) -> [1]
    factorize(0) -> ValueError
    factorize(-1) -> ValueError
    """

    if not is_positive_integer(n):
        raise ValueError("n must be positive integer.")

    if n == 1:
        return [1]

    factors = []

    # 2 is a special case
    while n & 1 == 0:
        factors.append(2)
        n >>= 1

    divisor = 3
    while 1 < n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 2

    return factors


def prime(n):
    """Return True if n is prime."""
    return len(factorize(n)) == 1
