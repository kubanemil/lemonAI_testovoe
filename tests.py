import numpy as np
from main import FuncOptimizer
import pytest


@pytest.fixture
def A():
    return np.asarray([(i, 8) for i in range(-5, 5)] + [(i, -2) for i in range(5, 15)])


@pytest.fixture
def optimizer(A):
    return FuncOptimizer(A)


def test_abc(optimizer):
    assert optimizer.a == 8
    assert optimizer.b == -2
    assert optimizer.c == 5


def test_std(optimizer):
    assert optimizer.std() == 0


def test_plot(optimizer):
    optimizer.plot(show=False)
    assert True
