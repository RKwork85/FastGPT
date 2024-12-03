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



list1 = []
with open('ttt', 'r', encoding='utf-8') as f:
        for index in f:
            # index = index.replace('\n', '')
            list1.append(index)


result_data = []
for i in list1:            
    with open('XiaWeiID8', 'r', encoding='utf-8') as file:
        for index in file:
            font_str = index.replace('\n','')
            data = font_str + i
            result_data.append(data)


with open('final.txt', 'w', encoding='utf-8') as f:
     for i in result_data:
          f.write(i)