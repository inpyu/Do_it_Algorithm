import sys
input = sys.stdin.readline
n, sCity, eCity, m = map(int, input().split())
edges = []
distance = [-sys.maxsize] * n

for _ in range(m):
    start, end, price = map(int, input().split())
    edges.append((start,end,price))

cityMoney = list(map(int,input().split()))

distance[sCity] = cityMoney[sCity]

for i in range(n+101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + cityMoney[end] - price:
            distance[end] = distance[start] + cityMoney[end] - price
            if i >= n-1:
                distance[end] = sys.maxsize

if distance[eCity] == -sys.maxsize:
    print("gg")
elif distance[eCity] == sys.maxsize:
    print("Gee")
else:
    print(distance[eCity])