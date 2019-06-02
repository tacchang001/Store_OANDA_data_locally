import pandas as pd


class Market:
    """

    """
    def __init__(self, ohlc):
        self.ohlc = ohlc
        self.num = len(ohlc)

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= self.num:
            raise StopIteration()
        i = self.current
        self.current += 1
        return self.ohlc.iloc[i]
