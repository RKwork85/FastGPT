'''
api 对接fastgpt平台模型

'''


# from openai import OpenAI


# client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="fastgpt-iZd67F13vcdaco09rqFdp0FMzISEcJGRxtgcsPFSa89NGTySExLFIJ")         # 需要在onepai平台中 添加渠道生成令牌

# stream = client.chat.completions.create(
#     model="doubao-pro-128k",
#     messages=[{"role": "user", "content": "写一篇800字的文章，题目为：论当代大学生的社会担当"}],
#     stream=True,
    
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")



## 多轮对话拿到结果
import time
import json
from openai import OpenAI
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

def chat_request(client, messages):

    completion = client.chat.completions.create(
        model="doubao-pro-128k",                                            ## 3 模型接入点要对
        messages=messages,
        )
    
    completion_cp = completion.model_dump_json()
    data = json.loads(completion_cp)
    # 文本信息
    return {'role':'assistant','content': data["choices"][0]['message']['content']}



client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="fastgpt-iZd67F13vcdaco09rqFdp0FMzISEcJGRxtgcsPFSa89NGTySExLFIJ")         # 需要在onepai平台中 添加渠道生成令牌
messages = []
user_message = {'role': 'user', 'content': '生活不是一部电影，幸福只能从彼此的珍惜中来'}
messages.append(user_message)


start = time.time()

for i in range(1, 41):
    ai_message = chat_request(client=client, messages=messages)
    print(f'第{i}次调用', ai_message)
    messages.append(ai_message)
    messages.append(user_message)
    
print(messages)
end = time.time()

print(f"最终执行时间{end - start}")


with open('finial33.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii=False, indent=4 )
