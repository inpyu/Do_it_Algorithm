n = int(input())
start = 1
end = 1
sum = 1
count = 1

while end != n:
    if(sum > n):
        sum -= start
        start += 1
    elif(sum < n):
        end += 1
        sum += end
    elif(sum == n):
        count +=1
        end += 1
        sum += end

print(count)