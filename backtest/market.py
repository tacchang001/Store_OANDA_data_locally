from pandas import DataFrame

from backtest.indicators import ext_ohlc, iMA


class Market:
    """

    """
    def __init__(self, ohlc):
        self.ohlc = ohlc
        self.num = len(ohlc)

        self.sma_5 = DataFrame()
        self.sma_25 = DataFrame()

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= self.num:
            raise StopIteration()
        i = self.current
        self.current += 1
        return self.ohlc.iloc[i]

    def get_sma_5(self, index):
        if len(self.sma_5) <= 1:
            ohlc_ext = ext_ohlc(self.ohlc)
            self.sma_5 = iMA(ohlc_ext, 5, ma_method='SMA')
        return self.sma_5.iloc[index]

    def get_sma_25(self, index):
        if len(self.sma_25) <= 1:
            ohlc_ext = ext_ohlc(self.ohlc)
            self.sma_25 = iMA(ohlc_ext, 25, ma_method='SMA')
        return self.sma_25.iloc[index]
