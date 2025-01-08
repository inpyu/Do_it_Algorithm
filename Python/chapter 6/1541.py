string_list = list(map(str, input().split("-")))
plus_list = list(map(int, string_list[0].split("+")))
answer = sum(plus_list)
for i in range(1,len(string_list)):
    num_list = list(map(int, string_list[i].split("+")))
    temp = sum(num_list)
    answer -= temp

print(answer)