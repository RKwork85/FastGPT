import pandas as pd
import glob

# 使用 glob 模块获取所有 JSON 文件
file_pattern = '*.json'  # 根据需要调整文件模式
json_files = glob.glob(file_pattern)

# 创建一个空的 DataFrame
merged_df = pd.DataFrame()

# 遍历每个 JSON 文件并合并
for file in json_files:
    df = pd.read_json(file)
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# 根据视频 ID 合并数据
final_df = merged_df.groupby('视频ID').agg({
    '访谈型文案思路提取助手': 'first',
    '访谈型文案观点参考提取助手': 'first'
}).reset_index()

# 输出合并后的结果
final_df.to_json('merged_data.json', orient='records', force_ascii=False, indent=4)

print("数据合并完成，结果已保存到 merged_data.json")