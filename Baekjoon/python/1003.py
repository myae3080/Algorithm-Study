# dp

import sys

fibo_db_list = [
    [1, 0],
    [0, 1],
    [1, 1]
]

for n in range(3, 41):
    fibo_db_list.append([fibo_db_list[n - 2][0] + fibo_db_list[n - 1][0], fibo_db_list[n - 2][1] + fibo_db_list[n - 1][1]])

for i in range(int(input())):
    # input
    n = int(sys.stdin.readline())

    result_list = fibo_db_list[n]

    print(result_list[0], result_list[1])