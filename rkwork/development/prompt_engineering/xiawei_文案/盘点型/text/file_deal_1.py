import os 

import json

current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)

json_file = []
with open("123.txt", 'r') as f:
    for index, data in enumerate(f, start=1):
        data =     {
        "Xiawei_ID": 6,
        "Name": f"ID_6_Number_{index}",
        "Data": f"{data}"
    }
        json_file.append(data)

with open("XiaWei_ID_6.json", 'w', encoding='utf-8') as f:
    json.dump(json_file, f, ensure_ascii=False,  indent=4)