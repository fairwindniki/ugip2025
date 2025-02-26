import json
import os

def load_station_data():
    """
    data/stations.json から駅データ（統合バリアフリー情報）を読み込む
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_path = os.path.join(base_dir, "data", "stations.json")
    with open(data_path, encoding='utf-8') as f:
        data = json.load(f)
    return data
