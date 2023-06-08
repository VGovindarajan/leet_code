from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

def max_profit_linear(prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0
    n = len(prices)

    running_total = i = 0
    while i < n - 1:
        buy_px = sell_px = 0
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        if i < n:
            buy_px = prices[i]
            i += 1

        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        if i < n:
            sell_px = prices[i]
            i += 1
            running_total += sell_px - buy_px

    return running_total


def max_profit(prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0

    dp = {}  # Key = (index,buying), Value = max profit
    n = len(prices)

    def dfs(i, buying):
        # base case
        if (i, buying) in dp:
            return dp[(i, buying)]

        if i >= n:
            return 0

        # logic
        no_trade = dfs(i + 1, buying)

        if buying:
            buy = dfs(i + 1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, no_trade)
        else:
            sell = dfs(i + 1, not buying) + prices[i]
            dp[(i, buying)] = max(sell, no_trade)
        return dp[(i, buying)]

    dfs(0, True)
    return dp[(0, True)]


def main():
    numbers1 = [7, 1, 5, 3, 6, 4]
    expected1 = 7
    actual1 = max_profit_linear(numbers1)
    print(actual1)
    assert expected1 == actual1

    numbers2 = [7, 6, 4, 3, 1]
    expected2 = 0
    actual2 = max_profit_linear(numbers2)
    print(actual2)
    assert expected2 == actual2

    numbers3 = [1, 2, 3, 4, 5]
    expected3 = 4
    actual3 = max_profit_linear(numbers3)
    print(actual3)
    assert expected3 == actual3

    numbers4 = [7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6,
                4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3,
                6, 4, 7092, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1,
                5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7,
                1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4,
                7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6,
                4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3,
                6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5,
                3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 62, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7,
                1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4,
                7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6,
                4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1001, 5,
                3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1,
                5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7,
                1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4,
                7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6,
                4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3,
                6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4]
    expected4 = 9148
    actual4 = max_profit_linear(numbers4)
    print(actual4)
    assert expected4 == actual4


if __name__ == "__main__":
    main()
