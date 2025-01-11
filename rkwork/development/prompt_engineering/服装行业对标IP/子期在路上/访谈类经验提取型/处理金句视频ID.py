import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))


dataID = []

with open ('服装行业访谈型对标表.json', 'r', encoding='utf-8') as f:
    data = f.read()
    json_data = json.loads(data)
    for index, single_data in enumerate(json_data):
        dataID.append(single_data['视频ID'])
       
    
    with open('服装行业访谈型金句提取.json','r', encoding='utf-8') as f:
            data = f.read()
            json_data = json.loads(data)
            for index, i in enumerate(json_data):
                 i.pop('视频文案')
                 i['视频ID'] = dataID[index]

            with open('服装行业访谈型金句提取new.json', 'w', encoding='utf-8') as f:
                 json.dump(json_data,f, ensure_ascii=False, indent=4)