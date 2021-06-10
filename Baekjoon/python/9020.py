# math, prime number, Sieve of Eratosthenes, Goldbach's conjecture

import sys

# input
count = int(input())
num_list = [int(sys.stdin.readline()) for i in range(count)]

# prime number setting(Sieve of Eratosthenes)
n = 10001
prime_num_list = [True] * n

m = int(n ** 0.5)
for i in range(2, m + 1):
    if prime_num_list[i] == True:           
        for j in range(i + i, n, i):
            prime_num_list[j] = False

''' 
    시간 초과 때문에 여러 방법 다 써봤지만, 소수만 골라 담은 list를 돌면서 하는 방법보다
    true, false에 해당 하는 index 값 찾아 출력하는 쪽으로 구현
'''
for even_num in num_list:
    range_num = even_num // 2
    
    for i in range(range_num):
        if prime_num_list[range_num - i] * prime_num_list[range_num + i]:
            print(range_num - i, range_num + i)
            break