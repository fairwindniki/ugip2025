// barrier-free-frontend/src/components/SupplementaryInfo.jsx
import { useEffect, useState } from "react";
import PropTypes from "prop-types";
import axios from "axios";

const SupplementaryInfo = ({ start, end }) => {
  const [info, setInfo] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (start && end) {
      setLoading(true);
      axios
        .get(import.meta.env.VITE_BACKEND_URL + "/api/supplementary", {
          params: { start, end },
        })
        .then((response) => {
          setInfo(response.data.supplementary_info);
          setError("");
        })
        .catch((err) => {
          console.error("補足情報取得エラー:", err);
          setError("補足情報の取得に失敗しました。");
        })
        .finally(() => {
          setLoading(false);
        });
    }
  }, [start, end]);

  if (loading) return <p className="loading">補足情報を取得中...</p>;
  if (error) return <p className="error">{error}</p>;
  if (!info) return null;

  return (
    <div className="supplementary-info">
      <h2>補足情報</h2>
      <p>{info}</p>
    </div>
  );
};

SupplementaryInfo.propTypes = {
  start: PropTypes.string.isRequired,
  end: PropTypes.string.isRequired,
};

export default SupplementaryInfo;
