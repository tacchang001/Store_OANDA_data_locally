import sys
import argparse
import json
import jsonschema
import pandas as pd

from backtest.backtester import BackTest
from backtest.market import Market
from backtest.strategy import Strategy

# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#available-options
pd.options.display.width = 120
pd.options.display.colheader_justify = 'right'


def main(args):
    sfn = 'input_schema.json'
    with open(sfn, 'r') as sfr:
        schema = json.load(sfr)
    jsonschema.Draft4Validator.check_schema(schema)

    with open(args.json, 'r') as fr:
        candles = pd.read_json(fr.read())
    try:
        jsonschema.validate(candles, schema)
    except jsonschema.ValidationError as e:
        print('Invalid JSON - {0}'.format(e.message), file=sys.stderr)

    m = Market(candles['candles'])
    s = Strategy(m)
    bt = BackTest(m, s)
    bt.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='FX Back test')

    parser.add_argument("json",
                        metavar='json',
                        help="candle stick json file name")
    # parser.add_argument("csv",
    #                     metavar='csv',
    #                     help="candle stick csv file name")
    __args = parser.parse_args()
    print(__args)

    main(__args)
