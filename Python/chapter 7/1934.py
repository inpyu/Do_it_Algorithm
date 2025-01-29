num = int(input())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


for i in range(num):
    a, b = map(int, input().split())
    result = a * b / gcd(a,b)
    print(int(result))