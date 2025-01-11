import json
import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# JSON文件名和CSV文件名
json_file = '蕉下官方旗舰店数据整理_solved.json'
csv_file = '蕉下官方旗舰店数据整理_solved.csv'

# 读取JSON文件
with open(json_file, 'r') as file:
    data = json.load(file)

# 确定CSV文件的列名
fieldnames = data[0].keys()

# 写入CSV文件
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"JSON文件 '{json_file}' 已成功转换为CSV文件 '{csv_file}'。")