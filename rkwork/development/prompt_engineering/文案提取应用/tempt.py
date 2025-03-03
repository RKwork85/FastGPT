import json
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)


with open("result2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for index , value in enumerate(data, start=30):
    value["ID"] = index



with open("reuslt3.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii= False, indent=4)


