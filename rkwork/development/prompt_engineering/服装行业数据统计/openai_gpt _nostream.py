from openai import OpenAI    

client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="prechengwenai-mtpxUVV9XVh78goVAI1ZgtAv4iOhwyNHPBDGSHj7DX8kXvelk1Xu")         # 需要在onepai平台中 添加渠道生成令牌

response = client.chat.completions.create(
    model="doubao-pro-128k",
    
    messages=[{"role": "user", "content": "https://www.douyin.com/video/7447493344692948278"}],    
    stream=False,
)

# 非流式输出的方式
raw_jsondata = response.model_dump_json()
import json
data =json.loads(raw_jsondata)
print(data)

content_str = data['choices'][0]['message']['content']
print(content_str, type(content_str))
content_json =json.loads(content_str)