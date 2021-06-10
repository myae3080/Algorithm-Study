# math

burger_list = []
beverage_list = []

for i in range(5):
    price = int(input())

    if i < 3:
        burger_list.append(price)
    else:
        beverage_list.append(price)

print(min(burger_list) + min(beverage_list) - 50)