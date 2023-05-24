class LLNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self._value = value
        self._prev_node = prev_node
        self._next_node = next_node

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_previous_node(self):
        return self._prev_node

    def set_previous_node(self, value):
        self._prev_node = value

    def get_next_node(self):
        return self._next_node

    def set_next_node(self, value):
        self._next_node = value

    def __repr__(self):
        return f'Node({self._value})'


class LinkedList:
    def __init__(self):
        self._head = None
        self._last = None

    def add_node(self, value):
        if self._head is None:
            node = LLNode(value, None, None)
            self._head = node
            return
        elif self._last is None:
            node = LLNode(value, self._head, None)
            self._last = node
            self._head.set_next_node(self._last)
        else:
            node = LLNode(value, self._last,  None)
            self._last.set_next_node(node)
            self._last = node

    def remove_head(self):
        if self._head is None:
            return None
        t = self._head

        self._head = self._head.get_next_node()
        if self._head is not None:
            self._head.set_previous_node(None)
        return t.get_value()

    def remove_last(self):
        t = self._last
        if self._last is None:
            t = self._head
            self._head = None

        if t is not None:
            self._last = t.get_previous_node()
            if self._last is not None:
                self._last.set_next_node(None)
            if self._last == self._head:
                self._last = None

            return t.get_value()

        return None

    def get_value_at(self, index):
        if 0 > index:
            return None
        current = self._head
        if index == 0:
            if current is not None:
                return current.get_value()
            else:
                return None
        for i in range(0, index):
            if current is not None:
                current = current.get_next_node()
        return None if current is None else current.get_value()


    def count(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.get_next_node()
        return count

    def __repr__(self):
        return f'count={self.count()}, head={self._head}, last={self._last}'

def main():
    ll = LinkedList()
    ll.add_node(12)
    ll.add_node(13)
    ll.add_node(14)
    ll.add_node(15)
    ll.add_node(16)
    print(ll)
    c = ll.count()
    for i in range(0, c):
        print(i, ll.get_value_at(i))

    print(ll.remove_head())
    print(ll.remove_last())
    print(ll)
    c = ll.count()
    for i in range(0, c):
        print(i, ll.get_value_at(i))

if __name__ == "__main__":
    main()



