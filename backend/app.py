import os
from openai import OpenAI
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import json
from flask_cors import CORS

app = Flask(__name__)
load_dotenv()
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    # 클라이언트로부터 요청 데이터 받기
    data = request.json
    user_input = data.get('message')

    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # OpenAI GPT 모델 호출
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # 사용할 모델 이름
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # GPT 모델의 응답 처리 (올바른 접근 방식으로 수정)
        gpt_response = completion.choices[0].message.content.strip()

        # 결과를 JSON 형식으로 반환 (json.dumps로 ensure_ascii=False 설정)
        response_data = json.dumps({'response': gpt_response}, ensure_ascii=False)

        return app.response_class(
            response=response_data,
            mimetype='application/json',
            status=200
        )
    except Exception as e:
        # 에러 발생 시 에러 메시지 반환
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
