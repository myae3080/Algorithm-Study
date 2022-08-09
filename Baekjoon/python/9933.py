# source : https://www.acmicpc.net/problem/9933

# input
words = [input() for _ in range(int(input()))]

for word in words:
    if words.count(word[::-1]):
        print(len(word), word[(len(word) // 2)])
        break