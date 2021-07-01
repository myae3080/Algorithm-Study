# math

import sys

# input
input = sys.stdin.readline

for i in range(int(input())):
    # input
    n = int(input())
    num_list = list(map(int, input().rstrip().split()))

    print(sum(num_list))