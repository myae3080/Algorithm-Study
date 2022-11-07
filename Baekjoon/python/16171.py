# source : https://www.acmicpc.net/problem/16171

# input
S, K = input(), input()

string = ''.join([c if c.isalpha() else '' for c in S])

print(0) if string.find(K) == -1 else print(1)