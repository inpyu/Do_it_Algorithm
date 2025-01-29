from collections import deque

num, window = map(int, input().split())
num_list = list(map(int, input().split()))

mydeque = deque()
for i in range(num):
    while(mydeque and mydeque[-1][0] > num_list[i]):
        mydeque.pop()
    mydeque.append((num_list[i],i))
    if(mydeque[0][1] <= i - window):
        mydeque.popleft()
    print(mydeque[0][0], end=' ')