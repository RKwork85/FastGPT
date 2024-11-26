txt = '''参照示例文案结构，文案仿写，要求文案结构一致，语言风格一致，主题父母，示例结构如下：在这个世界上，只有父母给我们吃的饭是免费的，其他每一餐都需要付出代价。
如果有一天啊你把父母的心伤透了，那在这世界上可能真的找不到一个人无私的对你这么好了。'''
import os 
aim_list = []
current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)
with open('hhh.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 301):
        f.write(str(i) + '\n')