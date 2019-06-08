# Store_OANDA_data_locally
OANDAのデータをローカルDBに保存する。いつでもダウンロードできるけど大量＆頻繁にダウンロードするのは申し訳ない。

```uml

@startuml

class "為替レート" as CandleStick {
      open:
      high:
      low:
      close:
}
' 制約をノートとして記述する
note top of CandleStick
     {値動きの履歴}
end note

class "注文" as Order {
      指値:
      売りor買い
      期限:
      
      注文()
      キャンセル()
}

abstract class "為替指数" as TechnicalIndicator {
  value:
}

class "移動平均" as MA {
  value:
}

class "MACD" as MACD {
  value:
}

class "売買戦略" as Strategy {

}

class "バックテスト" as Backtest {

}

MA --|> TechnicalIndicator
MACD --|> TechnicalIndicator

TechnicalIndicator --> CandleStick
Order --> CandleStick
Strategy --> TechnicalIndicator
Strategy --> CandleStick
Strategy --> Order
Backtest --> CandleStick
Backtest --> Strategy

@enduml

```
