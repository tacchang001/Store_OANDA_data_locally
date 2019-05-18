# http://swdrsker.hatenablog.com/entry/2018/05/18/070000

from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.instruments as instruments
import datetime
import pandas

import oanda_csv.oanda_account as account


def main():
    try:
        _id, _token = account.read_oanda_authz()
        _start = datetime.datetime(year=2018, month=10, day=1)
        _minutes = 30*2
        _start = _start.strftime("%Y-%m-%dT%H:%M:00.000000Z")
        api = API(_token, environment="practice")
        _params = {
            "alignmentTimezone": "Japan",
            "from": _start,
            "count": _minutes,
            "granularity": "D"}
        request = instruments.InstrumentsCandles(instrument="USD_JPY", params=_params)
        api.request(request)
        # print(json.dumps(request.response, indent=2))
        df1 = pandas.DataFrame({'time': [row['time'] for row in request.response['candles']]})
        # print(df1.head)
        df2 = pandas.DataFrame.from_dict([row['mid'] for row in request.response['candles']])
        df2 = df2.ix[:, ['o', 'h', 'l', 'c']]
        # print(df2.head)
        df3 = pandas.DataFrame({'volume': [row['volume'] for row in request.response['candles']]})

        candle = pandas.concat([df1, df2, df3], axis=1)

        print(candle.head)

        candle.to_csv("candle2.csv", index=False)

    except V20Error as ev20:
        print("OANDA Error: {}".format(ev20))
    except Exception as er:
        print("異常終了: {}".format(er))


if __name__ == '__main__':
    main()
