import argparse
import pandas as pd

from backtest.backtest import BackTest
from backtest.strategy import Strategy


def main(args):
    uc = ['time', 'close', 'open', 'high', 'low']
    df = pd.read_csv(args.csv, usecols=uc, parse_dates=True)
    print(df.tail(2))
    df.columns = ['Time', 'Close', 'Open', 'High', 'Low']
    df = df.ix[:, ['Time', 'Open', 'High', 'Low', 'Close']]
    print(df.columns)

    s = Strategy()
    bt = BackTest(df, s)
    bt.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='FX Back test')

    parser.add_argument("csv",
                        metavar='csv',
                        help="candle stick csv file name")
    __args = parser.parse_args()
    print(__args)

    main(__args)
