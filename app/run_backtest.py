import sys
import argparse
import json
import jsonschema
import pandas as pd

from backtest.backtester import BackTest
from backtest.market import Market
from backtest.strategy import Strategy


def main(args):
    sfn = 'input_schema.json'
    with open(sfn, 'r') as sfr:
        schema = json.load(sfr)
    jsonschema.Draft4Validator.check_schema(schema)

    with open(args.json, 'r') as fr:
        json_data = json.load(fr)
    try:
        jsonschema.validate(json_data, schema)
    except jsonschema.ValidationError as e:
        print('Invalid JSON - {0}'.format(e.message), file=sys.stderr)

    # m = Market(df)
    # s = Strategy(m)
    # bt = BackTest(m, s)
    # bt.run()


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
