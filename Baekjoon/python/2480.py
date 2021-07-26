# math

# input
num_list = sorted(list(map(int, input().split())), reverse=True)

count = len(set(num_list))

if count == 3:
    print(num_list[0] * 100)
elif count == 2:
    print(1000 + (num_list[1] * 100))
else:
    print(10000 + (num_list[0] * 1000))