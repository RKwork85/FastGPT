import pandas as pd
import json

# JSON 文件路径
json_file_path = "/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/文案提取应用/data_result.json"

# 输出的 Excel 文件路径
output_file_path = "/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/文案提取应用/视频模版分类.xlsx"

# 读取 JSON 文件
try:
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    print("JSON 文件读取成功。")
except FileNotFoundError:
    print(f"错误：文件 {json_file_path} 未找到，请检查路径是否正确。")
    exit()
except json.JSONDecodeError:
    print(f"错误：文件 {json_file_path} 不是有效的 JSON 格式。")
    exit()

# 检查 JSON 数据的结构
if isinstance(json_data, list):
    # 如果 JSON 数据是一个列表，直接转换为 DataFrame
    df = pd.DataFrame(json_data)
elif isinstance(json_data, dict):
    # 如果 JSON 数据是一个字典，尝试找到数据部分（例如 "data" 键）
    data_key = "data"  # 假设数据存储在 "data" 键下 
    if data_key in json_data:
        df = pd.DataFrame(json_data[data_key])
    else:
        print(f"错误：JSON 数据中未找到键 '{data_key}'。")
        exit()
else:
    print("错误：JSON 数据格式不支持。")
    exit()

# 将 DataFrame 保存为 .xlsx 文件
try:
    df.to_excel(output_file_path, index=False, engine="openpyxl")
    print(f"JSON 数据已成功保存到 {output_file_path}")
except Exception as e:
    print(f"保存文件时发生错误：{e}")