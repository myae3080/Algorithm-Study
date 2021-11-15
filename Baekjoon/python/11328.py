# source : https://www.acmicpc.net/problem/11328
# string

for _ in range(int(input())):
    # input
    str_a, str_b = input().split()
    
    print("Possible") if sorted(list(str_a)) == sorted(list(str_b)) else print("Impossible")