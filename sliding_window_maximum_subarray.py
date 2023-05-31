from typing import List


# https://leetcode.com/problems/maximum-subarray/description/
def max_sub_array(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    largest = nums[0]

    cur_sum = 0
    for index, num in enumerate(nums):

        if cur_sum <= 0:
            cur_sum = num
        else:
            cur_sum += num

        largest = max(largest, cur_sum)

    return largest


def main():
    numbers1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6
    actual1 = max_sub_array(numbers1)
    print(actual1)
    assert expected1 == actual1

    numbers2 = [1]
    expected2 = 1
    actual2 = max_sub_array(numbers2)
    print(actual2)
    assert expected2 == actual2

    numbers3 = [5, 4, -1, 7, 8]
    expected3 = 23
    actual3 = max_sub_array(numbers3)
    print(actual3)
    assert expected3 == actual3


if __name__ == "__main__":
    main()
