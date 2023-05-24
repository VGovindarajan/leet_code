from linked_list import LinkedList

class StackLL:
    def __init__(self):
        self._linked_list = LinkedList()

    def push(self, value):
        self._linked_list.add_node(value)

    def pop(self):
        return self._linked_list.remove_last()

    def peek(self):
        return self._linked_list.get_value_at(self.count()-1)

    def count(self):
        return self._linked_list.count()

    def __repr__(self):
        count = self.count()
        return f'Count={count},first={self._linked_list.get_value_at(0)},last={self._linked_list.get_value_at(count-1)}'


def main():
    s = StackLL()

    for i in range(0, 8):
        s.push(i+1)
    print(s)

    for i in range(0, 12):
        print(s.pop())

    print(s)

if __name__ == "__main__":
    main()