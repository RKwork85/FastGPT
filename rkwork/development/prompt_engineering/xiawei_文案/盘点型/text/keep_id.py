import json
import os

current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)

with open('XiaWei_ID_3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(len(data))

data_list = []
with open("result.json", 'w', encoding='utf-8') as f:
    for index, dt in enumerate(data):
        dt["Name"] = f"ID_3_Number_{index + 1}"
        data_list.append(dt)
    
    json.dump(data_list, f, ensure_ascii=False, indent=4 )