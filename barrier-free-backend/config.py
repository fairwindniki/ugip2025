import os

class Config:
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "YOUR_GOOGLE_MAPS_API_KEY")
    # 他の設定も必要に応じて追加
