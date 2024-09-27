# source : https://www.acmicpc.net/problem/20949

def main():
    monitor_info = []
    
    # input
    for i in range(1, int(input()) + 1):
        # input
        W, H = map(int, input().split())
        
        monitor_info.append((i, W ** 2 + H ** 2))
    
    for info in sorted(monitor_info, key=lambda info: (-info[1], info[0])):
        print(info[0])

if __name__ == '__main__':
    main()