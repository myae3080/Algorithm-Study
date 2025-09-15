# source : https://www.acmicpc.net/problem/17206

import sys

input = sys.stdin.readline

def main():
    # input
    N = int(input())
    problems = list(map(int, input().split()))

    result = [0] * 80001
    cumul_sum = 0
    for n in range(3, 80001):
        if n % 3 == 0 or n % 7 == 0:
            cumul_sum += n
        
        result[n] = cumul_sum
    
    for i in range(N):
        print(result[problems[i]])

if __name__ == '__main__':
    main()