## 概要

- AtCoderのPython用環境
- atcoder-cli(npm)とonline-judge-tools(pip3)を使用

## 使い方

(参考: atcoder-cli チュートリアル)[http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/]

1. `acc new (コンテストID)` ...コンテストIDは コンテストのURL(例: `https://beta.atcoder.jp/contests/abc101`) の最後のスラッシュ以降の英数字
    - 問題選択画面が出るのでそのままエンターを押すとA問題がダウンロードされる
    - 上下キーで移動し、スペースキーで複数選択、エンターで一括ダウンロードもできる
    - 後から追加でダウンロードする場合は`acc add`
2. 名前にコンテストIDがついたフォルダが作成されるのでそこに移動
3. `a/`というフォルダがあるのでその中で.pyファイルを作成して解答する
4. `acc submit (ファイル名)`で提出

## 環境

- Python 3.10.5
- pip 22.1.2
- Node.js v16.16.0
- npm 8.11.0

## 環境構築手順

(参考: atcoder-cli インストールガイド)[http://tatamo.81.la/blog/2018/12/07/atcoder-cli-installation-guide/]

1. node, npmがインストールされていなければする [Node.jsのHP](https://nodejs.org/ja/) ...npmも一緒に入る `node -v` `npm -v`で確認
2. Pythonがインストールされていなければする(後述)
3. `npm install -g atcoder-cli` -> `acc --version`で確認
4. `pip3 install online-judge-tools` -> `oj --version`で確認
5. `acc login` でAtCoderのユーザー名とパスワードを入力し、ログイン -> `acc session`で確認
6. `oj login https://beta.atcoder.jp/` で上と同様にログイン -> `oj login --check https://beta.atcoder.jp/` で確認

## メモ

- `pip3 freeze > requirements.txt`で`requirements.txt`を作成
- requirements.txtにいろいろ書いてあるけど、online-judge-tools以外必要かどうかよくわかっていない
