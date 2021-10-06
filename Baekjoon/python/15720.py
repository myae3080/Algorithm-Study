# source : https://www.acmicpc.net/problem/15720
# math, greedy algorithm, sorting

# input
burger, side, beverage = map(int, input().split())
burger_list = sorted(list(map(int, input().split())), reverse=True)
side_list = sorted(list(map(int, input().split())), reverse=True)
beverage_list = sorted(list(map(int, input().split())), reverse=True)

total = 0
minimum = min(burger, side, beverage)

for i in range(max(burger, side, beverage)):
    if i < minimum:
        total += int((burger_list[i] + side_list[i] + beverage_list[i]) * 0.9)
    else:
        if i < burger:
            total += burger_list[i]

        if i < side:
            total += side_list[i]

        if i < beverage:
            total += beverage_list[i]

print(sum(burger_list) + sum(side_list) + sum(beverage_list))
print(total)