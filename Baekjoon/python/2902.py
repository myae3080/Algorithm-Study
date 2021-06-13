# string

'''
    두 번째 풀이
'''
# input
for s in input().split('-'):
    print(s[0], end='')

'''
    첫 번째 풀이
'''
short_name = ''

# input
for s in input().split('-'):
    short_name += s[0]

print(short_name)