import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open ('服装行业访谈型对标表测试.json', 'r', encoding='utf-8') as f:
    data = f.read()
    json_data = json.loads(data)
    for index, single_data in enumerate(json_data):
        single_data['视频ID'] = f'FZDB-1-Tinterview-N{index + 1}'
    
    with open('服装行业访谈型对标表.json','w', encoding='utf-8') as f:
        json.dump(json_data,f, ensure_ascii=False, indent=4)
