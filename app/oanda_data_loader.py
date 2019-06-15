from oandapyV20.exceptions import V20Error
import dateutil
import pprint
import json
import argparse

import oanda_csv.oanda_account as account
import oandaV20helper.endpoints.instruments as v20

_ASK = 'A'
_MID = 'M'
_BID = 'B'


def main(args):
    try:
        _id, _token = account.read_oanda_authz()
        d = {}
        for price in [_ASK, _MID, _BID]:
            _param = v20.make_instruments_params(
                granularity=args.granularity,
                price=price,
                from_time=args.starttime,
                to_time=args.endtime
            )
            d[price] = v20.get_candles(
                access_token=_token,
                instrument=args.instrument,
                param=_param
            )
            pprint.pprint(d[price])
        fn = "{}_{}_{}.json".format(
            args.instrument,
            args.granularity,
            args.starttime.strftime('%Y%m%d_%H%M')
        )
        merge_price(fn, args.granularity, args.instrument, d[_ASK], d[_MID], d[_BID])

    except V20Error as ev20:
        print("OANDA Error: {}".format(ev20))
    except Exception as er:
        print("異常終了: {}".format(er))


def valid_date(s):
    try:
        return dateutil.parser.parse(s)
    except ValueError:
        msg = "Invalid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def merge_price(file_name, granularity, instrument, ask, mid, bid):
    d = []
    dtime = [row['time'] for row in ask['candles']]
    dcomplete = [row['complete'] for row in ask['candles']]
    dvolume = [row['volume'] for row in ask['candles']]
    dask = [row['ask'] for row in ask['candles']]
    dmid = [row['mid'] for row in mid['candles']]
    dbid = [row['bid'] for row in bid['candles']]
    for i in range(len(dtime)):
        d.append({
            'time': dtime[i],
            'complete': dcomplete[i],
            'volume': dvolume[i],
            'ask': dask[i],
            'mid': dmid[i],
            'bid': dbid[i]
        })
    r = {'candles': d, 'granularity': granularity, 'instrument': instrument}
    # print(print(json.dumps(r, indent=2)))
    fw = open(file_name, 'w')
    # json.dump(r, fw, indent=4)
    fw.close()


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

    args = parser.parse_args()
    print(args)

    main(args)
