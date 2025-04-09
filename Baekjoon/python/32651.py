# source : https://www.acmicpc.net/problem/32651

def main():
    # input
    N = int(input())
    
    if N > 100000:
        print('No')
        
        return

    print('Yes' if N % 2024 == 0 else 'No')

if __name__ == '__main__':
    main()