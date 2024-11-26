import json
import csv

# 假设你的JSON数据是这样的字符串
with open("result_file", 'r') as f:
    data = json.load(f)

# 将JSON字符串解析为Python对象

# 打开一个新的CSV文件用于写入
with open('output.csv', 'w', newline='') as csvfile:
    # 创建一个csv字典写入器
    fieldnames = data[0].keys()  # 从第一个对象中获取字段名
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入表头
    writer.writeheader()

    # 写入数据
    for row in data:
        writer.writerow(row)

print("JSON数据已成功转换为CSV文件。")