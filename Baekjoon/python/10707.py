# source : https://www.acmicpc.net/problem/10707
# math

# input
x_price = int(input())
y_price = int(input())
maximum = int(input())
extra_fee = int(input())
water = int(input())

x = x_price * water

if maximum > water:
    y = y_price
else:
    y = y_price + ((water - maximum) * extra_fee)

print(x) if x < y else print(y)