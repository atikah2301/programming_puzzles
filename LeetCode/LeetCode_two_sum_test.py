import pytest
from LeetCode_two_sum import TwoSum

test_data = [
    ([2, 7, 11, 15], 9, {0, 1}),
    ([3, 2, 4], 6, {1, 2}),
    ([3, 3], 6, {0, 1})
]


@pytest.mark.parametrize("nums, target, expected", test_data)
def test_(nums, target, expected):
    func = TwoSum()
    assert set(func.approach1(nums, target)) == expected


if __name__ == '__main__':
    test_()
