import { useState } from "react";
import SearchBar from "../components/SearchBar";
import Map from "../components/Map";
import RouteInfo from "../components/RouteInfo";
import SupplementaryInfo from "../components/SupplementaryInfo";
import OcrUploader from "../components/OcrUploader";
import { getBarrierFreeRoute } from "../api/directionsApi";

const Home = () => {
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [routeData, setRouteData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [ocrResult, setOcrResult] = useState(null);

  const handleSearch = async (startInput, endInput) => {
    setStart(startInput);
    setEnd(endInput);
    setLoading(true);
    const data = await getBarrierFreeRoute(startInput, endInput);
    setRouteData(data);
    setLoading(false);
  };

  const handleOcrResult = (data) => {
    setOcrResult(data);
  };

  return (
    <div className="container">
      <h1 className="title">バリアフリー経路検索</h1>
      <SearchBar onSearch={handleSearch} />
      {loading && <p className="loading">ルートを取得中...</p>}
      {routeData && <RouteInfo routeData={routeData} />}
      <SupplementaryInfo start={start} end={end} />
      <Map routeData={routeData} />
      <hr />
      <OcrUploader onOcrResult={handleOcrResult} />
      {ocrResult && (
        <div className="ocr-result">
          <h2>OCR 結果（構造化データ）</h2>
          <pre>{JSON.stringify(ocrResult.structured_data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Home;
