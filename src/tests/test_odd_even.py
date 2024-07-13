import pytest
from ..odd_even import max_odd_or_min_even

@pytest.mark.parametrize("x, y, z, expected", [
    (1, 3, 5, 5), # all odd
    (2, 3, 5, 5), # x even
    (3, 2, 5, 5), # y even
    (5, 3, 2, 5), # z even
    (2, 4, 5, 5), # x and y even
    (3, 4, 2, 3), # y and z even
    (2, 3, 4, 3), # x and z even
    (2, 4, 6, 2), # all even
])
def test_max_odd_or_min_even(x, y, z, expected):
    assert max_odd_or_min_even(x, y, z) == expected