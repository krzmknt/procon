import pytest

from .main import factorize


# ---------------------------
# Factorize


def test_factorize_positive_normal():
    assert factorize(1) == [1]
    assert factorize(2) == [2]
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
    assert factorize(5) == [5]
    assert factorize(6) == [2, 3]
    assert factorize(8) == [2, 2, 2]
    assert factorize(9) == [3, 3]
    assert factorize(10) == [2, 5]
    assert factorize(15) == [3, 5]



def test_factorize_positive_huge_number_20_digits():
    assert factorize(12345678901234567890) == [2, 3, 3, 5, 101, 3541, 3607, 3803, 27961]


def test_factorize_positive_huge_number_pow_2_10000():
    # Over 3000 digits
    assert factorize(2**10000) == [2] * 10000


def test_factorize_positive_huge_number_pow_3_10000():
    # Over 3000 digits
    assert factorize(3**10000) == [3] * 10000


def test_factorize_value_error():
    with pytest.raises(ValueError):
        factorize(0)

    with pytest.raises(ValueError):
        factorize(-1)

    with pytest.raises(ValueError):
        factorize(1.5)

    with pytest.raises(ValueError):
        factorize("malicious input")


def test_factorize_type_error():
    with pytest.raises(TypeError):
        factorize()

    with pytest.raises(TypeError):
        factorize(1, 2)
