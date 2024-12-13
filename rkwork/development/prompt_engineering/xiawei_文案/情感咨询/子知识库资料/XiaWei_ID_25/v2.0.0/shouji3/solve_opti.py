import os
import re

def extract_and_save(pattern, file_name):
    file_case = []
    with open(input_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.search(pattern, line, re.DOTALL)
            if match:
                file_case.append(match.group(1))
    
    with open(f'{file_name}.txt', 'w', encoding='utf-8') as file:
        for content in file_case:
            file.write(content + '\n')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
input_file_path = 'XiaWeiID_3'  # 替换为你的文件路径

patterns = [
    (r'^(.+?)(?=场景二：)', 'case1'),
    (r'^(.+?)(?=场景三：)', 'case2'),
    (r'(场景二：.+?)(?=$)', 'case3'),
    (r'(场景三：.+?)(?=$)', 'case4'),
]

for pattern, file_name in patterns:
    extract_and_save(pattern, file_name)