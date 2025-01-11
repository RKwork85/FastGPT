import os
import json

# url_list =[]

# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# with open('服装行业访谈型对标表测试.json','r', encoding='utf-8') as f:
#     data = json.loads(f.read())
#     for i in data:      
#         url_list.append(i['视频链接'])


# result_list = []

# with open('url.txt', 'w', encoding='utf-8') as f:
#     for url in url_list:
#         f.write(url + '\n') 

url_list =[]
count = 0
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('服装行业访谈型金句提取.json','r', encoding='utf-8') as f:
    data = json.loads(f.read())
    for i in data:      
        count += len(i['访谈类文案金句提取助手']) # 303
        for k in i['访谈类文案金句提取助手'].values():
            url_list.append(k)



# print(len(url_list))
# for i in url_list:
#     print(i)
# print(count)
# result_list = []

with open('访谈型金句.txt', 'w', encoding='utf-8') as f:
    for url in url_list:
        f.write(url + '\n') 



        