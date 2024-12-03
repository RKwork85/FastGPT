
# 使用示例
import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
input_file_path = 'XiaWeiID_2'  # 替换为你的文件路径

# 以任意字符到场景二结束
pattern1 = r'^(.+?)(?=场景二：)'


pattern2 = r'^(.+?)(?=场景三：)'
pattern3 = r'(场景二：.+?)(?=$)'

# 以场景三起始到末尾
pattern4 = r'(场景三：.+?)(?=$)'


file_case = []
file_case2 = []

with open(input_file_path, 'r', encoding='utf-8') as f:

    for name in range(1, 4):
        match name:
            # case 1 :    
            #     for i in f:
            #         match = re.search(pattern1, i, re.DOTALL)
            #         if match:
            #             file_case.append(match.group(1))

            #     with open(f'case{name}.txt', 'w',encoding='utf-8') as file:
            #         for i in file_case:
            #             file.write(i + '\n')

            #     file_case = []
            #         match = re.search(pattern2, i, re.DOTALL)
            #         if match:
            #             print(match.group(1))



            #         match = re.search(pattern3, i, re.DOTALL)
            #         if match:
            #             print(match.group(1))
            case 2:
                for i in f:
                    match = re.search(pattern2, i, re.DOTALL)
                    if match:
                        file_case.append(match.group(1))

                for i in file_case:
                    match = re.search(pattern3, i, re.DOTALL)
                    if match:
                        file_case2.append(match.group(1))

                with open(f'case{name}.txt', 'w',encoding='utf-8') as file:
                    for i in file_case2:
                        file.write(i + '\n')                
                file_case = []



            # case 3:
            #     for i in f:
            #         match = re.search(pattern4, i, re.DOTALL)
            #         if match:
            #             file_case.append(match.group(1))

            #     with open(f'case{name}.txt', 'w',encoding='utf-8') as file:
            #         for i in file_case:
            #             file.write(i + '\n')

            #     file_case = []