# source : https://www.acmicpc.net/problem/10823

def main():
    S = ''
    while 1:
        try:
            S += input()
        except:
            break
    
    print(sum(list(map(int, S.split(',')))))

if __name__ == '__main__':
    main()