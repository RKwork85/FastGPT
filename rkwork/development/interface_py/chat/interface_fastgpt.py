'''
api 对接fastgpt平台模型

'''

# 1 Http方式
'''
curl http://127.0.0.1:3000/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fastgpt-h07mC7ZqD919Zsa3tSps66clDLEuTr1oe2VtFbLz6Hb78l0qyWjr" \
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

# # 2 Openai 方式 不可用
# from openai import OpenAI
# import httpx

# default_headers={
#     'Authorization': 'Bearer fastgpt-xX2FbZzgsKIJIVXH1Kng0GtBY89kYXJbRZ2Bre1N1Zh0ajU6jIOW9',
#     'Content-Type': 'application/json'
# }

# http_client = httpx.Client(headers= default_headers)

# client = OpenAI(base_url="http://127.0.0.1:3000/api/v1/chat/completions", 
#                 api_key="fastgpt-xX2FbZzgsKIJIVXH1Kng0GtBY89kYXJbRZ2Bre1N1Zh0ajU6jIOW9",              # 需要在onepai平台中 添加渠道生成令牌
#                 http_client=http_client
#             )         

# stream = client.chat.completions.create(
#     model="glm-4",
#     messages=[{"role": "user", "content": "实验室预约规则"}],
#     stream=True,
    
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")



import requests   # 可用

url = "http://127.0.0.1:3000/api/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer fastgpt-h07mC7ZqD919Zsa3tSps66clDLEuTr1oe2VtFbLz6Hb78l0qyWjr"
}
data = {
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
    "stream": True
}

response = requests.post(url, json=data, headers=headers, stream=True)

# 打印响应内容
for line in response.iter_lines(decode_unicode=True):
    if line:
        print(line)
# data: {"id":"","object":"","created":0,"model":"","choices":[{"delta":{"role":"assistant","content":"如有"},"index":0,"finish_reason":null}]}



