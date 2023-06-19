# source : https://www.acmicpc.net/problem/6764

def main():
    # input
    depth = [int(input()) for _ in range(4)]
    
    asc = sorted(depth)
    desc = sorted(depth, reverse=True)
    
    if len(set(depth)) == 1:
        print('Fish At Constant Depth')
    elif len(set(depth)) < 4:
        print('No Fish')
    elif depth == asc:
        print('Fish Rising')
    elif depth == desc:
        print('Fish Diving')
    else:
        print('No Fish')
    
if __name__ == '__main__':
    main()