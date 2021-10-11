# source : https://www.acmicpc.net/problem/11943

# input
first_basket = list(map(int, input().split()))
second_basket = list(map(int, input().split()))

print(min(first_basket[0] + second_basket[1], first_basket[1] + second_basket[0]))