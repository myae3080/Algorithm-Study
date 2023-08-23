# source : https://www.acmicpc.net/problem/28431

def main():
    # input
    socks = [input() for _ in range(5)]
    
    for sock in socks:
        if socks.count(sock) % 2 == 1:
            print(sock)
            break

if __name__ == '__main__':
    main()