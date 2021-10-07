# source : https://www.acmicpc.net/problem/20362
# string

# input
n, nickname = input().split()

answer_list = []
correct, index = '', 0

for i in range(int(n)):
    # input
    nick, answer = input().split()

    answer_list.append(answer)

    if nickname == nick:
        correct = answer
        index = i

print(answer_list[:index].count(correct))