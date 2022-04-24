import os
import psutil

print(os.getpid()) # python이 실행되고 있는 pid 값
print(psutil.Process(os.getpid()).ppid()) # 해당 python의 parent pid 값
