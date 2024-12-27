from openai import OpenAI    # 方式三：openai API-KEY 方式
from openai import OpenAI    

client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="prechengwenai-ii6cBl2VnExQYIJ8851Wo0zXFEwtTHj2Y0YNKOJGpVm2X0S93bN1LCf6p")         # 需要在onepai平台中 添加渠道生成令牌

response = client.chat.completions.create(
    model="doubao-pro-128k",
    
    messages=[{"role": "user", "content": "https://www.douyin.com/video/7447493344692948278"}],    
    stream=True,
)

data = ''

# 流式输出的方式
for chunk in response:
    if chunk.choices[0].delta.content is not None:
        # print(chunk.choices[0].delta.content, end="")
        data += chunk.choices[0].delta.content

print(data)


# 非流式输出的方式
# raw_jsondata = response.model_dump_json()
# import json
# data =json.loads(raw_jsondata)
# content_str = data['choices'][0]['message']['content']

# 去除转义字符
# content_str = content_str.replace('\\', '')

# 解析为JSON
# parsed_json = json.loads(content_str)

# 打印结果
# print(content_str)

# print(data)

