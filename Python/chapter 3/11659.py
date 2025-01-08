import sys
a, b = map(int, input().split())
numList = list(map(int, input().split()))
sumList = [0]
sum = 0
for i in numList:
    sum = sum + i
    sumList.append(sum)

for i in range(0, b):
    start, end = map(int, input().split())
    print(sumList[end] - sumList[start - 1])