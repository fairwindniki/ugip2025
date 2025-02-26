import { useState } from "react";
import axios from "axios";
import PropTypes from "prop-types";

const OcrUploader = ({ onOcrResult }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("image", selectedFile);
    try {
      const response = await axios.post(
        import.meta.env.VITE_BACKEND_URL + "/api/ocr",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      onOcrResult(response.data);
    } catch (error) {
      console.error("OCRアップロードエラー:", error);
    }
    setLoading(false);
  };

  return (
    <div className="ocr-uploader">
      <h2>バリアフリーマップ画像からOCR</h2>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "処理中..." : "OCR実行"}
      </button>
    </div>
  );
};

OcrUploader.propTypes = {
  onOcrResult: PropTypes.func.isRequired,
};

export default OcrUploader;
