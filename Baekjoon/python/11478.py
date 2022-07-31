# source : https://www.acmicpc.net/problem/11478

# input
string = input()

length = len(string)
subsets = set()

for i in range(length):
    for j in range(i, length):
        subsets.add(string[i:j + 1])
        
print(len(subsets))
