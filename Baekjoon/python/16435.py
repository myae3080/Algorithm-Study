# sorting, greedy algorithm

# input
n, l = map(int, input().split())
h_list = sorted(list(map(int, input().split())))

for h in h_list:
    if l >= h:
        l += 1
    else:
        break

print(l)