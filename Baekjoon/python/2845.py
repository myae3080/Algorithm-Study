# math

# input
n, p = map(int, input().split())
total = n * p

for i in [k - total for k in map(int, input().split())]:
    print(i, end=' ')
