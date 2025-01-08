import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    node, left, right = input().split()
    tree[node] = [left, right]

def preOrder(now):
    if now =='.':
        return
    print(now, end='')
    preOrder(tree[now][0])
    preOrder(tree[now][1])

def lastOrder(now):
    if now =='.':
        return
    lastOrder(tree[now][0])
    lastOrder(tree[now][1])
    print(now, end='')

def inOrder(now):
    if now =='.':
        return
    inOrder(tree[now][0])
    print(now, end='')
    inOrder(tree[now][1])

preOrder('A')
print()
inOrder('A')
print()
lastOrder('A')