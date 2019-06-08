from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import pandas as pd

_TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


def get_candles(access_token, instrument, param):
    _api = API(access_token=access_token, environment="practice")
    _request = instruments.InstrumentsCandles(instrument=instrument, params=param)
    _api.request(_request)

    return _request.response


def to_dataframe(candle_dict, base='mid'):
    candle = pd.DataFrame.from_dict([row[base] for row in candle_dict['candles']])
    candle['time'] = [row['time'] for row in candle_dict['candles']]
    candle['time'] = pd.to_datetime(candle['time'], format=_TIMESTAMP_FORMAT)
    candle['volume'] = [row['volume'] for row in candle_dict['candles']]
    for name in ['o', 'h', 'l', 'c']:
        candle[name] = candle[name].astype('float')

    return candle


def make_instruments_params(granularity, price, from_time=None, to_time=None, count=None):
    if from_time is not None and to_time is not None:
        _params = _make_from_to_params(granularity, price, from_time=from_time, to_time=to_time)
    elif from_time is None and to_time is not None and count is None:
        _params = _make_to_params(granularity, price, to_time=to_time)
    elif from_time is not None and to_time is None and count is not None:
        _params = _make_from_count_params(granularity, price, from_time=from_time, count=count)
    elif from_time is None and to_time is not None and count is not None:
        _params = _make_to_count_params(granularity, price, to_time=to_time, count=count)
    else:
        _params = {
            "granularity": granularity
        }

    return _params


def _make_from_to_params(granularity, price, from_time, to_time):
    _params = {
        "from": from_time.strftime(_TIMESTAMP_FORMAT),
        "to": to_time.strftime(_TIMESTAMP_FORMAT),
        "granularity": granularity,
        "price": price
    }

    return _params


def _make_to_params(granularity, price, to_time):
    _params = {
        "to": to_time.strftime(_TIMESTAMP_FORMAT),
        "granularity": granularity,
        "price": price
    }

    return _params


def _make_from_count_params(granularity, price, from_time, count):
    _params = {
        "from": from_time.strftime(_TIMESTAMP_FORMAT),
        "count": count,
        "granularity": granularity,
        "price": price
    }

    return _params


def _make_to_count_params(granularity, price, to_time, count):
    _params = {
        "to": to_time.strftime(_TIMESTAMP_FORMAT),
        "count": count,
        "granularity": granularity,
        "price": price
    }

    return _params


def main():
    from datetime import datetime

    _to1 = datetime(2018, 4, 10, 12, 34, 56)
    _params1 = make_instruments_params("M15", "B", to_time=_to1)
    print(_params1)

    _from2 = datetime(2019, 3, 22, 18, 0, 0)
    _to2 = datetime(2019, 3, 23, 6, 0, 0)
    _params2 = make_instruments_params("M15", "M", from_time=_from2, to_time=_to2)
    print(_params2)

    _from3 = datetime(2018, 4, 10, 0, 0, 0)
    _count3 = 30
    _params3 = make_instruments_params("M15", "A", from_time=_from3, count=_count3)
    print(_params3)

    _to4 = datetime(2018, 4, 10, 0, 0, 0)
    _count4 = 40
    _params4 = make_instruments_params("M15", "B", to_time=_to4, count=_count4)
    print(_params4)


if __name__ == "__main__":
    main()
