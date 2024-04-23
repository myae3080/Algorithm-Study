# source : https://www.acmicpc.net/problem/17201

def main():
    # input
    n = int(input())
    magnatics = input()
    
    is_valid = True
    for i in range(1, (n * 2) - 1, 2):
        if magnatics[i] == magnatics[i + 1]:
            is_valid = False
            break
    
    print('Yes' if is_valid else 'No')

if __name__ == '__main__':
    main()