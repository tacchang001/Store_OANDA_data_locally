from backtest.order import Order
import numpy as np

class Strategy:
    """

    """
    def __init__(self, market):
        self.market = market

    def buy_entry(self, i, candle):
        sma_5 = self.market.get_sma_5(i)
        sma_25 = self.market.get_sma_25(i)
        if not np.isnan(sma_5) and not np.isnan(sma_25):
            o1 = Order()
            o2 = Order()
            print("order")
            return [o1, o2]
        else:
            return []

    def buy_exit(self, candle, orders):
        return []

    def sell_entry(self, candle):
        pass

    def sell_exit(self, candle, orders):
        pass
