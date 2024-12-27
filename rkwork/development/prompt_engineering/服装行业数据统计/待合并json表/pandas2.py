import json
import pandas as pd
import numpy as np

# 定义df1
df1 = pd.DataFrame({'alpha': ['A', 'B', 'B', 'C', 'D', 'E'],
                    'feature1': [1, 1, 2, 3, 3, 1],
                    'feature2': ['low', 'medium', 'medium', 'high', 'low', 'high']})

# 定义df2
df2 = pd.DataFrame({'alpha': ['A', 'A', 'B', 'F'],
                    'pazham': ['apple', 'orange', 'pine', 'pear'],
                    'kilo': ['high', 'low', 'high', 'medium'],
                    'price': np.array([5, 6, 5, 7])})

# 基于共同列alpha的内连接
df3 = pd.merge(df1, df2, how='inner', on='alpha')

# 输出到JSON文件
with open('output.json', 'w') as f:
    json_data = {
        'df1': df1.to_dict(orient='records'),
        'df2': df2.to_dict(orient='records'),
        'df3': df3.to_dict(orient='records')
    }
    json.dump(json_data, f, indent=4)

print("数据已成功输出到 output.json 文件。")