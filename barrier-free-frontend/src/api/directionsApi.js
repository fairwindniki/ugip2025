import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_BACKEND_URL;

/**
 * バリアフリー対応のルートを取得する
 * @param {string} start - 出発地の緯度・経度（例: "35.6895,139.6917"）
 * @param {string} end - 目的地の緯度・経度（例: "35.6812,139.7671"）
 * @returns {Promise} - ルートデータ（Google Maps Directions API のレスポンス）
 */
export const getBarrierFreeRoute = async (start, end) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/directions`, {
      params: { start, end },
    });
    return response.data;
  } catch (error) {
    console.error("ルート取得エラー:", error);
    return null;
  }
};
