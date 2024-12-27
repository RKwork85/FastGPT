import os
import json

url_list =[]

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('服装行业访谈型金句提取.json','r', encoding='utf-8') as f:
    data = json.loads(f.read())
    for i in data: 
        i.pop('脚本内容')   
        url_list.append(i) 




with open('服装行业访谈型金句提取new.json', 'w', encoding='utf-8') as f:
    json.dump(url_list,f, ensure_ascii=False, indent=4)




        