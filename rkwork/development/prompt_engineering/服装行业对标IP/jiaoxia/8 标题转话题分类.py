import multiprocessing
import os
import json 
import time
from openai import OpenAI



def indexInsert(rawdata, newdata):
    rawdata_list = list(rawdata.items())
    newdata_list = list(newdata.items())
    rawdata_list.insert(12, newdata_list[0])
    result = dict(rawdata_list)
    return result

def chat_request(questionJson):
    client = OpenAI(
       base_url="http://aiagent-pre.chengwen.net/api/v1",  
       api_key="prechengwenai-h7mFxCvAHb5nKAjfKVGV49mxLI0joTNjeXyKp4F7XoU1P8IcB8cG9E7AjV"
    )
    question = questionJson['标题']
    
    completion = client.chat.completions.create(
        model="doubao-pro-128k",
        messages=[{'role': 'user', 'content': f'{question}'}],
    )
    completion_cp = completion.model_dump_json()
    data = json.loads(completion_cp)
    content = (data["choices"][0]['message']['content']).strip()
    try:    
        result_json = json.loads(content)
        result = indexInsert(questionJson, result_json)
        print('第', result['ID'],'正常处理！')
        return result
    except Exception as e:
        print(questionJson['ID'],"返回数据格式，出错！返回的数据为：",content,'\n','报错信息为：', e)


if __name__ =='__main__':
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    start = time.time()
    
    with open('raw.json', 'r', encoding='utf-8') as f:
        dataStr = f.read()
        dataList = json.loads(dataStr)
        for index, item in enumerate(dataList,start=1):
            item['ID'] = index
            
    task = dataList
    samples =task[:10]

    file_list = []

    with multiprocessing.Pool(processes=20) as pool:
        results = pool.map_async(chat_request, task)
        for index,result in enumerate(results.get()):
            file_list.append(result)
    end = time.time()

    print(f"最终执行时间{end - start}")

    with open('蕉下官方旗舰店数据整理_solved2.json', 'w', encoding='utf-8') as f:
        json.dump(file_list, f, ensure_ascii=False, indent=4)


# 285 返回数据格式，出错！返回的数据为：  
#  报错信息为： Expecting value: line 1 column 1 (char 0)
# 第 289 正常处理！
# 286 返回数据格式，出错！返回的数据为：  
#  报错信息为： Expecting value: line 1 column 1 (char 0)
# 287 返回数据格式，出错！返回的数据为：  
#  报错信息为： Expecting value: line 1 column 1 (char 0)