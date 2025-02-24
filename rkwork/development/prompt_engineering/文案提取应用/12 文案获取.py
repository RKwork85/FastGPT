import multiprocessing
import os
import json 
import time
from openai import OpenAI
import re
question_data= "https://www.douyin.com/video/7447493344692948278"


def indexInsert(rawdata, newdata):
    rawdata_list = list(rawdata.items())
    newdata_list = list(newdata.items())
    rawdata_list.insert(4, newdata_list[0])
    result = dict(rawdata_list)
    return result


def chat_request(questionJson):

    question = questionJson['aweme_url']
    
    client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="prechengwenai-bdcnlemah5fm6Vsd0qKM2aMogazkZISj30sN0ruo37b14kmabGzWY7rAj7eop6of")
    response = client.chat.completions.create(
        model="doubao-pro-128k",                                            
        messages=[
            {'role': 'user', 'content': f'{question}'}],
        stream= True
        )
    data_chunk = ''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:

            data_chunk += chunk.choices[0].delta.content
    json_pattern = r'\{.*?\}'
    json_match = re.search(json_pattern, data_chunk, re.DOTALL)
    if json_match:
            json_data_str = json_match.group(0)
    try:
        extracted_json = json.loads(json_data_str) 
        aim_json = {"文案內容":extracted_json['COPYWRITER']}

        result = indexInsert(questionJson, aim_json)

        return result
    except Exception as e:
        print(f"解析JSON时出错：{e}")

# 提供的文本
if __name__ == '__main__':
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/文案提取应用/内衣_search_filtered.json','r', encoding='utf-8') as f:
        tasks = json.load(f)

    result_list = []

    samples = tasks[:]
    # print(type(tasks))
    start = time.time()
    

    with multiprocessing.Pool(processes=20) as pool:
        results = pool.map_async(chat_request, samples)
        
        for index, result in enumerate(results.get()):
            if result is None:
                print(f'第 {index} 个任务返回了 None，跳过处理')
                continue  
            if isinstance(result, dict):
                result_list.append(result)
                print(f'第 {index} 个任务已完成')
            else:
                print(f'第 {index} 个任务返回了非字典类型的结果：{type(result)}，跳过处理')
    end = time.time()
    print(f"最终执行时间{end - start}")
    with open('/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/文案提取应用/内衣_search_solved.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False, indent=4)




# #  两个re 没有得到json格式
# #  一个没有字段内容
# #  还有视频链接不存在
# # 补丁：不清楚是哪些数据，需要校对url链接

