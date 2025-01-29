from queue import PriorityQueue

count = int(input())
pq = PriorityQueue()
for i in range(count):
    num = int(input())
    pq.put(num)

answer = 0
while pq.qsize() > 1 :
    min_num = pq.get()
    min_num2 = pq.get()
    temp = min_num + min_num2
    answer += temp
    pq.put(temp)

print(answer)
    