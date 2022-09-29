# source : https://www.acmicpc.net/problem/11006

for _ in range(int(input())):
    # input
    legs, chickens = map(int, input().split())
    
    one_leg = chickens * 2 - legs
    print(one_leg, chickens - one_leg)