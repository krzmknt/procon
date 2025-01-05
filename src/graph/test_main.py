import pytest
from .main import dnf


def test_dnf():
    N = 3
    M = 2
    E = [[1, 3], [2, 3]]

    assert dnf(N, M, E) == 1
