# Selenium と Python を使用した簡単な例

## 始めましょう

- ランタイムバーションをインストールする (python)

```
$ asdf install
```

- ローカル環境使用して開発出来ますが、別の仮想環境を成立を作成して、その環境を使用することをお勧めします。それにより、コンフリクトを回避することができる

```
$ python -m venv .venv && source .venv/bin/active
```

- `requirements.txt`で定義された依存パッケージをインストールする

```
$ pip install -r requirements.txt
```

- ``PYTHONPATH`` を設定する

```
$ ./entry.sh
```

## テストスイーツ

- テストスイーツが色々なテストケースを含んでいます、テストスイーツを実行するために下のコマンドを実行する

```
$ python ./src/test_suites/<テストスイーツ名>.py
```