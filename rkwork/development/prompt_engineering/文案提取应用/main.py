import multiprocessing
import os
import json 
import time
from openai import OpenAI
import re
question_data= "https://www.douyin.com/video/7447493344692948278"


def indexInsert(rawdata, newdata):
    rawdata.pop('user_signature', None)
    rawdata.pop('user_unique_id', None)
    rawdata.pop('short_user_id', None)

    rawdata_list = list(rawdata.items())
    newdata_list = list(newdata.items())

    rawdata_list.insert(5, newdata_list[0])
    result = dict(rawdata_list)
    return result

def cat_prompt(data):

    prompt = '''
以上信息是一个文案模版，请将输入的产品信息，融入到文案模版，生成一篇文案，产品信息中不存在的细节不可以在生成的文案中出现，文案模版中的通用部分可以适当在生成的文案中体现，语言风格自然，正常沟通方式
品牌：速惟
产品：宽下摆运动内衣
FAB 产品解说: 侧翼加高。隐藏副乳，贴合身体。使穿着者视觉上更显瘦，增强自信心。, V 形美背。提升散热能力，大方露出背部肌肤。让穿着者在运动中保持清爽，同时展现出迷人的背部曲线。
面料宣传: 丝滑弹力面料，舒适支撑，展现完美身姿。
工艺: 净色
运动场景: 骑行, 器械
一句话宣传: 外穿无压力的运动内衣，超适合夏天户外！
用户痛点:
版型宣传:
颜色: 明月白
设计宣传: 加宽下摆设计，舒适无束缚。
面料解说: 面料的弹力性能，使得运动内衣能够更好地贴合身体，提供良好的支撑。
'''
    question_data =  data + prompt
    print(question_data)
    return question_data


def chat_request(questionJson):
    
    question = cat_prompt(questionJson['文案內容'])    

    client = OpenAI(base_url="https://api.deepseek.com", api_key="sk-13870ed83bb741e59db6ca2877726057")
    response = client.chat.completions.create(
        model="deepseek-chat",                                            
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {'role': 'user', 'content': f'{question}'}
            ],
        stream= True
        )
    data_chunk = ''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:

            data_chunk += chunk.choices[0].delta.content

    result = indexInsert(questionJson, {"生成文案": data_chunk})
    print(result)
    return result






# 提供的文本
if __name__ == '__main__':
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    result_list = []

    with open('/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/文案提取应用/运动内衣_filter_low_200_liked.json','r', encoding='utf-8') as f:
        data = json.load(f)

    start = time.time()    
    samples = data[0:2]
    with multiprocessing.Pool(processes=100) as pool:
        results = pool.map_async(chat_request, data)
        
        for index, result in enumerate(results.get()):
            result_list.append(result)



    end = time.time()
    print(f"最终执行时间{end - start}")
    with open('/home/rkwork/rkwork/project/FastGPT/rkwork/development/prompt_engineering/文案提取应用/运动内衣_gen_finally2.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False, indent=4)



