from flask import Blueprint, Response, request, jsonify
import requests
import os
import json
from api.utils.data_loader import load_station_data

directions_bp = Blueprint('directions', __name__)

# Google Maps APIキー（環境変数から取得）
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_barrier_free_entrance(entrances):
    """
    駅の出入口情報からバリアフリー対応のものを取得
    """
    bf_entrances = [e for e in entrances if e["barrier_free"]]
    return bf_entrances[0] if bf_entrances else None

def find_stations_along_route(start, end):
    """
    出発地と目的地の間にある駅を検索し、バリアフリー対応の出入口を経由地に追加
    """
    stations = load_station_data()
    waypoints = []

    for station in stations:
        bf_entrance = get_barrier_free_entrance(station["entrances"])
        if bf_entrance:
            waypoints.append(f"{bf_entrance['lat']},{bf_entrance['lng']}")

    return waypoints

@directions_bp.route('/directions', methods=['GET'])
def get_directions():
    """
    ルート検索API
    """
    start = request.args.get("start")  # 出発地（例: 35.6895,139.6917）
    end = request.args.get("end")  # 目的地（例: 35.6812,139.7671）

    if not start or not end:
        return jsonify({"error": "出発地と目的地を指定してください"}), 400

    # ルート上のバリアフリー経由地を取得
    waypoints = find_stations_along_route(start, end)

    # Google Maps Directions API にリクエスト
    directions_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": start,
        "destination": end,
        "waypoints": "|".join(waypoints) if waypoints else None,
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(directions_url, params=params)
    data = response.json()

    # Unicode エスケープを防ぎ、整形して出力
    response_json = json.dumps(data, ensure_ascii=False, indent=2)

    return Response(response_json, content_type="application/json; charset=utf-8"), 200
