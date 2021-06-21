# string, parsing

import sys

# input
input = sys.stdin.readline

for i in range(int(input())):
    input_list = input().rstrip().split()
    remove_list = []
    print_list = []

    while True:
        sentence = input().rstrip()

        if sentence == 'what does the fox say?':
            break
        else:
            remove_list.append(sentence.split()[2])
    
    for s in input_list:
        if s not in remove_list:
            print_list.append(s)
    
    print(" ".join(print_list))