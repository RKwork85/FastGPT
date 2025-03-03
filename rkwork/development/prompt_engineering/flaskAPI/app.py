from concurrent.futures import ProcessPoolExecutor
import json
import multiprocessing
from flask import Flask, request, jsonify
import time
from openai import OpenAI
import os

app = Flask(__name__)

os.environ['ARK_API_KEY'] = "e963ee3a-0366-47e7-a928-d269b55cad2c"

# 配置 OpenAI 客户端
client = OpenAI(
    api_key=os.getenv("ARK_API_KEY"),
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

def chat_request(questionJson):
    question = questionJson['question']
    system_prompt = questionJson["system_prompt"]
    completion = client.chat.completions.create(
        model="ep-20250227185525-44mvs",
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f'{question}'}
        ]
    )
    completion_cp = completion.model_dump_json()
    data = json.loads(completion_cp)
    questionJson.update({
        "AIresponse": data["choices"][0]['message']['content'],
    })
    return questionJson

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        print("data的内容：", data)
        tasks = data["user_questions"]

        if not tasks or not isinstance(tasks, list):
            return jsonify({"error": "请输入列表数据"}), 400

        start = time.time()
        resultList = []

        with multiprocessing.Pool(processes=20) as pool:
            results = pool.map_async(chat_request, tasks)
            for index, result in enumerate(results.get()):    
                resultList.append(result)

        end = time.time()
        print(f"最终执行时间{end - start}")

        return resultList
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2586, debug=True)