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

    question = questionJson['模版文案']
    
    client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="prechengwenai-g9o92e1gOvHcd5YDfS0X0qnHKqazGHgM9l2T9uR8mPo8DIBvSYv2uLfScxeczo")
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
  
    data_json = {"品牌":"S&W文案架构", "文案内容": question, "视频形式": data_chunk, "话题分类":questionJson["子分类"]}

    return data_json
  
# 提供的文本
if __name__ == '__main__':
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/s&w架构更改/data.json','r', encoding='utf-8') as f:
        tasks = json.load(f)

    result_list = []

    samples = tasks[:2]
    start = time.time()
    
    with multiprocessing.Pool(processes=50) as pool:
        results = pool.map_async(chat_request, tasks)
        
        for index, result in enumerate(results.get()):
            result_list.append(result)


    end = time.time()
    print(f"最终执行时间{end - start}")
    with open('/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/s&w架构更改/data_result.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False, indent=4)




# #  两个re 没有得到json格式
# #  一个没有字段内容
# #  还有视频链接不存在
# # 补丁：不清楚是哪些数据，需要校对url链接

