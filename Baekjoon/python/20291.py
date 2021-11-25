# source : https://www.acmicpc.net/problem/20291
# parsing

file_dict = {}

for _ in range(int(input())):
    # input
    extension = input().split(".")[1]
    
    if extension not in file_dict:
        file_dict[extension] = 1
    else:
        file_dict[extension] += 1

file_dict = sorted(file_dict.items())

[print(tu[0], tu[1]) for tu in file_dict]