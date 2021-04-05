# Twitter API Etude
## 概要
Twitter UserStreamが使えていた時に遊んでもらっていました。

現在はUserStream廃止されたので使えません。

```
$ pip install -r requirements.txt
$ python update_name.py
```

実行前に
```python
t_ck = ''
t_cs = ''
t_tk = ''
t_ts = ''
```
それぞれ consumer_key, consumer_secret, token, token_secret を入力した後にご利用ください。

## 永続化
### nohupを利用(簡単)
```
$ nohup python update_name.py &
```

### ユニット定義ファイルの作成
1. ユニット定義ファイルの作成 。 
   
以下の```[]```で囲われているところを編集し
```service:update_name.service
/etc/systemd/system/authorizer.service
[Unit]
Description=Twitter update_name

[Service]
Type=simple
User=[user_name]
Group=[group_name]
WorkingDirectory=[tweitterディレクトリのパス]
ExecStart=python [tweitterディレクトリのパス]/update_name.py
Restart=on-failure
RestartSec=5
```
 2. サービス化
```bash
$ sudo systemctl daemon-reload
$ sudo systemctl enable update_name
$ sudo systemctl restart update_name
```
