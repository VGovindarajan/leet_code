from typing import List


# https://leetcode.com/problems/partition-equal-subset-sum/description/
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=9920s
def can_partition(nums: List[int]) -> bool:
    if sum(nums) % 2 == 1:
        return False

    k = sum(nums) // 2
    if max(nums) > k:
        return False

    dp_set = set()

    for n in nums:
        if n == k:
            return True
        dp_temp = set()
        dp_temp.add(n)
        for ds in dp_set:
            dp_temp.add(ds)
            dp_temp.add(ds + n)
            if ds + n == k:
                return True
        dp_set = dp_temp

    return True if k in dp_set else False


def main():
    numbers1 = [1, 5, 11, 5]
    expected1 = True
    actual1 = can_partition(numbers1)
    print(actual1)
    assert expected1 == actual1

    numbers2 = [1, 2, 3, 5]
    expected2 = False
    actual2 = can_partition(numbers2)
    print(actual2)
    assert expected2 == actual2

    numbers3 = [2, 3, 4, 8, 14, 9]
    expected3 = True
    actual3 = can_partition(numbers3)
    print(actual3)
    assert expected3 == actual3


if __name__ == "__main__":
    main()
