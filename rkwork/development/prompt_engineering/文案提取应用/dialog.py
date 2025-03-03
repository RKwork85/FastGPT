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



client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="prechengwenai-o7KMlfoYm5HelRE4XqYdS4TQRcsS5H5PfExeGdrXkq4w3Gr9dEj78wI")
messages = []
user_question ="""
针对一款产品属性生成一条口播的文案：
语言风格：自然，正常，生活场景词汇；
内容：自己对产品的感受，过往的经历，站在观众的角度去感受；
过渡：不要有直接明显的过渡词汇
产品：速惟 宽下摆运动内衣
中强度：瑜伽伴侣 稳固不上窜
设计卖点：
1.加长背心式，外穿不尴尬
2.侧翼加高，隐藏副乳，贴合不溢
3.V 形美背，凸显背后曲线更显瘦
4.加宽下摆，舒适不勒腰
5.固定胸杯，增加承托力，穿着更稳定运动不跑位
只生成文案
"""

user_message = {'role': 'user', 'content': f'{user_question}'}
messages.append(user_message)


start = time.time()

for i in range(1, 3):
    ai_message = chat_request(client=client, messages=messages)
    print(f'第{i}次调用', ai_message)
    messages.append(ai_message)
    messages.append(user_message) 
    
print(messages)
end = time.time()

print(f"最终执行时间{end - start}")


resultData = []
for index, value  in enumerate(messages, start=1):
    if value["role"]== "assistant":
        resultData.append({"产品编号": "S3SS8529","ID":index // 2, "文案内容":value["content"]})


with open('result2.json', 'w', encoding='utf-8') as f:
    json.dump(resultData, f, ensure_ascii=False, indent=4 )
