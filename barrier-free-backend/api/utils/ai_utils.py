import os
import requests
import json

def ai_search_barrier_free(entrances):
    """
    ダミーAIによるバリアフリー出入口の検索  
    与えられた出入口情報の中から、最も適切なものを選定する（ここでは単に最初のバリアフリー出入口を返す）
    """
    bf_entrances = [e for e in entrances if e.get("barrier_free")]
    return bf_entrances[0] if bf_entrances else None

def enhance_ocr_text(ocr_text):
    """
    既存のダミーOCRテキスト補正（ここでは単純に空白・改行を整形）
    """
    lines = ocr_text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    enhanced_text = " ".join(cleaned_lines)
    return enhanced_text

def process_barrier_free_map_with_gemini(ocr_text):
    """
    Gemini API を用いて、OCRテキストからバリアフリー情報の JSON を動的に生成する  
    ※ 実際の Gemini API のエンドポイント・パラメータは利用環境に合わせて調整してください。
    """
    prompt = f"""
あなたはバリアフリーマップの専門家です。以下の OCR 結果から、駅ごとのバリアフリー情報を抽出し、下記の JSON 形式に従って出力してください。

【出力形式例】
{{
  "station_id": "unique_id",
  "station_name": "駅名",
  "lat": 35.6895,
  "lng": 139.6917,
  "entrances": [
    {{
      "entrance_id": "entrance1",
      "lat": 35.6896,
      "lng": 139.6918,
      "barrier_free": true,
      "details": "エレベーターあり"
    }},
    {{
      "entrance_id": "entrance2",
      "lat": 35.6894,
      "lng": 139.6915,
      "barrier_free": false,
      "details": "階段のみ"
    }}
  ]
}}

OCR 結果:
{ocr_text}

上記のフォーマットに従って、適切な JSON を出力してください。
    """
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
    endpoint = "https://api.gemini.example.com/v1/complete"  # 仮のエンドポイント
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GEMINI_API_KEY}"
    }
    payload = {
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.2
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception("Gemini API Error: " + response.text)
    result = response.json()
    # 仮に API レスポンスの "text" フィールドに JSON が返されるとする
    json_text = result.get("text", "")
    try:
        data = json.loads(json_text)
    except Exception as e:
        raise Exception("Invalid JSON from Gemini: " + str(e))
    return data

def get_supplementary_info(start, end):
    """
    ダミーLLMによる補足情報の生成  
    出発地と目的地をもとに、LLM（Gemini）を利用して補足情報を生成する想定。
    """
    # ここでは簡単なメッセージを返すだけとしていますが、実際は Gemini API で詳細な情報を生成
    return f"出発地({start})から目的地({end})へのルートは、障害物回避・バリアフリー対応が確認されています。推奨経路は安全かつ快適な移動をサポートします。"
