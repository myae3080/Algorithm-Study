# source : https://www.acmicpc.net/problem/14593

def main():
    # input
    participants_info = sorted([[i + 1] + list(map(int, input().split())) for i in range(int(input()))], key=lambda i: (-i[1], i[2], i[3]))
    
    print(participants_info[0][0])

if __name__ == '__main__':
    main()