import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
from volcenginesdkarkruntime import Ark




def get_video_information(content):
    client = Ark(api_key="e5838444-66ee-4c37-bddc-53c46bbd700f")

    print("----- streaming request -----")
    stream = client.bot_chat.completions.create(
        model="bot-20241212185120-qqnnf",
        messages=[
            {"role": "user",
             "content": content}
        ],
        stream_options={
            'include_usage': True
        },
        stream=True
    )

    for chunk in stream:
        if chunk.bot_usage != None:
            data = chunk.bot_usage.action_details[0]
            # 提取状态码
            status_code = data['tool_details'][0]['output']['data']['status_code']
            # 提取第一个 ark_web_data_list 中的内容
            content = data['tool_details'][0]['output']['data']['data']['ark_web_data_list'][0]['content']
            print(content)
            return content


data=pd.read_excel("七叔女装供应链.xlsx")
data=data.head(100)

def process_video_row(row):
    print(row['Awesome ID'])
    # 处理每一行，返回分析结果
    return get_video_information(row['URL'])

# 使用线程池执行器进行多线程处理
with ThreadPoolExecutor(max_workers=4) as executor:  # 设置你希望的最大线程数
    # 提交所有的任务给线程池
    future_to_index = {executor.submit(process_video_row, row): index for index, row in data.iterrows()}

    # 等待所有的任务完成
    for future in as_completed(future_to_index):
        index = future_to_index[future]
        try:
            # 获取任务的结果
            result = future.result()
            print(result)
            # 在主线程中更新 DataFrame
            data.at[index, '豆包搜索'] = result
        except Exception as exc:
            print(f"视频 {data.at[index, '文件名称']} 处理时出错: {exc}")

data.to_excel('data/七叔女装供应链结果.xlsx')