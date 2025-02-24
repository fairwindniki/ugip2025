from flask import Flask, Response
from flask_cors import CORS
from api.routes.stations import stations_bp
from api.routes.directions import directions_bp
import json
from dotenv import load_dotenv

# .env を読み込む
load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(stations_bp, url_prefix='/api')
app.register_blueprint(directions_bp, url_prefix='/api')

@app.route("/")
def home():
    """ルートページを表示（Unicodeエスケープせずに返す）"""
    response_data = {"message": "バリアフリールート検索APIへようこそ！"}
    response_json = json.dumps(response_data, ensure_ascii=False)  # Unicodeエスケープを防ぐ
    return Response(response_json, content_type="application/json; charset=utf-8"), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
