from flask import Blueprint, Response
import json
from api.utils.data_loader import load_station_data

stations_bp = Blueprint('stations', __name__)

@stations_bp.route('/barrier-free-data', methods=['GET'])
def get_barrier_free_data():
    """バリアフリー情報を提供するAPI"""
    data = load_station_data()
    response_json = json.dumps(data, ensure_ascii=False)  # Unicodeエスケープを防ぐ
    return Response(response_json, content_type="application/json; charset=utf-8"), 200
