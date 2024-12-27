import requests
import json

# 设置请求的URL和Headers
url = 'https://aiagent-pre.chengwen.net/api/v1/chat/completions'
headers = {
    'Authorization': 'Bearer fastgpt-nquanT5fQrNml7AGU66qqFREpOa2GeIIGkAC8JXnxaF6qlcLrqVv',
    'Content-Type': 'application/json'
}

# 设置请求的数据
data = {
    "chatId": "13ad233333333",
    "stream": False,
    "detail": True,
    # "variables": {
    #     "uid": "asdfadsfasfd2323",
    #     "name": "张三"
    # },
    "messages": [
         {
            "role": "user",
            "content": "哲理型文案结构一"
        },
        
    ]
}

# 发送请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 检查响应状态码
if response.status_code == 200:
    # 解析响应内容
    response_data = response.json()
    print("Response Data:", response_data)
    # 检查是否有交互节点
#     if 'interactive' in response_data:
#         interactive_data = response_data['interactive']
#         print("Interactive Data:", interactive_data)
#         # 根据交互节点的类型和参数，引导用户进行选择
#         # 这里是一个示例，实际代码需要根据交互节点的具体类型来处理
#         user_choice = input("请选择一个选项: ")
        
#         # 准备下一次请求的数据
#         next_data = {
#             "chatId": "abcd",
#             "stream": True,
#             "detail": True,
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": user_choice
#                 }
#             ]
#         }
        
#         # 发送下一次请求
#         next_response = requests.post(url, headers=headers, data=json.dumps(next_data))
#         if next_response.status_code == 200:
#             next_response_data = next_response.json()
#             print("Next Response Data:", next_response_data)
#         else:
#             print("Failed to continue workflow")
#     else:
#         print("No interactive node found")
# else:
#     print("Failed to get response")





# Response Data: {'responseData': [{'id': 'nfFrtTTw1Ybp', 'nodeId': 'cIBg2cbUKiPH', 'moduleName': '用户选择#2', 'moduleType': 'userSelect', 'runningTime': 0, 'userSelectResult': '1'}, {'id': 'eT1MtjF0RjUy', 'nodeId': 'sn3zRYmfxy4U', 'moduleName': '判断器#2', 'moduleType': 'ifElseNode', 'runningTime': 0, 'totalPoints': 0, 'ifElseResult': 'IF'}], 'newVariables': {'userId': '66e0fc19b5ea3fdd326f34fe', 'uid': 'asdfadsfasfd2323', 'name': '张三'}, 'id': 'abcd', 'model': '', 'usage': {'prompt_tokens': 1, 'completion_tokens': 1, 'total_tokens': 1}, 'choices': [{'message': {'role': 'assistant', 'content': [{'type': 'interactive', 'interactive': {'type': 'userSelect', 'params': {'description': '感谢您选择了【故事型】文案，接下来 请选择您 喜欢的 文案结构类型，我会为您创组3篇符合该文案结构的文案内容！\n1 讲故事类型文案结构一：欺凌场景(性格) | 孩子  +  做法1 加剧 + 做法2 无效 | 老师或家长 + 转机 寓言递进  + 寓言总结\n2 讲故事类型文案结构二：\n3 ...', 'userSelectOptions': [{'value': '1', 'key': 'option1'}, {'value': '2', 'key': 'option2'}]}, 'entryNodeIds': ['vm6dwxVI41aH'], 'memoryEdges': [{'source': 'ihWXiYcPSk54', 'target': 'ljYjuFkr7N52', 'sourceHandle': 'ihWXiYcPSk54-source-ELSE IF 1', 'targetHandle': 'ljYjuFkr7N52-target-left', 'status': 'waiting'}, {'source': 'sn3zRYmfxy4U', 'target': 'vm6dwxVI41aH', 'sourceHandle': 'sn3zRYmfxy4U-source-IF', 'targetHandle': 'vm6dwxVI41aH-target-left', 'status': 'active'}, {'source': 'vm6dwxVI41aH', 'target': 'ihWXiYcPSk54', 'sourceHandle': 'vm6dwxVI41aH-source-option1', 'targetHandle': 'ihWXiYcPSk54-target-left', 'status': 'waiting'}, {'source': 'lN7HHD8FPVLg', 'target': 'rv4jho1RUpTX', 'sourceHandle': 'lN7HHD8FPVLg-source-right', 'targetHandle': 'rv4jho1RUpTX-target-left', 'status': 'waiting'}, {'source': 'ihWXiYcPSk54', 'target': 'lN7HHD8FPVLg', 'sourceHandle': 'ihWXiYcPSk54-source-IF', 'targetHandle': 'lN7HHD8FPVLg-target-left', 'status': 'waiting'}, {'source': 'rv4jho1RUpTX', 'target': 'dTOAckgNQBni', 'sourceHandle': 'rv4jho1RUpTX-source-right', 'targetHandle': 'dTOAckgNQBni-target-left', 'status': 'waiting'}, {'source': 'dTOAckgNQBni', 'target': 'm15VBD75mePj', 'sourceHandle': 'dTOAckgNQBni-source-right', 'targetHandle': 'm15VBD75mePj-target-left', 'status': 'waiting'}, {'source': 'm15VBD75mePj', 'target': 'sBVGQ7U5TtFh', 'sourceHandle': 'm15VBD75mePj-source-right', 'targetHandle': 'sBVGQ7U5TtFh-target-left', 'status': 'waiting'}, {'source': 'sBVGQ7U5TtFh', 'target': 'hNK6Rp2P7kyW', 'sourceHandle': 'sBVGQ7U5TtFh-source-right', 'targetHandle': 'hNK6Rp2P7kyW-target-left', 'status': 'waiting'}, {'source': 'hNK6Rp2P7kyW', 'target': 'rsSy6VpkKDfE', 'sourceHandle': 'hNK6Rp2P7kyW-source-right', 'targetHandle': 'rsSy6VpkKDfE-target-left', 'status': 'waiting'}, {'source': 'fFFrM5hlpUK2', 'target': 'glc3cxRfDFFr', 'sourceHandle': 'fFFrM5hlpUK2-source-right', 'targetHandle': 'glc3cxRfDFFr-target-left', 'status': 'waiting'}, {'source': 'rsSy6VpkKDfE', 'target': 'fFFrM5hlpUK2', 'sourceHandle': 'rsSy6VpkKDfE-source-right', 'targetHandle': 'fFFrM5hlpUK2-target-left', 'status': 'waiting'}, {'source': '448745', 'target': 'cIBg2cbUKiPH', 'sourceHandle': '448745-source-right', 'targetHandle': 'cIBg2cbUKiPH-target-left', 'status': 'waiting'}, {'source': 'cIBg2cbUKiPH', 'target': 'sn3zRYmfxy4U', 'sourceHandle': 'cIBg2cbUKiPH-source-option1', 'targetHandle': 'sn3zRYmfxy4U-target-left', 'status': 'waiting'}, {'source': 'cIBg2cbUKiPH', 'target': 'sn3zRYmfxy4U', 'sourceHandle': 'cIBg2cbUKiPH-source-option2', 'targetHandle': 'sn3zRYmfxy4U-target-left', 'status': 'waiting'}], 'nodeOutputs': [{'nodeId': '448745', 'key': 'userChatInput', 'value': '1'}, {'nodeId': 'sn3zRYmfxy4U', 'key': 'ifElseResult', 'value': 'IF'}, {'nodeId': 'cIBg2cbUKiPH', 'key': 'selectResult', 'value': '1'}]}}]}, 'finish_reason': 'stop', 'index': 0}]}

