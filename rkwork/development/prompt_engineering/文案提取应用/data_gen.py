import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)


topic = ["日常话题", "功能话题", "风格话题","场景话题", "好物话题", "个性话题"]
result_data = []
for i in topic:
    user_question =f"""针对一款产品属性生成一条口播的文案：
    语言风格：自然，正常，生活场景词汇；
    开头引入：请从{i}话题中具体的某一点作为铺垫，引入文案
    内容：多角度，多场景谈自己对产品的细节感受，结合自己过往的经历，代入观众的感受；修辞手法的适当应用
    过渡：不要有直接明显的过渡词汇
    产品：速惟 宽下摆运动内衣
    中强度：瑜伽伴侣 稳固不上窜
    设计卖点：
    1.加长背心式，外穿不尴尬
    2.侧翼加高，隐藏副乳，贴合不溢
    3.V 形美背，凸显背后曲线更显瘦
    4.加宽下摆，舒适不勒腰
    5.固定胸杯，增加承托力，穿着更稳定运动不跑位
    输出时，只生成文案, 不输出其他内容
    """

    single_data = {"topic": i,"question": user_question}

    for i in range(1, 31):
        data = {"ID": i, **single_data}
        print(single_data)
        result_data.append(data)


    with open("topics_data.json", "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=4)