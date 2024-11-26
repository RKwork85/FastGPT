import os 

dirname = "XiaWei_ID_"

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
for i in range(1, 100):
    name = dirname + str(i)
    os.mkdir(name)
