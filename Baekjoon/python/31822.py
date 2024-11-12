# source : https://www.acmicpc.net/problem/31822

def main():
    # input
    re_subject = input()
    
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        subject = input()
        
        if re_subject[:5] == subject[:5]:
            result += 1

    print(result)

if __name__ == '__main__':
    main()