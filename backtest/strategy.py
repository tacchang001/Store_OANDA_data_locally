from backtest.order import OrderBuy


class Strategy:
    """

    """
    def __init__(self, market):
        self.market = market

    def order(self, candle):
        o = OrderBuy()
        return o
