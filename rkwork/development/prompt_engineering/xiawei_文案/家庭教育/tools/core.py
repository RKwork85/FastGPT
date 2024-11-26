import os
import json
import csv


current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)
file_dir = "XiaWei_ID_16"
file_json = file_dir + '.json'
file_name_list = file_dir + ".txt"
file_csv = file_dir + '.csv'


# 写json
# json_file = []
# with open("123.txt", 'r') as f:
#     for index, data in enumerate(f, start=1):
#         clean_data = data.strip()
#         data = {
#         "Xiawei_ID": 9,
#         "Name": f"ID_9_Number_{index}",
#         "Data": f"{clean_data}"
#     }
#         json_file.append(data)

# with open(file_json, 'w', encoding='utf-8') as f:
#     json.dump(json_file, f, ensure_ascii=False,  indent=4)
#     f.flush()




# 写name

with open(file_json, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(file_name_list, 'w', encoding='utf-8') as f:
    Name_list = [i['Name'] for i in data]
    f.write(str(Name_list))        
    f.flush()

# 写csv

with open(file_json, 'r') as f:
    data = json.load(f)

with open(file_csv, 'w', newline='') as csvfile:
    # 创建一个csv字典写入器
    fieldnames = data[0].keys()  # 从第一个对象中获取字段名
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入表头
    writer.writeheader()

    # 写入数据
    for row in data:
        writer.writerow(row)
print("JSON数据已成功转换为CSV文件。")


