import os
import json 
import time
from openai import OpenAI

question_data = ['讲一个故事吧']

os.environ['ARK_API_KEY'] ="e963ee3a-0366-47e7-a928-d269b55cad2c"       ## 2 在模型API中生成密钥

client = OpenAI(
    api_key=os.getenv("ARK_API_KEY"), 
    base_url="https://ark.cn-beijing.volces.com/api/v3",            ## 1 地址要对
)

def chat_request( question):

    completion = client.chat.completions.create(
        model="ep-20250227185525-44mvs",                                            ## 3 模型接入点要对
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.无论得到什么内容只会回复谢谢'},
            {'role': 'user', 'content': f'{question}'}],
        )
    
    completion_cp = completion.model_dump_json()
    data = json.loads(completion_cp)
    # 文本信息
    print(data["choices"][0]['message']['content'])
    
start = time.time()
chat_request(question=question_data)
end = time.time()
print(f"最终执行时间{end - start}")

