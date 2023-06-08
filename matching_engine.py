from enum import Enum
from datetime import datetime
from typing import List
from queue import PriorityQueue
import time

# Would be of interest to know the run time of this engine


class Side(Enum):
    BUY = 1
    SELL = -1

    @classmethod
    def from_int(cls, i):
        return cls(-1) if i < 0 else cls(1)


class Order:
    def __init__(self, size: int, trader: str, side: Side, price: float, ts: float):
        self.size = size
        self.trader = trader
        self.side = side
        self.price = price
        self.ts = ts

    @classmethod
    def from_order(cls, o):
        return cls(o.size, o.trader, o.side, o.price, o.ts)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.size},{self.trader},{self.side!r},{self.price},{self.ts})'

    # override the comparison operator
    def __lt__(self, other):
        return self.price < other.price and self.ts < other.ts


class Fill:
    def __init__(self, qty: int, trader: str, c_party: str, side: Side, price: float, ts: float):
        self.qty = qty
        self.trader = trader
        self.c_party = c_party
        self.side = side
        self.price = price
        self.ts = ts

    def __repr__(self):
        return f'{self.__class__.__name__}({self.qty},{self.trader},{self.c_party},{self.side!r},{self.price},{self.ts})'

    def __eq__(self, other):
        return self.side == other.side and self.qty == other.qty and self.trader == other.trader and self.c_party == other.c_party and self.price == other.price

class MatchingEngine:
    def __init__(self):
        self._buys = PriorityQueue()
        self._sells = PriorityQueue()
        pass

    # Get the most expensive buy order
    def get_buy(self) -> Order:
        if self._buys.empty():
            return None
        return self._buys.get()[1]

    def set_buy(self, order: Order):
        self._buys.put((order.price * -1, order))

    # Get the cheapest sell order
    def get_sell(self) -> Order:
        if self._sells.empty():
            return None
        return self._sells.get()[1]

    def set_sell(self, order: Order):
        self._sells.put((order.price, order))

    def process(self, orders: List[Order]) -> List[Fill]:
        fills = []
        for o in orders:
            print(o)
            # Buy
            if o.side == Side.BUY:
                should_process = True
                cur_buy_order = Order.from_order(o)
                while should_process:
                    resting_sell_order = self.get_sell()
                    if resting_sell_order is None:
                        self.set_buy(cur_buy_order)
                        should_process = False
                    elif resting_sell_order.price > cur_buy_order.price:
                        self.set_buy(cur_buy_order)
                        self.set_sell(resting_sell_order)
                        should_process = False
                    else:
                        price = resting_sell_order.price
                        fill_qty = min(cur_buy_order.size, resting_sell_order.size)
                        fill_ts = datetime.now().timestamp()
                        f1 = Fill(fill_qty, cur_buy_order.trader, resting_sell_order.trader, cur_buy_order.side, price,
                                  fill_ts)
                        f2 = Fill(fill_qty, resting_sell_order.trader, cur_buy_order.trader, resting_sell_order.side,
                                  price, fill_ts)
                        fills.append(f1)
                        fills.append(f2)
                        print(f1)
                        print(f2)

                        # Add the orders back if any size left
                        resting_sell_order.size = resting_sell_order.size - fill_qty
                        if resting_sell_order.size > 0:
                            self.set_sell(resting_sell_order)
                            print(f'Added back sell : {resting_sell_order}')

                        cur_buy_order.size = cur_buy_order.size - fill_qty
                        if cur_buy_order.size == 0:
                            should_process = False

            # Sell
            else:
                should_process = True
                cur_sell_order = Order.from_order(o)
                while should_process:
                    resting_buy_order = self.get_buy()
                    if resting_buy_order is None:
                        self.set_sell(cur_sell_order)
                        should_process = False
                    elif resting_buy_order.price < cur_sell_order.price:
                        self.set_buy(resting_buy_order)
                        self.set_sell(cur_sell_order)
                        should_process = False
                    else:
                        price = resting_buy_order.price
                        fill_qty = min(cur_sell_order.size, resting_buy_order.size)
                        fill_ts = datetime.now().timestamp()
                        f1 = Fill(fill_qty, cur_sell_order.trader, resting_buy_order.trader, cur_sell_order.side, price,
                                  fill_ts)
                        f2 = Fill(fill_qty, resting_buy_order.trader, cur_sell_order.trader, resting_buy_order.side,
                                  price, fill_ts)
                        fills.append(f1)
                        fills.append(f2)
                        print(f1)
                        print(f2)

                        # Add the orders back if any size left
                        resting_buy_order.size = resting_buy_order.size - fill_qty
                        if resting_buy_order.size > 0:
                            self.set_buy(resting_buy_order)
                            print(f'Added back buy : {resting_buy_order}')

                        cur_sell_order.size = cur_sell_order.size - fill_qty
                        if cur_sell_order.size <= 0:
                            should_process = False

        return fills


def main():

    o1 = Order(100, "VG", Side.BUY, 50.00, datetime.now().timestamp())
    time.sleep(0.1)
    o4 = Order(300, "C2", Side.BUY, 50.00, datetime.now().timestamp())
    time.sleep(0.1)
    o2 = Order(200, "House", Side.SELL, 50.01, datetime.now().timestamp())
    o3 = Order(200, "C1", Side.SELL, 49.99, datetime.now().timestamp())
    time.sleep(0.1)
    o5 = Order(50, "C3", Side.SELL, 49.99, datetime.now().timestamp())

    f1 = Fill(100, "C1", "VG", Side.SELL, 50.00, None)
    f2 = Fill(100, "VG", "C1", Side.BUY, 50.00, None)

    f3 = Fill(100, "C2", "C1", Side.BUY, 49.99, None)
    f4 = Fill(100, "C1", "C2", Side.SELL, 49.99, None)

    f5 = Fill(50, "C3", "C2", Side.SELL, 50.00, None)
    f6 = Fill(50, "C2", "C3", Side.BUY, 50.00, None)


    order1 = [o1, o2, o3]
    expected1 = [f1, f2]
    engine = MatchingEngine()
    actual1 = engine.process(order1)
    print(actual1)
    assert expected1 == actual1


    order2 = [o1, o2, o3, o4]
    expected2 = [f1, f2, f3, f4]
    engine = MatchingEngine()
    actual2 = engine.process(order2)
    print(actual2)
    assert expected2 == actual2


    order3 = [o1, o2, o3, o4, o5]
    expected3 = [f1, f2, f3, f4, f5, f6]
    engine = MatchingEngine()
    actual3 = engine.process(order3)
    print(actual3)
    assert expected3 == actual3

if __name__ == "__main__":
    main()