# rkwork@rkwork:~/rkwork/project/FastGPT$ /home/rkwork/miniconda3/bin/python /home/rkwork/rkwork/project/FastGPT/rkwork/development/interface_py/chat/jiaohu.py

# Response Data: {'responseData': [{'id': 'jolL4GdZFI2D', 'nodeId': 'vm6dwxVI41aH', 'moduleName': '用户选择', 'moduleType': 'userSelect', 'runningTime': 0.01, 'userSelectResult': '2'}], 'newVariables': {'userId': '66e0fc19b5ea3fdd326f34fe', 'uid': 'asdfadsfasfd2323', 'name': '张三'}, 'id': 'abcd', 'model': '', 'usage': {'prompt_tokens': 1, 'completion_tokens': 1, 'total_tokens': 1}, 'choices': [{'message': {'role': 'assistant', 'content': ''}, 'finish_reason': 'stop', 'index': 0}]}

import re
import json

# 提供的字符串
text = '\n{"URL":"https://www.douyin.com/video/123456789","TITLE":"小夜灯使用介绍","AUTHOR":"雷军","COPYWRITER":"这是一条来自抖音的视频视频中雷军展示了一款小夜灯并介绍了其使用方法和优点他将小夜灯装在床头柜前晚上起夜时会自动亮起无需开大灯非常方便此外还可以将小夜灯贴在衣柜里或洗手间里使用起来更加便捷雷军认为这款小夜灯非常实用家里可以多买几个贴在需要的地方"}\''

# 使用正则表达式提取JSON数据
json_pattern = r'\{.*?\}'
json_match = re.search(json_pattern, text, re.DOTALL)

if json_match:
    json_data_str = json_match.group(0)
    try:
        # 将提取的JSON字符串解析为Python字典
        extracted_json = json.loads(json_data_str)
        print("提取的JSON数据：")
        print(json.dumps(extracted_json, indent=4, ensure_ascii=False), type(extracted_json))
    except json.JSONDecodeError as e:
        print(f"解析JSON时出错：{e}")
else:
    print("未找到匹配的JSON数据")