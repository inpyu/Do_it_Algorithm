n = int(input())

def primary(num):
    for i in range(2, int(num ** 0.5)+1) :
        if num % i == 0 :
            return False
    return num != 1

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


while True:
    if primary(n) and is_palindrome(n):
        print(n)
        exit()
    n+=1