import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n+1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a,b)
    else:
        if checkSame(a,b):
            print("YES")
        else:
            print("NO")