# import csv

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

import os
import csv
import json

current_file = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_file)



# 定义CSV文件路径和JSON文件路径
csv_file_path = 'names.csv'
json_file_path = 'output.json'

# 读取CSV文件并转换为JSON
def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # 读取所有行并存储为字典列表
        data = [row for row in csv_reader]
        
        # 写入JSON文件
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

# 调用函数
csv_to_json(csv_file_path, json_file_path)