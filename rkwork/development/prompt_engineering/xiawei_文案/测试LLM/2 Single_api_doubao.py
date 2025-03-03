# # 方式一：http 可实现
# import requests
# import json
 
 
# def ask_doubao(api_key, msg_list):

#     url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
#     headers = {
#         "Authorization": "Bearer " + api_key,
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "ep-20241107113951-4rvzr",  # 模型端点ID，在线推理申请
#         "messages": msg_list,
#     }

#     response = requests.post(url, headers=headers, json=data)
#     return response
 
 
# if __name__ == '__main__':

#     api_key = "6fac9cce-8ed5-4c98-bf49-37e7787b0112"            # API管理
#     msg_list = [
#         {
#             "role": "system",
#             "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"
#         }, 
#         {
#             "role": "user",
#             "content": "常见的十字花科植物有哪些"
#         }
#     ]
#     resource = ask_doubao(api_key, msg_list)
#     print(resource.json())



# result
# {'choices': [{'finish_reason': 'stop', 'index': 0, 'logprobs': None, 'message': {'content': '以下是一些常见的十字花科植物：\n\n### 一、蔬菜类\n1. **白菜**\n   - 包括大白菜（Brassica rapa pekinensis）和小白菜（Brassica rapa chinensis）等。大白菜是我国北方冬季常见的蔬菜，叶片宽大，层层包裹，呈球状体；小白菜植株相对较小，叶片较嫩，口感鲜美，富含维生素、矿物质和膳食纤维等营养成分。\n2. **甘蓝**\n   - 例如结球甘蓝（Brassica oleracea var. capitata），也就是我们常说的卷心菜、包菜。其叶片厚实，层层紧抱成球形，有绿、紫等颜色。还有花椰菜（Brassica oleracea var. botrytis），白色的花序可食用，富含维生素C、类胡萝卜素等营养物质；西兰花（Brassica oleracea var. italica），绿色的花球，营养丰富，被认为是一种高营养的蔬菜。\n3. **萝卜**\n   - 如白萝卜（Raphanus sativus var. longipinnatus）、红萝卜（Raphanus sativus var. radculus）等。萝卜肉质根为主要食用部分，形状有长圆形、圆形等，可生食、熟食或腌制，具有消食、下气等功效。\n4. **芥菜**\n   - 芥菜（Brassica juncea）种类较多，雪里蕻（Brassica juncea var. multiceps）是芥菜的一种变种，其茎和叶可用于腌制咸菜；大头菜（Brassica juncea var. megarrhiza）肉质根肥大，可腌制或炒食。\n\n### 二、观赏植物类\n1. **紫罗兰**\n   - 紫罗兰（Matthiola incana），花朵色彩丰富，有紫色、白色、粉色等，花瓣呈十字形排列，花朵香气淡雅，常被用于庭院种植或切花观赏。\n2. **二月兰**\n   - 二月兰（Orychophragmus violaceus），也叫诸葛菜。它是一种常见的野花，在春季开花，花朵为淡紫色，大片生长时形成美丽的紫色花海，常生长在路边、林下等地。', 'role': 'assistant'}}], 'created': 1730950961, 'id': '021730950934997fb7dc9cfb61c996573e2f6246c1be98ae72481', 'model': 'doubao-pro-32k-240828', 'object': 'chat.completion', 'usage': {'completion_tokens': 483, 'prompt_tokens': 35, 'total_tokens': 518}}


## 第二种：openai方式调用

import os
import json 
import time
from openai import OpenAI

question_data = ['讲一个故事吧']

# api_key = sk-be8fb3e390b84edba24374f7205a25c6
# export ARK_API_KEY="e963ee3a-0366-47e7-a928-d269b55cad2c"


os.environ['ARK_API_KEY'] ="e963ee3a-0366-47e7-a928-d269b55cad2c"       ## 2 在模型API中生成密钥

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("ARK_API_KEY"), 
    base_url="https://ark.cn-beijing.volces.com/api/v3",            ## 1 地址要对
)

def chat_request(client, question):

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
chat_request(client=client, question=question_data)
end = time.time()
print(f"最终执行时间{end - start}")

