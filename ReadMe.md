# 取得装備一覧のスクショから、武器名を判定するやつ

## 必要なもの

    1. Google Cloud Vision APIの有効化
        参考：https://cloud.google.com/vision/docs/setup?hl=ja
        1. プロジェクトを作成する
        2. 課金を有効にする
        3. API を有効にする（Cloud Vision API）
        4. 認証を設定する（jsonのダウンロード）

    2. python
        1. python のインストール
            https://www.python.org/downloads/
        2. ライブラリのインストール
            WeaponDetector_GCV フォルダをエクスプローラーで開き、
            アドレスバーに、cmd を入力しEnter。
            コマンドプロンプトが開くので、下記コマンドを実行。
            python -m pip install -r requirements.txt

    3. batファイルにて、認証情報ファイルの指定
        1. start.bat をテキストエディタで開く。
        2. 認証情報ファイルの指定
            3行目の後ろにある
            ./.account/test-ocr-353804-96ef00b6a9b5.json
            を、1.4でダウンロードした認証情報ファイルを指すように変更する。

## 実行

    1. 画像をbatファイルにドラッグドロップする
    2. windowが生成され、読み込み結果が表示される。
        また、./out.txtに、tsvで書き込まれる。
    3. 表示された武器が正しいか確認する。
    4. ./out.txt からコピーし、スプレッドシートに張り付ける
        一部間違っている・不要なものが含まれるなどの場合、修正する

## その他設定変更

### 武器リストの変更

    1. 武器リストを生成する
        例：./data/EDF5_WEAPON_LIST_JA.txt
    2. 武器リストの指定を変更する
        batファイル3行目にある
        ./data/EDF5_WEAPON_LIST_JA.txt
        を、上記で生成したものに変更する。

### 画像トリミング位置の変更

    ./tmp/ に生成された画像を確認し、トリミング範囲がおかしかった場合に行う。
    scanWeapon_GCV.py の60行目を変更する

