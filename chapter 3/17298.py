size = int(input())
num_list = list(map(int, input().split()))

ans = [0] * size #위치에 따른 오큰수 저장
count = 0
stack = []

for i in range(size):
    while(stack and num_list[stack[-1]] < num_list[i]):
        ans[stack.pop()] = num_list[i]
    stack.append(i)

while(stack):
    ans[stack.pop()] = -1

for i in ans:
    print(i, end=" ")