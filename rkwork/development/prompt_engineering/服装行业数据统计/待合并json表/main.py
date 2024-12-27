import os
import json
import pandas as pd

# 获取当前目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_list = [f for f in os.listdir() if f.endswith('json')]

print(file_list)
resultList = []
primary_key = '视频ID'

# for i in file_list:
with open(file_list[0], 'r', encoding='utf-8') as f:
    data_json = f.read()
    data1 = json.loads(data_json)

    with open(file_list[1], 'r', encoding='utf-8') as f:
        data_json = f.read()
        data2 = json.loads(data_json)

        for item1, item2 in zip(data1, data2):
            print(item1['视频ID'], item2['视频ID'])