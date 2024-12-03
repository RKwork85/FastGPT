import time
import json
from openai import OpenAI
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

data_list = []

for i in range(1,4):
    number = i
    with open(f'duihua{number}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            if i['role']=='assistant':
                data_list.append(i['content'])


    with open(f'finial{number}', 'w', encoding='utf-8') as f:
        for i in data_list:
            f.write(i +'\n')
    
    data_list = []