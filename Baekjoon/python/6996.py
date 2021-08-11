# source : https://www.acmicpc.net/problem/6996
# sorting

for _ in range(int(input())):
    # input
    str1, str2 = input().split()

    str1_list = sorted([s for s in str1])
    str2_list = sorted([s for s in str2])

    if str1_list == str2_list:
        print('{} & {} are anagrams.'.format(str1, str2))
    else:
        print('{} & {} are NOT anagrams.'.format(str1, str2))