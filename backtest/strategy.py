from backtest.order import Order


class Strategy:
    """

    """
    def __init__(self):
        pass

    def buy_entry(self, candle):
        o1 = Order()
        o2 = Order()
        return [o1, o2]

    def buy_exit(self, candle, *orders):
        for order in orders:
            print(order)
        return orders

    def sell_entry(self, candle):
        pass

    def sell_exit(self, candle, *orders):
        pass
