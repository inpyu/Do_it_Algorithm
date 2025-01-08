a = int(input())
sum = int(input())
ing_list = list(map(int, input().split()))

ing_list.sort()

start_idx = 0
end_idx = a - 1
count = 0

while(end_idx > start_idx):
    if(ing_list[start_idx] + ing_list[end_idx] == sum):
        count += 1
        end_idx -= 1
        start_idx += 1
    elif(ing_list[start_idx] + ing_list[end_idx] > sum):
        end_idx -= 1
    elif(ing_list[start_idx] + ing_list[end_idx] < sum):
        start_idx += 1

print(count)