# Store_OANDA_data_locally
OANDAのデータをローカルDBに保存する。いつでもダウンロードできるけど大量＆頻繁にダウンロードするのは申し訳ない。

```uml
@startuml{Fig3.1.png}
title 簡単なクラス図

class "Order （注文）" as Order {
      dateReceived: Date [0..1]
      isPrepaid: Boolean [1]
      number: String [1]
      price: Money
      
      dispatch()
      close()
}
' 制約をノートとして記述する
note top of Order
     {if Order.customer.getCreditRating is "poor" \n then Order.isPrepaid must be true}
end note

class "Order Line （注文明細）" as OrderLine {
      quantity: Interger
      price: Money
}

class "Product （製品）" as Product {
      quantity: Interger
      price: Money
}

class "Customer （顧客）" as Customer {
      name [1]
      address [0..1]

      getCreditRating(): String
}

class "Corporate Customer （法人顧客）" as CorporateCustomer {
      contactName
      creaditRating
      creditLimit

      billForMonth(Integer)
      remind()
}

class "Personal Customer （個人顧客）" as PersonalCustomer {
      creditCardNumber
}
' 制約をノートとして記述する
note top of PersonalCustomer
     {getCreditRating() == "poor"}
end note

Order "1" --> "*" OrderLine : " lineitems {ordered}"
Order "*" --> "1" Customer
OrderLine "*" --> "1" Product
CorporateCustomer --|> Customer
PersonalCustomer --|> Customer
CorporateCustomer "*" --> "0..1" Employee : salesRep

@enduml

```
