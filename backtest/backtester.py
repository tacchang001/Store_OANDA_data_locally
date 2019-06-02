
from backtest.market import Market
from backtest.strategy import Strategy
from backtest.Trade import Trade


class BackTest:
    """
    バックテスト本体。
    """
    def __init__(self, market, strategy):
        self.market = market
        self.strategy = strategy
        self.trade = Trade()

    def run(self):
        i = 0
        for candle in self.market:
            buy_exit = self.strategy.buy_exit(candle, self.trade.get_orders())
            self.trade.remove_orders(buy_exit)
            buy_entry = self.strategy.buy_entry(i, candle)
            self.trade.add_orders(buy_entry)
            if i > 30:
                break
            i += 1
