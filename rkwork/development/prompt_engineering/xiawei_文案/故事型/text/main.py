
import json

file_path = "file_data"
result_file = "result_data"

with open (file_path, mode='r', encoding='utf-8') as f:
    file = json.load(f)

list = []

with open(result_file, mode='w', encoding='utf-8') as f:
    for index, data in enumerate(file):
        body = {
            'Xiawei_ID': 1 ,
            "Name":f'ID_1_Number_{index+1}',
            f"Data":data['extro_info']
        }
        list.append(body)
    
    json.dump(list, f, ensure_ascii=False, indent=4)
