# source : https://www.acmicpc.net/problem/23746

def main():
    dict = {}
    
    # input
    for _ in range(int(input())):
        # input
        small, large = input().split()
        
        dict[large] = small
    
    # input
    compact = input()
    start_idx, end_idx = map(int, input().split())
    
    result = ''
    for c in compact:
        result += dict[c]
    
    print(result[start_idx - 1:end_idx])

if __name__ == '__main__':
    main()