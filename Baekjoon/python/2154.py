# source : https://www.acmicpc.net/problem/2154

def main():
    # input
    n = int(input())
    
    num_str = ''
    for i in range(1, n + 1):
        num_str += str(i)
        
    print(num_str.index(str(n)) + 1)

if __name__ == '__main__':
    main()