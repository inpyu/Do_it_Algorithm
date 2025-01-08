a, b = map(int, input().split())
numList = list(map(int, input().split()))
sumList = []
sumList2 = [0] * b
sum = 0
answer = 0
for i in numList :
    sum = sum + i
    sumList.append(sum)

for i in sumList :
    sumList2[ i % b ] += 1
    if i % b == 0:
        answer += 1

for i in sumList2:
    if i > 1:
        answer += (i*(i-1) // 2)

print(answer)

