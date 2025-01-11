hhh = '**标题：** 大眼版卡皮巴拉，大家觉得可爱吗？#卡皮巴拉 #雷军的好物分享\n**作者：** 雷军\n**视频ASR文本：** 这是童师傅的一个脚摆件大眼版的卡皮巴拉这个卡皮巴拉呢看起来好像没有我们小米小折叠的卡皮巴拉情绪那么稳定 我桌上还摆了一个小米速七  ultra  的车模这个车模是越看呢越好看也得好好擦一擦前段时间呢我还收到一个新的奖杯这是抖音送的我在抖音里面也应该算小有名气的博主 现在呢又进步了一点点你们的桌面都摆些什么东西啊平时会经常擦吗\n**视频或图片OCR文本：** |SU7tllere|这是铜师傅的一个小摆件|大眼版的卡皮巴拉|这个卡皮巴拉呢|好像没有我们|小米小折叠的卡皮巴拉|0344 情绪那么稳定啊|我桌上还摆了一个|小米SU7UItra的车模|这个车模是越看呢越好看|也得好好擦一擦|前段时间呢|我还收到一个新的奖杯|我在抖音里面|0000000 三千万猫丝成就纪念 雷军 抖音号:xnloijum 也应该算小有名气的博主|UNFOLD2010TX 雷军 小米创办人董事长兼CEO 1.7亿获赞99关注3751.7万粉丝 热爱是所有的理由和答案。 IP属地:北京 男 已实名 武汉大学 商品橱窗 0件好物 直播动态 公28 查看历史记录 已关注 私信 作品458 雷军带 和雷军一起聊车> 雷军的好物分享> 置顶 置顶 置顶 冬天开小米SU7 强迫症福利 今天我来当导演|现在呢又进步了一点点|+750W|你们的桌面都摆些什么东西啊|平时会经常擦吗|擦一擦我的卡皮巴拉 大家桌面一般摆啥?\n'







import multiprocessing
import os
import json 
import re
import time
from openai import OpenAI

question_data= "https://www.douyin.com/video/7317848191443995931"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def chat_request(question):
    # 在函数内部创建client实例
    client = OpenAI(base_url="http://aiagent-pre.chengwen.net/api/v1", api_key="prechengwenai-rwcUdjvhFxYyxtUrI5CtYxouAj82stiiua3Sw8ueRO2L5J3xX0ZXm3rZ")
    response = client.chat.completions.create(
        model="doubao-pro-128k",                                            
        messages=[
            # {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': f'{question}'}],
        stream= True
        )
    data_chunk = ''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            # print(chunk.choices[0].delta.content, end="")
            data_chunk += chunk.choices[0].delta.content

    # print("data_chunk 内容：",data_chunk)
    json_pattern = r'\{.*?\}'
    json_match = re.search(json_pattern, data_chunk, re.DOTALL)
    if json_match:
        json_data_str = json_match.group(0)
        print(json_data_str, type(json_data_str))
        try :
            content = json_data_str.strip()
            clear_data = content.replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')
            data = json.loads(clear_data)
            return data
        
        #     json_data_str = json_match.group(0)
        # data = json.loads(completion_cp)
        # content = (data["choices"][0]['message']['content'])
        # content = content.strip()
        # print("返回内容：",repr(content))
        # clear_data = content.replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')
        # print("清理后的内容：", clear_data)

        # content = str(content)
        # try:
        #     json_data = json.loads(clear_data)
        #     print("解析成功！", json_data["paragraph"])
        #     return json_data  # 返回包含结果的列表
        except Exception as e:
            print(e)




start = time.time()
result_list = []
# 创建一个进程池，池中进程数量为2
task = [question_data for _ in range(1) ]

with multiprocessing.Pool(processes=20) as pool:
    # 使用map_async方法将任务列表提交给进程池，并获取AsyncResult对象
    results = pool.map_async(chat_request, [task[0]])
    

    # 获取所有任务结果
    for index,result in enumerate(results.get()):
        print("result返回内容",result, type(result))
        result_list.append(result)
        

end = time.time()
print(f"最终执行时间{end - start}")

with open('服装行业访谈型对标表测试2.json', 'w', encoding='utf-8') as f:
    json.dump(result_list, f, ensure_ascii=False, indent=4)