import json
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 输入的JSONL文件名
jsonl_file = 'VFU运动旗舰店_solved.jsonl'
# 输出的JSON文件名
json_file = 'VFU运动旗舰店_solved.json'

# 初始化一个列表来存储所有的JSON对象
data = []

# 读取JSONL文件
with open(jsonl_file, 'r', encoding='utf-8') as infile:
    for line in infile:
        # 将每一行解析为JSON对象并添加到列表中
        data.append(json.loads(line))

# 将列表写入JSON文件
with open(json_file, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print(f"JSONL文件已成功转换为JSON文件：{json_file}")