




import multiprocessing
import os
import json 
import re
import time
from openai import OpenAI

question_data= "https://www.douyin.com/video/7317848191443995931"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def chat_request(question):
    # 在函数内部创建client实例
    client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="prechengwenai-rwcUdjvhFxYyxtUrI5CtYxouAj82stiiua3Sw8ueRO2L5J3xX0ZXm3rZ")
    response = client.chat.completions.create(
        model="doubao-pro-128k",                                            
        messages=[
            # {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': f'{question}'}],
        stream= True
        )
    data_chunk = ''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            # print(chunk.choices[0].delta.content, end="")
            data_chunk += chunk.choices[0].delta.content

    # print("data_chunk 内容：",data_chunk)
    json_pattern = r'\{.*?\}'
    json_match = re.search(json_pattern, data_chunk, re.DOTALL)
    if json_match:
        json_data_str = json_match.group(0)
        print(json_data_str, type(json_data_str))
        try :
            content = json_data_str.strip()
            clear_data = content.replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')
            data = json.loads(clear_data)
            return data
        
        #     json_data_str = json_match.group(0)
        # data = json.loads(completion_cp)
        # content = (data["choices"][0]['message']['content'])
        # content = content.strip()
        # print("返回内容：",repr(content))
        # clear_data = content.replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')
        # print("清理后的内容：", clear_data)

        # content = str(content)
        # try:
        #     json_data = json.loads(clear_data)
        #     print("解析成功！", json_data["paragraph"])
        #     return json_data  # 返回包含结果的列表
        except Exception as e:
            print(e)




start = time.time()
result_list = []
# 创建一个进程池，池中进程数量为2
task = [question_data for _ in range(1) ]

with multiprocessing.Pool(processes=20) as pool:
    # 使用map_async方法将任务列表提交给进程池，并获取AsyncResult对象
    results = pool.map_async(chat_request, [task[0]])
    

    # 获取所有任务结果
    for index,result in enumerate(results.get()):
        print("result返回内容",result, type(result))
        result_list.append(result)
        

end = time.time()
print(f"最终执行时间{end - start}")

with open('服装行业访谈型对标表测试2.json', 'w', encoding='utf-8') as f:
    json.dump(result_list, f, ensure_ascii=False, indent=4)