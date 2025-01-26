# source : https://www.acmicpc.net/problem/29699

def main():
    # input
    N = int(input())
    
    label = 'WelcomeToSMUPC'
    
    print(label[N % len(label) - 1])

if __name__ == '__main__':
    main()