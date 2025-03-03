import requests
import json
import time


# 定义请求的 URL 和数据
url = "http://127.0.0.1:2586/process"  # 修改为你的服务地址
data ={
    "user_questions": [
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在50字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
        {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品","system_prompt":"you are a very helpful assistant!回复在150字左右"},
    ]
}
# data  ="muzihhh"
start = time.time()

# 发送 POST 请求
response = requests.post(url, json=data)

import time
# 检查响应
if response.status_code == 200:
    print("请求成功！")
    print("返回结果：")
    print(json.dumps(response.json(), ensure_ascii=False, indent=4))
else:
    print(f"请求失败，状态码：{response.status_code}")
    print("错误信息：")
    print(response.json())

end = time.time()

print(end - start)


# {
#     "system_prompt":"you are a very helpful assistant!输出在150字左右",
#     "user_questions": [
#         {"question": "如何制作一杯完美的拿铁咖啡？", "lable": "咖啡制作"},
#         {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品"},
#         {"question": "如何制作一杯完美的拿铁咖啡？", "lable": "咖啡制作"},
#         {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品"},
#         {"question": "如何制作一杯完美的拿铁咖啡？", "lable": "咖啡制作"},
#         {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品"},
#         {"question": "如何制作一杯完美的拿铁咖啡？", "lable": "咖啡制作"},
#         {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品"},
#         {"question": "如何制作一杯完美的拿铁咖啡？", "lable": "咖啡制作"},
#         {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品"},
#         {"question": "如何制作一杯完美的拿铁咖啡？", "lable": "咖啡制作"},
#         {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品"},
#         {"question": "如何制作一杯完美的拿铁咖啡？", "lable": "咖啡制作"},
#         {"question": "如何选择一台适合自己的笔记本电脑？", "lable": "科技产品"}
#     ]
# }

