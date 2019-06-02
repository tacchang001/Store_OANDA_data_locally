import pandas as pd


class Market:
    """

    """
    def __init__(self, ohlc):
        self.__ohlc = ohlc
        self.__num = len(ohlc)

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.__current >= self.__num:
            raise StopIteration()
        i = self.__current
        self.__current += 1
        return self.__ohlc.iloc[i]

