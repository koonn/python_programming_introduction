import pytest
from ..odd_even import min_odd

@pytest.mark.parametrize("x, y, z, expected", [
    (1, 3, 5, 1), # all odd
    (2, 3, 5, 3), # x even
    (3, 2, 5, 3), # y even
    (5, 3, 2, 3), # z even
    (2, 4, 5, 5), # x and y even
    (3, 4, 2, 3), # y and z even
    (2, 3, 4, 3), # x and z even
    (2, 4, 6, 2), # all even
])
def test_min_odd(x, y, z, expected):
    assert min_odd(x, y, z) == expected