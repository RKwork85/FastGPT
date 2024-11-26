import os
import json


current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
print(os.getcwd())
with open("XiaWei_ID_9.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open('XiaWei_ID_9.txt', 'w', encoding='utf-8') as f:
    Name_list = [i['Name'] for i in data]
    f.write(str(Name_list))        