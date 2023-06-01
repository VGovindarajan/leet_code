from typing import List
from collections import defaultdict, deque


# https://leetcode.com/problems/alien-dictionary/
# https://www.youtube.com/watch?v=6kTZYvNNyps

def alien_order(words: List[str]) -> str:
    def dfs(c) -> bool:

        if c in visited:
            return visited[c]
        visited[c] = True
        for next_char in dd[c]:
            if dfs(next_char):
                return True
        output.append(c)
        visited[c] = False

    if len(words) == 0:
        return ""

    dd = {c: set() for w in words for c in w}
    visited = {}  # False (visit done), True (currently visiting)
    output = []
    for i in range(len(words)-1):
        i_word = words[i]
        j_word = words[i + 1]
        min_len = min(len(i_word), len(j_word))
        if len(i_word) > len(j_word) and i_word[:min_len] == j_word[:min_len]:
            return ""

        for k in range(min_len):
            if i_word[k] != j_word[k]:
                dd[i_word[k]].add(j_word[k])

    for ch in dd:
        if dfs(ch):
            return ""
    output.reverse()
    return "".join(output)


def main():
    input1 = ["wrt", "wrf", "er", "ett", "rftt"]
    expected1 = "wertf"
    actual1 = alien_order(input1)
    print(actual1)
    assert expected1 == actual1

    input2 = ["z", "x"]
    expected2 = "zx"
    actual2 = alien_order(input2)
    print(actual2)
    assert expected2 == actual2

    input3 = ["z", "x", "z"]
    expected3 = ""
    actual3 = alien_order(input3)
    print(actual3)
    assert expected3 == actual3


if __name__ == "__main__":
    main()
