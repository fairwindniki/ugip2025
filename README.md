barrier-free-backend/
│── api/                    # API関連の処理
│   ├── __init__.py          # Flaskアプリの初期化
│   ├── routes/              # APIエンドポイント管理
│   │   ├── __init__.py
│   │   ├── stations.py      # 駅データの提供
│   │   ├── directions.py    # 経路検索API
│   │   ├── ocr.py           # OCR関連のAPI
│   ├── utils/               # ヘルパー関数（データ処理など）
│   │   ├── __init__.py
│   │   ├── data_loader.py   # JSONやCSVを読み込む処理
│   │   ├── geo_utils.py     # 経路上の駅判定ロジック
│── data/                    # データ（CSV, JSON, OCR結果など）
│   ├── stations.json        # 統合バリアフリー情報
│   ├── raw/                 # 元データ（CSV, 画像など）
│── tests/                   # テストコード
│   ├── test_stations.py
│   ├── test_directions.py
│── app.py                   # Flaskアプリのエントリーポイント
│── config.py                # 環境変数や設定
│── requirements.txt          # 依存関係（Poetryでなくpipの場合）
│── pyproject.toml            # Poetryの設定ファイル
│── poetry.lock               # Poetryの依存管理ファイル
│── .gitignore                # Git無視ファイル
│── README.md                 # プロジェクト説明


barrier-free-frontend/
├── public/                    # 静的ファイル
│   ├── index.html              # ルートHTMLファイル
├── src/                        # アプリのメインソース
│   ├── assets/                 # 画像やスタイル
│   ├── components/             # 再利用可能なUIコンポーネント
│   │   ├── Map.jsx             # Google Maps 表示コンポーネント
│   │   ├── SearchBar.jsx       # 出発地・目的地入力コンポーネント
│   │   ├── RouteInfo.jsx       # ルート情報表示コンポーネント
│   ├── pages/                  # 画面ごとのコンポーネント
│   │   ├── Home.jsx            # メイン画面（地図 + 検索バー）
│   ├── api/                    # API関連
│   │   ├── directionsApi.js    # ルート検索APIリクエスト
│   ├── styles/                 # スタイル関連
│   │   ├── global.css          # 全体のスタイル
│   ├── App.jsx                 # メインのアプリケーションコンポーネント
│   ├── main.jsx                 # Reactエントリーポイント
├── .env                        # 環境変数（APIキーなど）
├── package.json                # npmパッケージ管理
├── vite.config.js              # Vite設定ファイル

