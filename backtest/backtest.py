
from backtest.market import Market
from backtest.strategy import Strategy


class BackTest:
    """
    バックテスト本体。
    """
    def __init__(self, ohlc, strategy):
        self.market = Market(ohlc)
        self.strategy = strategy

    def run(self):
        i = 0
        for c in self.market:
            o = self.strategy.order(c)
            print(o)
            if i > 10:
                break
            i += 1
