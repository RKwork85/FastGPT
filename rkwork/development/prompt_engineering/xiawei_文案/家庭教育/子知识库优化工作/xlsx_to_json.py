import json
import pandas as pd
import os 


current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)


# 读取Excel文件
def xlsx_to_json(xlsx_file_path, json_file_path):
    # 使用pandas读取Excel文件
    df = pd.read_excel(xlsx_file_path)
    
    # 将DataFrame转换为JSON格式
    json_data = df.to_json(orient='records', force_ascii=False)
    json_file = json.loads(json_data) 
    # 将JSON数据写入文件
    print(type(json_file))
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(json_file, f, indent=4, ensure_ascii=False)
   
# 调用函数
xlsx_file_path = 'XiaWei_ID_'  # 替换为你的Excel文件路径
json_file_path = 'XiaWei_ID_'  # 输出的JSON文件路径
for i in range(11, 14):
    temp_path = xlsx_file_path + str(i) + '.xlsx'
    output_path = json_file_path + str(i) + '.json'
    xlsx_to_json(temp_path, output_path)



# pip install pandas openpyxl