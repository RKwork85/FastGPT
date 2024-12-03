'''
api 对接fastgpt平台模型

'''

# 1 Http方式
'''
curl http://127.0.0.1:3000/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fastgpt-ccmeCIJp1cfdFaB2vbyIDoDrfzHn7tcQFUrErJNb8Owy8AKxlWI8fO" \
  -d '{
    "model": "glm-4",
    "messages": [
      {
        "role": "system",
        "content": "帮助用户解决问题."
      },
      {
        "role": "user",
        "content": "实验室的预约规则"
      }
    ],
    "stream": true
  }'
  
'''



import requests   # 方式二：fastgpt 鉴权方式 可用

url = "http://154.211.13.226:3000/api/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer fastgpt-ytTG4tyIyBr3XAMqZ7jSywfnTj3u1y1tI45gRrXyKYokXprNnlaq"
}
data = {
    "model": "glm-4",
    "messages": [
        {
            "role": "user",
            "content": "第一关第一个"
        }
    ],
    "stream": True,
    "detail":True
}

response = requests.post(url, json=data, headers=headers, stream=True)
print(response.text)
# 打印响应内容
for line in response.iter_lines(decode_unicode=True):
    if line:
        print(line)
# data: {"id":"","object":"","created":0,"model":"","choices":[{"delta":{"role":"assistant","content":"如有"},"index":0,"finish_reason":null}]}





# from openai import OpenAI    # 方式三：openai API-KEY 方式



# client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="fastgpt-iZd67F13vcdaco09rqFdp0FMzISEcJGRxtgcsPFSa89NGTySExLFIJ")         # 需要在onepai平台中 添加渠道生成令牌

# stream = client.chat.completions.create(
#     model="doubao-pro-128k",
#     messages=[{"role": "user", "content": "写一篇800字的文章，题目为：论当代大学生的社会担当"}],
#     stream=True,
    
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")