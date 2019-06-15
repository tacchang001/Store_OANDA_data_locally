import pandas as pd

from backtest.indicators import ext_ohlc, iMA


class Market:
    """

    """
    def __init__(self, candles):
        self.candles = candles
        _times = pd.DataFrame({'time': [row['time'] for row in self.candles]})
        _candles = pd.DataFrame.from_dict([row['mid'] for row in self.candles])
        _candles_columns = ['o', 'h', 'l', 'c']
        _candles = _candles.ix[:, _candles_columns]
        for name in _candles_columns:
            _candles[name] = _candles[name].astype('float')
        _volumes = pd.DataFrame({'volume': [row['volume'] for row in self.candles]})
        self.mids = pd.concat([_times, _candles, _volumes], axis=1)
        self.num = len(candles)

        self.sma_5 = pd.DataFrame()
        self.sma_25 = pd.DataFrame()

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= self.num:
            raise StopIteration()
        i = self.current
        self.current += 1
        return self.candles.iloc[i]

    def get_sma_5(self, index):
        if len(self.sma_5) <= 1:
            ohlc_ext = ext_ohlc(self.mids)
            self.sma_5 = iMA(ohlc_ext, 5, ma_method='SMA')
        return self.sma_5.iloc[index]

    def get_sma_25(self, index):
        if len(self.sma_25) <= 1:
            ohlc_ext = ext_ohlc(self.mids)
            self.sma_25 = iMA(ohlc_ext, 25, ma_method='SMA')
        return self.sma_25.iloc[index]
