import pytest
import sys

from Lesson_9.lesson_9 import division, add, minus, range_n

@pytest.mark.skip()
def test_range():
    assert range_n(6, 3, 1)

@pytest.mark.skipif(sys.version_info[0] == 2, reason="Only with python 2")
def test_division():
    result = division(2, 1)
    assert result == 2
    assert division(1,1) == 1

@pytest.mark.xfail
def test_add():
    assert add(1, 1) == 2
    assert False

def test_negative_add():
    assert add(1, -2) == -1


@pytest.mark.test_decorator
def test_another_add():
    assert add(1, -2) == -1


@pytest.mark.test_decorator
def test_minus():
    a = 5
    b = 6
    assert minus(b, a) == 1

# -m MARKEXPR
# -l --showlocals


@pytest.mark.parametrize("a", [1, 2, 3, 4, 5, 6])
def test_division_parametrize(a):
    assert division(a, 1) == a

@pytest.mark.parametrize("a, b, c", [(1, 1, 1), (2, 2, 1), (3, 3, 1), (4, 2, 2)])
def test_multi_parametrize_divizion(a, b, c):
    assert division(a, b) == c

@pytest.fixture()
def initialize_array():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize("a, b, c", [(1, 1, 1), (2, 2, 1), (3, 3, 1), (4, 2, 2)])
def test_divion_with_fixture(initialize_array):
    for el in initialize_array:
        assert division(el, 1) == el