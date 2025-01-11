import csv
import json

# CSV文件名和JSON文件名
csv_file = 'data.csv'
json_file = 'data.json'

# 读取CSV文件并转换为字典列表
data = []
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

# 写入JSON文件
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"CSV文件 '{csv_file}' 已成功转换为JSON文件 '{json_file}'。")