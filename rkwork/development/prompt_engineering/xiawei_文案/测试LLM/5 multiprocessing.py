import multiprocessing
from datetime import datetime
import time

def worker(args):
    """线程工作函数，返回工作结果"""
    name, duration = args  # 从args元组中解包name和duration
    # 获取当前时间
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{start_time} - Worker: {name} started')

    # 模拟工作负载
    time.sleep(duration)

    # 获取当前时间
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{end_time} - Worker: {name} finished after {duration} seconds')
    return f"{name} completed"

if __name__ == '__main__':
    # 创建任务列表，每个任务是一个元组，包含name和duration
    tasks = [
        ('John', 2),
        ('Mary', 3)
    ]

    # 创建一个进程池，池中进程数量为2
    with multiprocessing.Pool(processes=2) as pool:
        # 使用map_async方法将任务列表提交给进程池，并获取AsyncResult对象
        results = pool.map_async(worker, tasks)

        # 获取所有任务结果
        for result in results.get():
            print(result)

    # 所有任务完成后打印消息
    print("All tasks completed.")