def unique_paths(m: int, n: int) -> int:
    row_len = m
    col_len = n
    row = [1] * (n + 1)
    row[n] = 0

    for row_i in range(row_len - 2, -1, -1):
        curr_row = [0] * (n + 1)
        for col_i in range(col_len - 1, -1, -1):
            curr_row[col_i] = curr_row[col_i + 1] + row[col_i]

        row = curr_row

    return row[0]


def main():
    rows1 = 3
    cols1 = 7
    expected1 = 28
    actual1 = unique_paths(rows1, cols1)
    print(actual1)
    assert expected1 == actual1


    rows2 = 99
    cols2 = 1
    expected2 = 1
    actual2 = unique_paths(rows2, cols2)
    print(actual2)
    assert expected2 == actual2

    rows3 = 99
    cols3 = 99
    expected3 = 5716592448890534420436582360196242777068052430850904489000
    actual3 = unique_paths(rows3, cols3)
    print(actual3)
    assert expected3 == actual3

    rows4 = 15
    cols4 = 15
    expected4 = 40116600
    actual4 = unique_paths(rows4, cols4)
    print(actual4)
    assert expected4 == actual4

if __name__ == "__main__":
    main()
