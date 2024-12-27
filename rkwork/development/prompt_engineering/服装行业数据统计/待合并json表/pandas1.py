import os
import pandas as pd

# 获取当前目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 遍历当前目录下的所有文件和目录
file_list = [f for f in os.listdir() if f.endswith('json')]

# 确保列表不为空
if file_list:
    # 读取第一个 JSON 文件
    first_file = file_list[0]
    df = pd.read_json(first_file)

    # 打印数据框的前几行
    print("数据框的前几行:")
    print(df.head())

    # 打印数据框的基本信息
    print("\n数据框的基本信息:")
    print(df.info())

    # 假设我们希望进行一些字符串处理（假设列名为 '视频ID'）
    column_name = '视频ID'

    if column_name in df.columns:
        # 1. 筛选包含特定子字符串的行
        substring = "N3"  # 替换为你想要的子字符串
        filtered_df = df[df[column_name].str.contains(substring, na=False)]
        print("\n筛选后的数据框（'{}' 包含 '{}':".format(column_name, substring))
        print(filtered_df)

        # 2. 替换特定子字符串为另一个字符串
        df[column_name] = df[column_name].str.replace("旧字符串", "新字符串", regex=False)
        print("\n替换后的数据框（'{}' 中的 '旧字符串' 被替换为 '新字符串':".format(column_name))
        print(df.head())

        # 3. 添加新列，基于现有列的字符串长度
        df['length_of_column'] = df[column_name].str.len()
        print("\n添加了新列 'length_of_column'，表示 '{}' 字符串的长度:".format(column_name))
        print(df.head())

        # 4. 保存修改后的数据框到新的 JSON 文件
        # df.to_json('modified_data.json', orient='records', lines=True)
    else:
        print("列 '{}' 不存在。".format(column_name))
else:
    print("没有找到 JSON 文件。")