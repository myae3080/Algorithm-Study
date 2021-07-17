# sorting, two pointer

# input
n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.extend(b_list)

print(str(sorted(a_list)).replace('[', '').replace(']', '').replace(',', ''))