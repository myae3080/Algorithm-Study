# source : https://www.acmicpc.net/problem/7513

def main():
    # input
    t = int(input())
    
    for i in range(1, t + 1):
        # input
        words = [input() for _ in range(int(input()))]
        
        print('Scenario #%d:' % i)
        
        # input
        for _ in range(int(input())):
            # input
            pw_info = list(map(int, input().split()))

            print(''.join([words[idx] for idx in pw_info[1:]]))
        
        print()

if __name__ == '__main__':
    main()