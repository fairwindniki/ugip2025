from flask import Blueprint, request, jsonify, Response
import pytesseract
from PIL import Image
import json
from api.utils.ai_utils import process_barrier_free_map_with_gemini

ocr_bp = Blueprint('ocr', __name__)

@ocr_bp.route('/ocr', methods=['POST'])
def process_ocr():
    """
    OCR 処理 API  
    画像ファイルを受け取り、OCR 実行後、Gemini API を利用してバリアフリー情報の JSON を生成する
    """
    if 'image' not in request.files:
        return jsonify({"error": "画像ファイルが必要です"}), 400

    file = request.files['image']
    try:
        image = Image.open(file.stream)
        # pytesseract で OCR を実行
        ocr_result = pytesseract.image_to_string(image, lang='jpn')
        # Gemini API を用いて OCR 結果から構造化データ（JSON）を生成
        structured_data = process_barrier_free_map_with_gemini(ocr_result)
        result = {
            "ocr_text": ocr_result,
            "structured_data": structured_data
        }
        response_json = json.dumps(result, ensure_ascii=False, indent=2)
        return Response(response_json, content_type="application/json; charset=utf-8"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
