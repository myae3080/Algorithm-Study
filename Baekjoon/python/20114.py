# source : https://www.acmicpc.net/problem/20114

def main():
    # input
    n, h, w = map(int, input().split())
    note = [list(input()) for _ in range(h)]

    compressed = [''] * len(note[0]) 
    for li in note:
        for i in range(len(li)):
            if compressed[i] == '' or compressed[i] == '?':
                compressed[i] = li[i]
    
    result = [''] * n
    for i in range(len(compressed)):
        target_idx = i // w
        if result[target_idx] == '' or result[target_idx] == '?':
            result[target_idx] = compressed[i]
    
    print(''.join(result))

if __name__ == '__main__':
    main()