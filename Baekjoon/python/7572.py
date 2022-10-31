# source : https://www.acmicpc.net/problem/7572

# input
N = int(input())

ten = '6789012345'
zodiac = 'IJKLABCDEFGH'

print(zodiac[N % 12] + ten[N % 10])