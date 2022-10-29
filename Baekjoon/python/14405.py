# source : https://www.acmicpc.net/problem/14405

# input
word = input()

word = word.replace('pi', '1').replace('ka', '1').replace('chu', '1').replace('1', '')

print('YES') if not word else print('NO')