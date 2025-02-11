import os
import re
import json 
import time
import random
import multiprocessing
from openai import OpenAI
from config import pre_config

from sw_package.file_read import data_json, xlsx_to_json
from sw_package.get_todayTime import todayTime

def chat_request(question_json):
    question = question_json["文案内容"]
    client = OpenAI(
       base_url="http://aiagent-pre.chengwen.net/api/v1",  
       api_key="prechengwenai-qYpABXW0b9AkL3ov3eQa5i99SpGwPfXIFtwuhnhVIo9AKKSPFnILwXqG3wJyj1"
    )
    
    completion = client.chat.completions.create(
        model="doubao-pro-128k",
        messages=[{'role': 'user', 'content': f'{question}'}],
    )
    completion_cp = completion.model_dump_json()
    data = json.loads(completion_cp)
    content = (data["choices"][0]['message']['content'])
    tempt_data = pre_config.data
    tempt_data["视频编号"] = todayTime() +"-" + question_json["ID"]
    tempt_data["回溯信息"] = pre_config.shooting_schedule + "-" + question_json["模板编号"] + "-" + random_choice(pre_config.video_template) + "-"+ todayTime() +"-" + question_json["ID"]
    tempt_data["视频名称"] = question_json["模板编号"] + "-" + random_choice(pre_config.video_template) + "-"+ todayTime() +"-" + question_json["ID"]
    tempt_data["视频字幕"], tempt_data["切割数组"] = process_cc_length(question_json["文案内容"])
    concat = content_solved(content)
    tempt_data["混剪素材"] = concat
    tempt_data["背景音乐"] = pre_config.bgm_path + "\\" + random_choice(pre_config.bgm_option)
    tempt_data["配音文案"] = question_json["文案内容"]
    tempt_data["AI配音"] = random_choice(pre_config.dubbing_ai)
    print("最终返回：", tempt_data)
    return tempt_data

    
    # 会有死锁问题
    # pre_config.data["混剪素材"] = content_solved(content)
    
    return 

def task_running(task):
    file_list = []
    with multiprocessing.Pool(processes=100) as pool:
        results = pool.map_async(chat_request, task)
        for index,result in enumerate(results.get()):
            file_list.append(result)

    return file_list



def content_solved(content):
    lines = content.strip().split("\n")
    result = [line.split("|", 1)[1].strip() for line in lines]
    video_materials_data = data_json("folder_files_dict.json")
    final_match = []
    for i in result:
        vdieo_materials_match = random_choice(video_materials_data[i])
        cat_data = pre_config.root + "/" +  pre_config.shooting_schedule +  "/" + i + "/" + vdieo_materials_match 
        final_match.append(cat_data)
    final_match_str = "\n".join(final_match)

    # 需要将所有的斜杠改为反斜杠
    final_match_str_solved = final_match_str.replace("/", "\\")

    return final_match_str_solved


def random_choice(lst):
    if not lst:  
        return ""
    return random.choice(lst)

def process_cc_length(text):
    # 存储每条数据长度处理结果的数组
    data_list = [item.strip() for item in re.split(r'[，。！？；：“”‘’\.,!?;:"\']+', text) if item.strip()]
    length_results = []
    # 存储处理后的新字符串数组
    new_strings = []

    for data in data_list:
        # 计算字符长度处理结果
        length_result = (len(data) // 10) + 1
        length_results.append(str(length_result))

        # 根据字符长度进行不同处理
        if len(data) <= 10:
            # 字符长度小于等于10，不做处理
            new_strings.append(data)
        elif 10 < len(data) < 15:
            # 字符长度大于10且小于15，截断为两个字符串
            split_index = (len(data) // 2) + 2
            new_strings.append(data[:split_index])
            new_strings.append(data[split_index:])
        elif 15 <= len(data) < 20:
            # 字符长度大于等于15且小于20，截断为两个字符串
            split_index = (len(data) // 2)  +1
            new_strings.append(data[:split_index])
            new_strings.append(data[split_index:])
        else:
            # 字符长度大于等于20，始终保持截断后的每个子串最小长度为4
            split_index = 7
            while len(data) > 0:
                new_strings.append(data[:split_index])
                data = data[split_index:]

        split_resultStr = "\n".join(new_strings)
        split_resultList = "\n".join(length_results)

    return split_resultStr, split_resultList


if __name__ =='__main__':

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    input_data = xlsx_to_json('inputData.xlsx')

    
    file_list = []
    samples =input_data[:20]
    start = time.time()

    result_file = task_running(input_data)
    end = time.time()
    print(f"最终执行时间{end - start}")
    
    with open("final_result2.json", "w", encoding="utf-8") as f:
        json.dump(result_file, f, indent=4, ensure_ascii=False)




