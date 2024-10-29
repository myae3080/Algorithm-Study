# source : https://www.acmicpc.net/problem/24606

def main():
    # input
    pw1, pw2 = input(), input()
    
    diff = 0
    for i in range(len(pw1)):
        if pw1[i] != pw2[i]:
            diff += 1
    
    print(2 ** diff)

if __name__ == '__main__':
    main()