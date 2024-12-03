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
user_message = {'role': 'assistant', 'content': '很实际的一句话，一个男人啥都提供不了，人不顶用，钱没影踪，爱不存在，时间没有，关键是脾气还恶劣，那你留着他干啥？竖牌坊吗？女人呢？若想日子美，记住一句话，谁对你真心，你就对谁真心，留不住的事物，那就一脚踢开。到如今你都没搞懂，靠山山会塌，靠人人会走，与其用一辈子去赌自己的依靠，倒不如自己做自己的依靠。2024年送你们四字真谛，记住了就能顺风顺水。不听瞎编，不吃空话，不搞救济，不收废物 '}
messages.append(user_message)


start = time.time()

for i in range(1, 40):
    ai_message = chat_request(client=client, messages=messages)
    print(f'第{i}次调用', ai_message)
    messages.append(ai_message)
    messages.append(user_message)
    
print(messages)
end = time.time()

print(f"最终执行时间{end - start}")


with open('finial5.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii=False, indent=4 )
