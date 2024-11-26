import os 

import json

current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)

json_file = []
with open("123.txt", 'r') as f:
    for index, data in enumerate(f, start=1):
        clean_data = data.strip()
        data =     {
        "Xiawei_ID": 9,
        "Name": f"ID_9_Number_{index}",
        "Data": f"{clean_data}"
    }
        json_file.append(data)

with open("XiaWei_ID_6.json", 'w', encoding='utf-8') as f:
    json.dump(json_file, f, ensure_ascii=False,  indent=4)