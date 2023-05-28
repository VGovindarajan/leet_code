from typing import List

# https://leetcode.com/problems/subsets/editorial/ Approach 3: Lexicographic (Binary Sorted) Subsets
def subsets_bitset(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    output = []
    for i in range(2**n, 2**(n+1)):
        #print(bin(i))
        bitmask = bin(i)[3:]
        #print(bitmask)
        output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

    return output


def subsets_cascade(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output

def subsets_backtracking(nums: List[int]) -> List[List[int]]:
    # https://leetcode.com/problems/subsets/editorial/ Approach 2, Backtracking
    def backtrack(count: int, start: int, curr: List[int]):
        # The combination is done
        if len(curr) == count:
            output.append(curr[:])
            return
        for i in range(start, n):
            # add nums[i] to current combination
            curr.append(nums[i])
            # Use the next integer to add to and possibly complete the combination
            backtrack(count, i + 1, curr)
            # backtrack and continue
            curr.pop()

    output = []
    n = len(nums)
    for j in range(0, n + 1):
        backtrack(j, 0, [])
    return output


def main():
    numbers1 = [1, 2, 3]
    expected1 = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    actual1 = subsets_bitset(numbers1)
    print(actual1)
    assert expected1 == actual1

    numbers2 = [0]
    expected2 = [[], [0]]
    actual2 = subsets_cascade(numbers2)
    print(actual2)
    assert expected2 == actual2

    numbers3 = [1, 2, 3, 4, 6]
    expected3 = [[], [1], [2], [3], [4], [6], [1, 2], [1, 3], [1, 4], [1, 6], [2, 3], [2, 4], [2, 6], [3, 4], [3, 6],
                 [4, 6], [1, 2, 3], [1, 2, 4], [1, 2, 6], [1, 3, 4], [1, 3, 6], [1, 4, 6], [2, 3, 4], [2, 3, 6],
                 [2, 4, 6], [3, 4, 6], [1, 2, 3, 4], [1, 2, 3, 6], [1, 2, 4, 6], [1, 3, 4, 6], [2, 3, 4, 6],
                 [1, 2, 3, 4, 6]]
    actual3 = subsets_backtracking(numbers3)
    print(actual3)
    assert expected3 == actual3


if __name__ == "__main__":
    main()
