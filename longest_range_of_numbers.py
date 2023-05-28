from collections import defaultdict
from typing import List


# “Those who cannot remember the past are condemned to repeat it.”
# https://leetcode.com/problems/longest-consecutive-sequence/description/

def longest_consecutive_range(nums: List[int]) -> int:
    def set_running_count(num) -> int:
        if num not in store:
            return 0
        if num in dd:
            return dd[num]

        if num - 1 in store:
            prev_count = set_running_count(num - 1)
            curr_count = 1 + prev_count
            dd[num] = curr_count
        else:
            dd[num] = 1
        return dd[num]

    if nums is None:
        return 0
    if len(nums) == 0:
        return 0
    store = set(nums)
    longest = 0
    dd = defaultdict(int)

    for nu in nums:
        running_count = set_running_count(nu)
        longest = max(longest, running_count)

    return longest


def main():
    numbers1 = [4, 1, 2, 3, 9, 99, 7, 5]
    expected1 = 5
    actual1 = longest_consecutive_range(numbers1)
    print(actual1)
    assert expected1 == actual1

    numbers2 = [0, 1, 2, 4, 3, 5, 9, 7, 0, 6, 8]
    expected2 = 10
    actual2 = longest_consecutive_range(numbers2)
    print(actual2)
    assert expected2 == actual2

    numbers3 = [4, 1, 2, 3, 9, 99, 7, 5, 999999999, 6]
    expected3 = 7
    actual3 = longest_consecutive_range(numbers3)
    print(actual3)
    assert expected3 == actual3


if __name__ == "__main__":
    main()
