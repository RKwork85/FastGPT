import re
import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

task =[]
# 构造输入数据
with open('AICleared_data.json','r', encoding='utf-8') as f:
    data = json.loads(f.read())
    for index, i in enumerate(data):
        text = data[index]['AI清理']
        data[index]['AI清理'] = re.sub(r'（.*?）', '', text)



with open('AICleared_data_v2.json', 'a+', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



# print(cleaned_text)