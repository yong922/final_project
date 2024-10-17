import os
# import openai
# from flask import Flask, request, jsonify
from dotenv import load_dotenv

# app = Flask(__name__)
# load_dotenv()

os.getenv("OPENAI_API_KEY")

# OpenAI API 키 설정 (환경 변수로 저장할 것을 권장)
# openai.api_key = os.getenv("OPENAI_API_KEY")

# @app.route('/api/generate', methods=['POST'])
# def generate_text():
#     data = request.json
#     prompt = data.get('prompt', '')

#     if not prompt:
#         return jsonify({'error': 'Prompt is required'}), 400

#     try:
#         # OpenAI GPT 모델 호출
#         response = openai.Completion.create(
#             engine="text-davinci-003",  # 원하는 GPT 엔진 (또는 GPT-4)
#             prompt=prompt,
#             max_tokens=100  # 생성할 텍스트의 길이
#         )

#         # 응답을 JSON으로 변환하여 반환
#         return jsonify({
#             'response': response.choices[0].text.strip()
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

