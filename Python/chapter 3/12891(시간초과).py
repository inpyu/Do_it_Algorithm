dna, lenth = map(int, input().split())
dnaString = input()
a, c, g, t = map(int, input().split())
answer = 0

start_idx = 0
end_idx = lenth
for i in range(0, len(dnaString)):
    if(end_idx > len(dnaString)):
        break
    password = dnaString[start_idx:end_idx]
    if((password.count('A') >= a) and (password.count('C') >= c) and (password.count('G') >= g) and (password.count('T') >= t) ):
        answer +=1 
    start_idx += 1
    end_idx +=1

print(answer)