n = int(input())

result = n

for i in range(2, int(n ** 1/2)+1):
    if n % i == 0: # 소인수 아님
        result -= result/i
        while n % i == 0:
            n /= i


print(int(result))