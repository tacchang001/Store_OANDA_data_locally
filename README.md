# Store_OANDA_data_locally
OANDAのデータをローカルDBに保存する。いつでもダウンロードできるけど大量＆頻繁にダウンロードするのは申し訳ない。

# Johnの起床シーケンス

- JohnはAliceからの通信をtriggerに起床します
- Johnは起床後、Bobに通知を送ります

```mermaid
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts<br/>prevail...
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
\```

