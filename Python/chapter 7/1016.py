import math

min_num, max_num = map(int, input().split())
check = [False] * (max_num - min_num +1)

count = 0
for i in range(2, int(math.sqrt(max_num))+1): #**1/2를 썼을 땐 시간초과가 나는데, math 함수를 쓰니 시간초과가 안난다(ㅠㅠ)
    pow = i*i
    start_idx = min_num//pow
    if min_num % pow != 0:
        start_idx+=1
    
    for j in range(start_idx, int(max_num//pow)+1):
        temp = j * pow
        check[temp - min_num] = True

count = 0
for i in check:
    if i == False:
        count+=1


print(count)