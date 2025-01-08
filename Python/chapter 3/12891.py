dna, lenth = map(int, input().split())
dnaString = input()
a, c, g, t = map(int, input().split())
dic = {'A':a, 'C':c, 'G':g, 'T': t}
count = {'A':0, 'C':0, 'G':0, 'T': 0}
answer = 0

for i in range(dna - lenth +1):

    flag = True
    if i == 0:
        for j in range(lenth):
            count[dnaString[j]] += 1
    
    else:
        count[dnaString[i + lenth -1]] += 1
        count[dnaString[i- 1]] -= 1
    for key in ('A', 'C', 'G', 'T'):
        if count[key] < dic[key]:
            flag = False
            break

    if flag:
        answer+=1

print(answer)