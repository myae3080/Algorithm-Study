# source : https://www.acmicpc.net/problem/10570

import sys
input = sys.stdin.readline

def main():
    # input
    for _ in range(int(input())):
        count_by_note = {}
        
        # input
        for __ in range(int(input())):
            # input
            num = int(input())
            
            if num in count_by_note:
                count_by_note[num] += 1
            else:
                count_by_note[num] = 1
                
        print(sorted(count_by_note.items(), key = lambda item: (-item[1], item[0]))[0][0])

if __name__ == '__main__':
    main()