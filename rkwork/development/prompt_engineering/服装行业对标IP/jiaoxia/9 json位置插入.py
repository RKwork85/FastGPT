import json

# 原始的JSON数据
original_json = {"aaa": "123", "bbb": "222", "ccc": "333"}

# 新的JSON数据
new_json = {"zzz": "000"}
new_items = list(new_json.items())
print(new_items)

# 将原始JSON转换为列表
items = list(original_json.items())
print(items)

# 找到插入位置

# 插入新的键值对
items.insert(1, new_items[0])

# 将列表转换回字典
updated_json = dict(items)
print(updated_json)
# hhh = json.dumps(updated_json, indent=4)
# print(hhh,type(hhh))