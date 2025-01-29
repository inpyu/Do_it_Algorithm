num = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
count = 0

for i in range(num):
    find = num_list[i]
    start_idx = 0
    end_idx = num -1

    while(start_idx < end_idx):
        if(num_list[start_idx] + num_list[end_idx] == find):
            if(start_idx != i and end_idx != i): # 중복 값이 있을 수 있으므로 idx로 검사 필요 !!!!! 
                count += 1
                break   
            elif(start_idx == i):
                start_idx += 1
                
            elif(end_idx == i):
                end_idx -= 1
        elif(num_list[start_idx] + num_list[end_idx] > find):
            end_idx -= 1
        elif(num_list[start_idx] + num_list[end_idx] < find):
            start_idx += 1

print(count)