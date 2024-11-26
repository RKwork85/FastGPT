import os 

import json

current_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_path)

json_file = []
for i in range(1,1001):
    json_file.append(i)

with open("number.txt", 'w') as f:
        f.write(str(json_file))
