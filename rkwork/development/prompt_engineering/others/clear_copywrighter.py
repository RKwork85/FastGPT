import multiprocessing
import os
import json 
import time
from openai import OpenAI
import re
question_data= "🎼我最近看到小象人家里面有两个家庭，沈吟，他们家为什么过得比较幸福？反观林姐家就过得鸡飞口跳。那通过两家对比，往上走和往下走的家庭最大的差异就是两点。第一点，往上走的家庭都是统一战线的，知道什么才是家庭的核心利益，而往下走的家庭心都是不齐的，各自有各自的算盘，其中在这个电视剧里面有个片段是邻居敲掉了院墙墙角的 2 块砖，积水就。😊全部流到了宋英家院子里。宋英对着隔壁就骂，而林武峰呢不声不响的运了几麻袋的这个泥巴，然后降雨过后，直接堵住小院出水管，积水进不来了。那反观之前使坏了邻居家呢，美女堵门，积水就全进家里去了。最后林俊就来赔笑脸道歉，说，哎呀，会把这个院墙补好。而黄玲姐家呢，她在前面冲锋陷阵解决问题的时候，她老公只站在父母那一边，林姐给自己小家庭争取利益的时候，庄超一。🎼还跟着父母一起骂黄玲，无情无义。那第二点就是往上走的这个家庭，夫妻俩是真的互相心疼的，而往下走的家庭，彼此都不心疼对方，或者只有一方心疼另一方，另一方就是看不上另外一方，宋莹上夜班，林武峰给他准备饭盒，送她去工厂。宋莹想要电视机，林武峰就用 50 斤的粮票，从同事那里换来了电视机票，连他跟邻居吵架，林武峰都会追出来为他披件衣裳。那宋莹开了早餐铺呢，林武峰也跟着早起，宋莹就。心疼林五峰，哎呀，不用他赔了，这两夫妻恩爱，孩子看在眼里，儿子林栋哲长大之后，也是一样对女朋友林小婷体贴又疼爱的。但是我们反观玲姐家呢，庄超英从来没为黄玲撑过腰，两人钱各管各的，庄超英每月还拿 3 分之 1 的工资补贴她父母。黄林月子里，庄超英咬牙切齿跟她吵架。那还有就是两口子带着孩子去给婆婆过生日，黄林是忙前忙后住了一桌子的菜，最后做完了，还准备上桌吃饭，一看没。😊🎼他位置，结果她老公说，哎，让他旁边去吃，不要上桌子。黄丽就跟庄超英说，我靠不上你。那他俩的儿子装图难呢，就明知道妈妈和妹妹在家里受欺负，也从来不维护他们。所以你们可以看到，往下走的家庭不就是应的那句老话吗？父爱则母敬，母敬则子安，子安则家和，家和万事兴。那往下走的家庭，就是这句话的下半一句，父难则母苦，母苦则子惧，子惧则家衰，家衰衰三代。"


def chat_request(questionJson):
    question = questionJson['视频内容']

    # 在函数内部创建client实例
    client = OpenAI(
       base_url="http://aiagent-pre.chengwen.net/api/v1",  
       api_key="prechengwenai-oTTsCuV7U4yNBu5XQUjDCk5kSrIRK1REFMbmWdeoneiIzK1FWz40"
    )


    try:    #整个程序的try
        completion = client.chat.completions.create(
            model="doubao-pro-128k",
            messages=[{'role': 'user', 'content': f'{question}'}],
        )
        
        completion_cp = completion.model_dump_json()
        data = json.loads(completion_cp)
        content = (data["choices"][0]['message']['content'])
        questionJson.update({'AI清理': content})

        print(questionJson) 
        return questionJson
    except Exception as e:
        print(e)




start = time.time()
count = 0
# 创建一个进程池，池中进程数量为2
os.chdir(os.path.dirname(os.path.abspath(__file__)))

task =[]
# 构造输入数据
with open('clearData.json','r', encoding='utf-8') as f:
    data = json.loads(f.read())


resultList = []
# task = [question_data for _ in range(1) ]
with multiprocessing.Pool(processes=20) as pool:
    # 使用map_async方法将任务列表提交给进程池，并获取AsyncResult对象
    results = pool.map_async(chat_request, data)
    

    # 获取所有任务结果
    for index,result in enumerate(results.get()):
        resultList.append(result)


        
end = time.time()

print('count:', count)
print(f"最终执行时间{end - start}")

with open('AICleared_data.json', 'a+', encoding='utf-8') as f:
    json.dump(resultList, f, ensure_ascii=False, indent=4)

