# source : https://www.acmicpc.net/problem/25841

def main():
    # input
    a, b, target = input().split()
    
    result = 0
    for n in range(int(a), int(b) + 1):
        result += str(n).count(str(target))
    
    print(result)
    
if __name__ == '__main__':
    main()