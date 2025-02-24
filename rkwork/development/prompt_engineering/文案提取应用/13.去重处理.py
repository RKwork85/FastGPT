import json
import os

# 步骤 1: 读取 JSON 文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/文案提取应用/运动内衣_search.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 步骤 2: 初始化一个集合用于记录唯一的字段值
unique_ids = set()

# 步骤 3: 过滤重复项
filtered_data = []
number = 0
for item in data:
    if item['aweme_url'] not in unique_ids:
        filtered_data.append(item)
        unique_ids.add(item['aweme_url'])
    else:
        print(item['aweme_url'], "重复")
        number +=1 

print(number)

# 步骤 4: 写回 JSON 文件（如果需要）
with open('/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/文案提取应用/运动内衣_search_filtered.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=4)

print("去重完成，结果已保存到 filtered_data.json")