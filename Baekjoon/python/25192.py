# source : https://www.acmicpc.net/problem/25192

import sys
input = sys.stdin.readline

def main():
    record_set = set()
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        record = input().rstrip()
        
        if record == 'ENTER':
            if len(record_set) > 0:
                result += len(record_set)
                record_set.clear()
        else:
            record_set.add(record)
    
    if len(record_set) > 0:
        result += len(record_set)
    
    print(result)

if __name__ == '__main__':
    main()