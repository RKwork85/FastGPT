import json
import pandas as pd

def data_json(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        data_json = json.loads(f.read())
        return data_json
    


def xlsx_to_json(file_path):
    df = pd.read_excel(file_path)

    json_dataStr = df.to_json(orient='records', force_ascii=False, indent=4)
    json_data = json.loads(json_dataStr)
    for index, value in enumerate(json_data, start=1):
        value["ID"] = str(index)

    return json_data