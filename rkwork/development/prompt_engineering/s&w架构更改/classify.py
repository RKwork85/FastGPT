import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 定义文件路径
input_file_path = "/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/s&w架构更改/data_result.json"

# 定义输出文件名
output_files = {
    "功能视频": "functional_videos.json",
    "场景视频": "scene_videos.json",
    "穿搭视频": "fashion_videos.json",
    "痛点视频": "pain_point_videos.json"
}

# 初始化分类存储的字典
classified_data = {category: [] for category in output_files.keys()}

# 读取原始JSON文件
try:
    with open(input_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("文件未找到，请检查路径是否正确。")
    exit()
except json.JSONDecodeError:
    print("文件格式错误，无法解析JSON。")
    exit()

# 按类别分类数据
for item in data:
    video_form = item.get("视频形式")
    if video_form in classified_data:
        classified_data[video_form].append(item)
    else:
        print(f"未识别的视频形式：{video_form}")

# 将分类后的数据写入新的JSON文件
for category, file_name in output_files.items():
    with open(file_name, "w", encoding="utf-8") as output_file:
        json.dump(classified_data[category], output_file, ensure_ascii=False, indent=4)
    print(f"已将{category}数据写入文件：{file_name}")