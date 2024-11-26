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
    
    # 将JSON数据写入文件
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

# 调用函数
xlsx_file_path = 'your_excel_file.xlsx'  # 替换为你的Excel文件路径
json_file_path = 'output.json'  # 输出的JSON文件路径
xlsx_to_json(xlsx_file_path, json_file_path)