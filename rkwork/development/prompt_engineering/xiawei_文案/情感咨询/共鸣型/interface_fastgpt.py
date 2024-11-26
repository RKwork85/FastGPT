'''
api 对接fastgpt平台模型

'''


# import requests   # 可用
# import json
# url = "http://aiagent-pre.chengwen.net/api/v1/chat/completions"
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer fastgpt-iZd67F13vcdaco09rqFdp0FMzISEcJGRxtgcsPFSa89NGTySExLFIJ"
# }
# data = {
#     "model": "doubao-pro-128k",
#     "messages": [
#         {
#             "role": "user",
#             "content": "别人在等伞，而我在等雨停。总有一段路要一个人走，总有一些事要一个人扛，也总有一份孤独需要自己一个人去承受。"
#         },
#     ],
#     "stream": False,
#     "detail":True
# }

# response = requests.post(url, json=data, headers=headers, stream=True)

# print(response.text)

# data = json.loads(response.text)
# first_response = data['responseData'][1]

# # 获取query字段的值
# query_value = first_response['historyPreview']
# print(query_value)


from openai import OpenAI



client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="fastgpt-iZd67F13vcdaco09rqFdp0FMzISEcJGRxtgcsPFSa89NGTySExLFIJ")         # 需要在onepai平台中 添加渠道生成令牌

stream = client.chat.completions.create(
    model="doubao-pro-128k",
    messages=[{"role": "user", "content": "写一篇800字的文章，题目为：论当代大学生的社会担当"}],
    stream=True,
    
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")