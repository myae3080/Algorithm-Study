# source : https://www.acmicpc.net/problem/27494

def main():
    # input
    n = int(input())
    
    result = 0
    for i in range(2023, n + 1):
        result += checkTicket(str(i), 0)

    print(result)

def checkTicket(serial: str, i: int) -> int:
    target = '2023'
    if target[i] in serial:
        if i == 3:
            return 1
        else:
            return checkTicket(serial[serial.index(target[i]):], i + 1)
    
    return 0

if __name__ == '__main__':
    main()