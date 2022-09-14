# source : https://www.acmicpc.net/problem/1919

# input
word1, word2 = input(), input()

characters1, characters2 = [0] * 26, [0] * 26

for c in word1:
    characters1[ord(c) - 97] += 1
    
for c in word2:
    characters2[ord(c) - 97] += 1

print(sum([abs(characters1[i] - characters2[i]) for i in range(26)]))