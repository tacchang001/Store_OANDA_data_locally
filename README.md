# Store_OANDA_data_locally
OANDAのデータをローカルDBに保存する。いつでもダウンロードできるけど大量＆頻繁にダウンロードするのは申し訳ない。

```uml
@startuml samplediagram
title Sample ERDiagram
entity "entity1" {
    + id [PK]
    ==
    # entity2_id [FK(entity2,id)]
    # entity4_id [FK(entity4,id)]
    * code:varchar(64)
    name:varchar(128)
}

entity "entity2" {
}

entity "entity3" {
}

entity "entity4" {
}


entity1} o-- entity2

entity1 --{ entity3
entity1 }--{ entity4
@enduml
```
