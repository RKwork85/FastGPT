import os
import json
import csv
import re
import shutil


current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)

# 文件复制重命名
source_file  = 'daiding.txt'
rename_file = 'XiaWeiID4'
numbers = re.findall(r'\d+', rename_file)
# 将提取的数字列表转换为字符串
number = ''.join(numbers)
shutil.copy(source_file, rename_file)



file_dir = "XiaWei_ID_" + number
file_json = file_dir + '.json'
file_name_list = file_dir + ".txt"
file_csv = file_dir + '.csv'


# 写json
json_file = []
with open(source_file, 'r') as f:
    for index, data in enumerate(f, start=1):
        clean_data = data.strip()
        data = {
        "Xiawei_ID": number,
        "Domain":"QingGan",
        "Name": f"ID_{number}_Number_{index}",
        "Data": f"{clean_data}"
    }
        json_file.append(data)

with open(file_json, 'w', encoding='utf-8') as f:
    json.dump(json_file, f, ensure_ascii=False,  indent=4)
    f.flush()




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


