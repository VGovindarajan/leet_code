from linked_list import LinkedList

class QueueLL:
    def __init__(self):
        self._linked_list = LinkedList()

    def enqueue(self, value):
        self._linked_list.add_node(value)

    def dequeue(self):
        return self._linked_list.remove_head()

    def count(self):
        return self._linked_list.count()

    def __repr__(self):
        count = self.count()
        return f'Count={count},first={self._linked_list.get_value_at(0)},last={self._linked_list.get_value_at(count-1)}'


def main():
    q = QueueLL()

    for i in range(0, 8):
        q.enqueue(i)
    print(q)

    for i in range(0, 12):
        print(q.dequeue())

    print(q)

if __name__ == "__main__":
    main()