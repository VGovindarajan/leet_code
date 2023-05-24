from typing import List

def find_sets(is_connected: List[List[int]]) -> int:
    n = len(is_connected)
    provinces = [i for i in range(0, n)]

    p = 0
    for row in is_connected:
        for i, j in enumerate(row):
            if i <= p:
                continue
            if (j == 1) and provinces[i] == i:
                provinces[i] = provinces[p]
            if (j == 1) and provinces[i] < i:
                v = provinces[p]
                vn = provinces[i]
                provinces[p] = vn
                for k, l in enumerate(provinces):
                    if l == v:
                        provinces[k] = vn
        p = p + 1

    return len(set(provinces))


def main():
    tc1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    c1 = find_sets(tc1)
    print(c1)

    tc2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    c2 = find_sets(tc2)
    print(c2)

    tc3 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1]]
    c3 = find_sets(tc3)
    print(c3)

    tc4 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    c4 = find_sets(tc4)
    print(c4)

    tc5 = [[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]
    c5 = find_sets(tc5)
    print(c5)

if __name__ == "__main__":
    main()
