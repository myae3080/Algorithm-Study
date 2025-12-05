# source : https://www.acmicpc.net/problem/5366

import sys

input = sys.stdin.readline

def main():
    names = []
    cnt_by_name = {}
    while 1:
        # input
        name = input().rstrip()

        if name == '0':
            break

        if name not in names:
            names.append(name)
        
        if name in cnt_by_name:
            cnt_by_name[name] += 1
        else:
            cnt_by_name[name] = 1
    
    total = 0
    for name in names:
        print('%s: %d' % (name, cnt_by_name[name]))

        total += cnt_by_name[name]
    
    print('Grand Total: %d' % total)

if __name__ == '__main__':
    main()