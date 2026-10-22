import pytest

from src.math_utils import factorial


def test_factorial_zero():
    """Kiểm tra giai thừa của 0 bằng 1."""
    assert factorial(0) == 1


def test_factorial_one():
    """Kiểm tra giai thừa của 1 bằng 1."""
    assert factorial(1) == 1


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (10, 3628800),
    ],
)
def test_factorial_positive_numbers(n, expected):
    """Kiểm tra giai thừa của các số nguyên dương hợp lệ."""
    assert factorial(n) == expected


@pytest.mark.parametrize("n", [-1, -5, -100])
def test_factorial_negative_numbers_raise_value_error(n):
    """Kiểm tra việc truyền số nguyên âm sẽ gây ra ValueError."""
    with pytest.raises(ValueError, match="Đối số phải là số nguyên không âm"):
        factorial(n)
