# source : https://www.acmicpc.net/problem/11098
# string

for _ in range(int(input())):
    max_cost = 0
    top_name = ''

    for __ in range(int(input())):
        # input
        cost, name = input().split()

        if int(cost) > max_cost:
            max_cost = int(cost)
            top_name = name

    print(top_name)