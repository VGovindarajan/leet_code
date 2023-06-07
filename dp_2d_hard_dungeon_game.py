from typing import List

# https://leetcode.com/problems/dungeon-game/description/
# https://leetcode.com/problems/dungeon-game/solutions/3607346/dungeon-game-simple-python-solution-with-detailed-notes/

def calculate_minimum_hp(dungeon: List[List[int]]) -> int:
    rows = len(dungeon)
    cols = len(dungeon[0])

    finish = dungeon[rows - 1][cols - 1]
    finish_health = 1
    if finish <= 0:
        finish_health = abs(finish) + 1

    curr_row = [0] * (cols + 1)

    for row_i in range(rows - 1, -1, -1):
        temp_row = [0] * (cols + 1)
        for col_i in range(cols - 1, -1, -1):

            # finish cell already has finish_health
            if row_i == rows - 1 and col_i == cols - 1:
                temp_row[col_i] = finish_health
                continue

            cell_val = dungeon[row_i][col_i]
            right_val = 1
            if col_i + 1 < cols:
                right_val = max(temp_row[col_i + 1] - cell_val, 1)
            else:
                right_val = float("inf")
            down_val = 1
            if row_i + 1 < rows:
                down_val = max(curr_row[col_i] - cell_val, 1)
            else:
                down_val = float("inf")
            temp_row[col_i] = min(right_val, down_val)
        curr_row = temp_row

    return curr_row[0]

    return curr_row[0]


def main():
    numbers1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    expected1 = 7
    actual1 = calculate_minimum_hp(numbers1)
    print(actual1)
    assert expected1 == actual1

    numbers2 = [[0]]
    expected2 = 1
    actual2 = calculate_minimum_hp(numbers2)
    print(actual2)
    assert expected2 == actual2

    numbers3 = [[0, -3]]
    expected3 = 4
    actual3 = calculate_minimum_hp(numbers3)
    print(actual3)
    assert expected3 == actual3


if __name__ == "__main__":
    main()
