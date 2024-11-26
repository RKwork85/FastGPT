import itertools
import os
current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)
# 假设您的20条数据存储在一个名为data.txt的文件中，每行一条数据
data_file = 'kkk.txt'
output_file = 'output.txt'

# 读取数据
with open(data_file, 'r') as file:
    lines = file.readlines()

# 确保数据行数为20
assert len(lines) == 20, "数据行数不是20"

# 生成所有可能的3条数据的组合
with open(output_file, 'w') as file:
    for i, combination in enumerate(itertools.combinations(lines, 3), start=1):
        # 将组合写入文件
        file.write(f"组合{i}: {' '.join([line.strip() for line in combination])}\n")