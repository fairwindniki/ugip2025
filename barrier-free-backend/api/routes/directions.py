from flask import Blueprint, Response, request, jsonify
import requests
import json
from api.utils.data_loader import load_station_data
from api.utils.geo_utils import is_station_on_route
from config import Config

directions_bp = Blueprint('directions', __name__)

def get_barrier_free_entrance(entrances):
    """駅の出入口情報からバリアフリー対応のものを取得"""
    bf_entrances = [e for e in entrances if e.get("barrier_free")]
    return bf_entrances[0] if bf_entrances else None

def find_stations_along_route(start, end):
    """
    出発地と目的地間にある駅を検索し、バリアフリー対応出入口の座標を経由点として抽出
    """
    stations = load_station_data()
    waypoints = []
    for station in stations:
        if is_station_on_route(start, end, station):
            bf_entrance = get_barrier_free_entrance(station.get("entrances", []))
            if bf_entrance:
                waypoints.append(f"{bf_entrance['lat']},{bf_entrance['lng']}")
            else:
                waypoints.append(f"{station['lat']},{station['lng']}")
    return waypoints

@directions_bp.route('/directions', methods=['GET'])
def get_directions():
    """
    経路検索API  
    出発地・目的地に加え、ルート上の駅（バリアフリー出入口）を経由点として組み込む
    """
    start = request.args.get("start")  # 例："35.6895,139.6917"
    end = request.args.get("end")      # 例："35.6812,139.7671"
    if not start or not end:
        return jsonify({"error": "出発地と目的地を指定してください"}), 400

    waypoints = find_stations_along_route(start, end)
    directions_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": start,
        "destination": end,
        "key": Config.GOOGLE_MAPS_API_KEY,
    }
    if waypoints:
        params["waypoints"] = "|".join(waypoints)

    response = requests.get(directions_url, params=params)
    data = response.json()
    response_json = json.dumps(data, ensure_ascii=False, indent=2)
    return Response(response_json, content_type="application/json; charset=utf-8"), 200