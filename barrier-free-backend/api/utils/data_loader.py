import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../../data/stations.json")

def load_station_data():
    """JSONファイルから駅のバリアフリー情報を読み込む"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"⚠️ Error: {DATA_FILE} が見つかりません")
        return []
    except json.JSONDecodeError:
        print(f"⚠️ Error: {DATA_FILE} のJSONフォーマットが不正です")
        return []
