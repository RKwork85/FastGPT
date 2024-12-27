import multiprocessing
import os
import json 
import time
from openai import OpenAI
import re
question_data= "https://www.douyin.com/video/7447493344692948278"


def chat_request(question):

    client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="prechengwenai-ii6cBl2VnExQYIJ8851Wo0zXFEwtTHj2Y0YNKOJGpVm2X0S93bN1LCf6p")
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

    json_pattern = r'\{.*?\}'
    json_match = re.search(json_pattern, data_chunk, re.DOTALL)
    if json_match:
            json_data_str = json_match.group(0)
    try:
        # 将提取的JSON字符串解析为Python字典
        extracted_json = json.loads(json_data_str)  # 还是这个字符串 匹配出来的不一定是字符串有问题     
        return extracted_json
    except Exception as e:
        print(f"解析JSON时出错：{e}")
        return None

# 提供的文本
if __name__ == '__main__':
    
    url_list =[]

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('访谈型url链接2','r', encoding='utf-8') as f:
        for i in f:      
            url_list.append(i.strip())

    result_list = []

    start = time.time()
    

    # tasks = [(question_data) for _ in range(2)]
    tasks = url_list

    
    with multiprocessing.Pool(processes=20) as pool:
        results = pool.map_async(chat_request, tasks)

        for index, result in enumerate(results.get()):
            try:
                data_result = {
                    "对标IP":"子期在路上✨",
                    "文案类型": "一、访谈型",
                    "视频ID": f"{index + 1}",
                    "视频链接": f"{result['URL']}",
                    "文案标题": f"{result['TITLE']}",       # 可能会没有某个字段 一个有问题
                    "视频文案": f"{result['COPYWRITER']}"
                }
                # print(data_result)
            except Exception as e:  
                continue
                
            result_list.append(data_result)
            # print(result)

    end = time.time()
    print(f"最终执行时间{end - start}")
    with open('服装行业访谈型对标表测试2.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False, indent=4)




#  两个re 没有得到json格式
#  一个没有字段内容
#  还有视频链接不存在
# 补丁：不清楚是哪些数据，需要校对url链接

