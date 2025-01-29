from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

q = PriorityQueue()

num = int(input())

for i in range(num):
    inputNum = int(input())
    if(inputNum == 0):
        if q.empty():
            print('0\n')
        else:
            printNum = q.get()
            print(str(printNum[1]) + '\n')
    else:
        q.put((abs(inputNum), inputNum))
