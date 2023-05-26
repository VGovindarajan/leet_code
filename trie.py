from typing import List
from queue import PriorityQueue


class TrieNode:
    def __init__(self):
        self.data = {}
        self.word_ending = False


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def add(self, word: str):
        cur = self._root
        for c in word:
            if c not in cur.data:
                cur.data[c] = TrieNode()
            cur = cur.data[c]
        cur.word_ending = True

    def search(self, word: str) -> bool:
        cur = self._root
        for c in word:
            if c not in cur.data:
                return False
            cur = cur.data[c]
        return cur.word_ending

    def is_partial_match(self, word: str) -> bool:
        cur = self._root
        for c in word:
            if c not in cur.data:
                return False
            cur = cur.data[c]
        return True

    def get_partial_matches(self, word: str) -> List[str]:
        cur = self._root
        for c in word:
            if c not in cur.data:
                return []
            cur = cur.data[c]

        return self._partial_impl(cur, word)

    def _partial_impl(self, node: TrieNode, word: str) -> List[str]:
        matches = []
        if node is None:
            return matches
        cur = node
        pq = PriorityQueue()
        pq.put((word, cur))

        while not pq.empty():
            word_q, node_q = pq.get()
            for c, cur_n in node_q.data.items():
                c_word = word_q + c
                if cur_n.word_ending:
                    matches.append(c_word)
                pq.put((c_word, cur_n))

        return matches


def main():
    t = Trie()
    add_apple = t.add("apple")
    add_boy = t.add("boy")
    add_charlie = t.add("charlie")

    apple_present = t.search("apple")
    charlie_present = t.search("charlie")
    app_present = t.search("app")
    baby_present = t.search("baby")

    app_partial = t.is_partial_match("app")
    char_partial = t.is_partial_match("char")

    add_application = t.add("application")
    add_applicant = t.add("applicant")

    appl_matches = t.get_partial_matches("appl")

    assert apple_present
    assert charlie_present
    assert app_present is False
    assert baby_present is False

    assert app_partial
    assert char_partial


if __name__ == "__main__":
    main()
