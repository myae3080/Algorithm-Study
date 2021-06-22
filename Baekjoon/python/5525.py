# string

'''
    50점
    TODO 100점
'''
# input
n = int(input())
m = int(input())
input_str = input()

n_str = ''
count = 0

for i in range(2 * n + 1):
    if i % 2 == 0:
        n_str += 'I'
    else:
        n_str += 'O'

for i in range(len(input_str) - len(n_str) + 1):
    if input_str[i:i + len(n_str)] == n_str:
        count += 1

print(count)