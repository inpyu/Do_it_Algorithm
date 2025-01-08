from queue import PriorityQueue

num = int(input())
pos_q = PriorityQueue()
neg_q = PriorityQueue()
one = 0
zero = 0
answer = []
for _ in range(num):
    i = int(input())
    if i > 1:
        pos_q.put(i*-1)
    elif i < 0:
        neg_q.put(i)
    elif i == 1:
        one +=1 
    elif i == 0 :
        zero += 1

sum = 0

while neg_q.qsize() > 1:
    num1 = neg_q.get()
    num2 = neg_q.get()
    sum += (num1 * num2)

if neg_q.qsize() == 1:
    if zero == 0:
        sum += neg_q.get()

while pos_q.qsize() > 1:
    num1 = pos_q.get()
    num2 = pos_q.get()
    sum += (num1 * num2)

if pos_q.qsize() > 0:
    sum += pos_q.get()*(-1)

if one > 0 :
    sum += one
print(sum)