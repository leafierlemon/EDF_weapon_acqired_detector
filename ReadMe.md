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
        `requirements.txt` のあるフォルダをエクスプローラーで開き、  
        アドレスバーに、`cmd` を入力しEnter。  
        コマンドプロンプトが開くので、下記コマンドを実行。  
        `python -m pip install -r requirements.txt`

3. configファイルにて、認証情報ファイルの指定
    1. `config/config.json` をテキストエディタで開く。
    2. 認証情報ファイルの指定
        3行目の後ろにある  
        `"./.account/test-ocr-353804-96ef00b6a9b5.json"`  
        を、1.4でダウンロードした認証情報ファイルを指すように変更する。(WeaponDetectorGUI.pyから見たパス)

## 実行

`python ./WeaponDetectorGUI.py`

### 画像から

0. 対象画面、フィルターから、適切なものを選ぶ。  
    - 対象画面：トリミング範囲と武器リストの指定。  
    - フィルター：UP,NEW,どちらでもない、のときの表示方法
1. 画像を左下のにドラッグドロップする
2. 右の検出結果に表示される。
3. 表示された武器が正しいか確認し、間違っている・不要なものは修正する。
4. CopyTSVボタンを押下することでコピーされる。（スプレッドシートに張り付ける）

### ウィンドウから

0. キャプチャWindow、対象画面、フィルターから、適切なものを選ぶ。
    - キャプチャWindow：キャプチャする対象のWindowを指定する。左のボタンで一覧を更新可能。
    - 対象画面：トリミング範囲と武器リストの指定。  
    - フィルター：UP,NEW,どちらでもない、のときの表示方法
1. Scanを押下する
2. 右の検出結果に表示される。
3. 表示された武器が正しいか確認し、間違っている・不要なものは修正する。
4. CopyTSVボタンを押下することでコピーされる。（スプレッドシートに張り付ける）

## その他設定変更

### 武器リストの変更

1. 武器リストを生成する  
    EDF5_WEAPON_LIST_JA.txtを参考に作成し、`./config/table/`に置く。
2. 武器リストの指定を変更する  
    `./config/config.json` の`target`にて、`table`を、上記で生成したものに変更する。

### 画像トリミング位置の変更

0. `./tmp/` に生成された画像を確認し、トリミング範囲がおかしかった場合に行う。  
1. `./config/config.json` の`target`にて、`trim`を、上記で生成したものに変更する。  
    rangeは、left,top,right,bottom の順。baseは、左記rangeを指定する際の画像のwidth,height。

## 備考

- 使い捨ての管理に使用することを想定
