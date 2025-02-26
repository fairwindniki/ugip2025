# barrier-free-backend/api/utils/geo_utils.py
import math

def haversine_distance(lat1, lng1, lat2, lng2):
    """2点間の距離(km)を計算"""
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlng/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def is_station_on_route(start, end, station, threshold=0.5):
    """
    出発地と目的地の直線からの駅のずれを計算し、閾値以内ならルート上にあると判断  
    start, end: "lat,lng"形式の文字列  
    station: {"lat": ..., "lng": ...}を含む辞書
    """
    try:
        start_lat, start_lng = map(float, start.split(","))
        end_lat, end_lng = map(float, end.split(","))
        station_lat = station.get("lat")
        station_lng = station.get("lng")
        d1 = haversine_distance(start_lat, start_lng, station_lat, station_lng)
        d2 = haversine_distance(station_lat, station_lng, end_lat, end_lng)
        d_total = haversine_distance(start_lat, start_lng, end_lat, end_lng)
        # 三角不等式に基づき、両距離の和と直線距離の差が小さい場合、ルート上とみなす
        if abs((d1 + d2) - d_total) < threshold:
            return True
        return False
    except Exception:
        return False
