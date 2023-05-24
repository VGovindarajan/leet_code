import logging
from queue import PriorityQueue
import typing

_logger = logging.getLogger("smallest_cost")

def calculate_cost(nums:[int]) -> int:
    q = PriorityQueue()
    for n in nums:
        q.put(n)

    total_cost = 0
    while q.qsize() > 1:
        first = q.get()
        q.task_done()
        second = q.get()
        q.task_done()
        cost = first + second
        q.put(cost)
        print(cost)
        total_cost += cost

    return total_cost

def main():
    #nums = [1, 2, 3, 4]
    nums = [5, 8, 6, 1]
    cost = calculate_cost(nums)
    print(cost)


if __name__ == "__main__":
    main()