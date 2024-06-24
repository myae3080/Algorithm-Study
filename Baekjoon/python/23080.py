# source : https://www.acmicpc.net/problem/23080

def main():
    # input
    k = int(input())
    cryptogram = input()
    
    print(''.join([cryptogram[i] for i in range(0, len(cryptogram), k)]))

if __name__ == '__main__':
    main()