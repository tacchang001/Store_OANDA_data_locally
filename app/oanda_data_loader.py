# http://swdrsker.hatenablog.com/entry/2018/05/18/070000

from oandapyV20.exceptions import V20Error
import dateutil
import pandas
import json
import argparse

import oanda_csv.oanda_account as account
import oandaV20helper.endpoints.instruments as v20


def main(args):
    try:
        _id, _token = account.read_oanda_authz()
        _param = v20.make_instruments_params(
            granularity=args.granularity,
            price=args.price,
            from_time=args.starttime,
            to_time=args.endtime
        )
        res = v20.get_candles(
            access_token=_token,
            instrument=args.instrument,
            param=_param
        )
        # print(json.dumps(request.response, indent=2))
        jfn = "{}_{}_{}_{}.json".format(
            args.instrument,
            args.granularity,
            args.price,
            args.starttime.strftime('%Y%m%d_%H%M')
        )
        fw = open(jfn, "w")
        json.dump(res, fw, indent=4)

        # df1 = pandas.DataFrame({'time': [row['time'] for row in _res['candles']]})
        # df2 = pandas.DataFrame.from_dict([row['mid'] for row in _res['candles']])
        # df2 = df2.ix[:, ['o', 'h', 'l', 'c']]
        # df3 = pandas.DataFrame({'volume': [row['volume'] for row in _res['candles']]})
        # candle = pandas.concat([df1, df2, df3], axis=1)
        #
        # candle.to_csv(
        #     "{}_{}_{}.csv".format(
        #         args.instrument,
        #         args.granularity,
        #         args.starttime.strftime('%Y%m%d_%H%M')
        #     ),
        #     index=False)

    except V20Error as ev20:
        print("OANDA Error: {}".format(ev20))
    except Exception as er:
        print("異常終了: {}".format(er))


def valid_date(s):
    try:
        return dateutil.parser.parse(s)
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OANDA V20 data loader')

    parser.add_argument("instrument",
                        metavar='I',
                        help="Name of the Instrument")
    parser.add_argument('-g',
                        "--granularity",
                        help="The granularity of the candlesticks to fetch [default=M1]",
                        default="M1")
    parser.add_argument('-s',
                        "--starttime",
                        help="The start of the time range to fetch candlesticks for.",
                        required=True,
                        type=valid_date)
    parser.add_argument('-e',
                        "--endtime",
                        help="The end of the time range to fetch candlesticks for.",
                        required=True,
                        type=valid_date)
    parser.add_argument('-p',
                        "--price",
                        help="The Price component(s) to get candlestick data for.",
                        default='M')

    args = parser.parse_args()
    print(args)

    main(args)
