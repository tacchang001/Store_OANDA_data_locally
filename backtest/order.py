from enum import Enum
from datetime import datetime

from util.json_adapter import JsonAdapter


class OrderSide(Enum):
    """
    必須 注文単位
    """
    BUY = "buy",
    SELL = "sell",
    INVALID = "none"


class OrderType(Enum):
    """
    必須 注文のタイプ。'limit','stop','marketIfTouched','market'のいずれか。
    """
    LIMIT = "limit",
    STOP = "stop",
    MARKET_IF_TOUCHED = "marketIfTouched",
    MARKET = "market",
    INVALID = "none"


class OrderBuy(JsonAdapter):
    """
    units : int
        必須 注文単位
    side : OrderSide
        必須 売買区別（buy=買い、sell=売り）
    type : OrderType
        必須。注文のタイプ。
        'limit','stop','marketIfTouched','market'のいずれか。
    expiry : datetime
        必須 注文の有効期限。
        注文のタイプが'limit','stop','marketIfTouched'のいずれか。
    price : int
        注文がトリガー（発動）する価格。
        注文のタイプが'limit','stop','marketIfTouched'のいずれかの場合、
        注文が発動る価格を設定。
    """
    def __init__(self):
        self.units = 0
        self.side = OrderSide.INVALID
        self.type = OrderType.INVALID
        self.expiry = datetime.today()
        self.price = 0

    def __str__(self):
        return "<units:{} side:{} type:{} expiry:{} price:{}>".format(
            self.units,
            self.side.value,
            self.type.value,
            self.expiry.strftime('%Y/%m/%d'),
            self.price
        )
