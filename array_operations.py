import logging

_logger = logging.getLogger('array_ops')


class TestArray:
    def __init__(self, size, items=None):
        self._size = size
        self._array = []
        if items is None:
            for i in range(0, size):
                self._array.append(None)
        else:
            for i in items:
                self._array.append(i)

    def get_at_index(self, index):
        if 0 <= index < len(self._array):
            return self._array[index]
        else:
            raise RuntimeError(f'index {index}, out of bounds')

    def set_at_index(self, index, value):
        if 0 <= index < len(self._array):
            self._array[index] = value
        else:
            raise RuntimeError(f'index {index}, out of bounds')

    def remove_at_index(self, index):
        if 0 <= index < len(self._array):
            length = len(self._array)
            removed = self._array[index]
            for j in range(index, length-2):
                self._array[j] = self._array[j+1]
            self._array[length-1] = None
            return removed
        else:
            raise RuntimeError(f'index {index}, out of bounds')

    def insert_at_index(self, index, value):
        if 0 <= index < len(self._array):
            length = len(self._array)
            self._array.append(self._array[length-1])
            self._size += 1
            removed = self._array[index]
            for j in range(length-1, index, -1):
                self._array[j] = self._array[j-1]
            self._array[index] = value
        else:
            raise RuntimeError(f'index {index}, out of bounds')


    def __repr__(self):
        return f'TestArray({self._size!r}, {str(self._array)})'


def main():
    logging.basicConfig(filename="logs/array_operations_log.txt", encoding="utf-8",
                        format='%(asctime)s, %(levelname)s: %(message)s', level=logging.DEBUG)
    _logger.info("Started ...")

    arr = TestArray(3)
    print(arr)
    arr.set_at_index(0, 1)
    arr.set_at_index(1, "AAPL")
    arr.set_at_index(2, set())
    _logger.info(arr)

    arr.insert_at_index(0, "First")
    arr.insert_at_index(1, "AMD")
    arr.insert_at_index(2, dict())

    arr.remove_at_index(2)
    _logger.info(arr)
    _logger.info(arr.get_at_index(0))

    a2 = TestArray(6, ['First', 'AAPL', set(), 1, 'AMD', dict()])
    _logger.info(a2)

if __name__ == "__main__":
    main()
