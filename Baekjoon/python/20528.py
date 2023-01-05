# source : https://www.acmicpc.net/problem/20528

# input
n = int(input())
palindromes = [s[0] for s in input().split()]

print(1) if len(set(palindromes)) == 1 else print(0)