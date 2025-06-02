# source : https://www.acmicpc.net/problem/33135

def main():
    # input
    S = input()
    
    print(len(S) - len(set(list(S))))

if __name__ == '__main__':
    main()