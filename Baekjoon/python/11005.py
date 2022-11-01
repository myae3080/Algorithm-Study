# source : https://www.acmicpc.net/problem/11005

# input
N, B = map(int, input().split())

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''
while N > 0:
    result += number[N % B]
    N //= B
    
print(result[::-1])