from collections import defaultdict
from typing import List

# https://leetcode.com/problems/coin-change-ii/description/
# https://www.youtube.com/watch?v=qMky6D6YtXU&t=2701s
def change_dfs_memoisation(amount: int, coins: List[int]) -> int:
    dp = {}
    n = len(coins)

    def dfs(ind, amt):
        if amt == amount:
            return 1
        if amt > amount:
            return 0
        if ind == n:
            return 0
        if (ind, amt) in dp:
            return dp[(ind, amt)]

        dp[(ind, amt)] = dfs(ind, amt + coins[ind]) + dfs(ind + 1, amt)
        if (0,0) in dp:
            print(dp)
        return dp[(ind, amt)]


    return dfs(0, 0)


def change_brute_force(amount: int, coins: List[int]) -> int:
    if amount == 0:
        return 1
    if len(coins) == 1:
        if amount % coins[0] == 0:
            return 1
        else:
            return 0

    coins.sort()
    n = len(coins)
    dp = defaultdict(list)
    for amt in range(1, amount + 1):
        for ind, coin in enumerate(coins):
            if amt < coin:
                continue
            elif amt == coin:
                dp[amt].append([coin])
            else:
                if dp[amt - coin]:
                    for prev in dp[amt - coin]:
                        if prev:
                            cp = prev.copy()
                            cp.append(coin)
                            dp[amt].append(cp)

    # print("dp", dp)
    results = set()
    candidates = dp[amount]
    for candidate in candidates:
        if candidate and len(candidate) > 0:
            candidate.sort()
            results.add(tuple(candidate))
    # print(results)
    return len(results)


def main():
    numbers1 = [1, 2, 5]
    amount1 = 5
    expected1 = 4
    actual1 = change_dfs_memoisation(amount1, numbers1)
    print(actual1)
    assert expected1 == actual1

    numbers2 = [1, 2, 3, 4]
    amount2 = 7
    expected2 = 11
    actual2 = change_dfs_memoisation(amount2, numbers2)
    print(actual2)
    assert expected2 == actual2

    numbers3 = [2]
    amount3 = 3
    expected3 = 0
    actual3 = change_dfs_memoisation(amount3, numbers3)
    print(actual3)
    assert expected3 == actual3

    numbers4 = [1, 2, 3, 4, 7, 9, 11, 14, 17, 18]
    amount4 = 18
    expected4 = 156
    actual4 = change_dfs_memoisation(amount4, numbers4)
    print(actual4)
    assert expected4 == actual4


if __name__ == "__main__":
    main()
