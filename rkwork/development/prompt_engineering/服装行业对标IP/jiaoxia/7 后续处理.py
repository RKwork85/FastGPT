import re
import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pattern1 = r"安全环境下拍摄请勿模仿"
pattern3 = r"安全通路下拍摄"
pattern4 = r"安全环境拍摄，请勿模仿"
pattern5 = r"专利号"
pattern6 = r"证书号"
pattern2 = r"文案内容：(.*)"


data = []
result_data = []
with open('蕉下官方旗舰店数据整理_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    temp = data[0]
    # 匹配到则构建到新的列表里面去
    for i in data:
        # 数据标准
        if isinstance(i, dict):
            if i.get("文案内容"):
                # 文案长度标准和错乱标准
                if len(i['文案内容']) < 60 or re.search(pattern1, i['文案内容']) or  re.search(pattern3, i['文案内容']) or re.search(pattern4, i['文案内容']) or re.search(pattern5, i['文案内容']) or re.search(pattern6, i['文案内容']):
                    print('不符合字数的文案ID',i['ID'])
                    
                    pass
                else:
                    # 处理后的文案标准
                    match2 = re.search(pattern2, i['文案内容'])
                    if match2:
                        content = match2.group(1)
                        i['文案内容'] = content  
                        # print('修改后的文案',i['ID'])
                        # print(i)
                        result_data.append(i)
                    else:
                        result_data.append(i)


print('最终清理后的文案数量：',len(result_data))
with open('蕉下官方旗舰店数据整理_solved.json', 'w', encoding='utf-8') as f:
    json.dump(result_data, f, ensure_ascii=False, indent=4)
