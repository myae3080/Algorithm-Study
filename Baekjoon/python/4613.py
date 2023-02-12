# source : https://www.acmicpc.net/problem/4613

def main():
    while 1:
        # input
        packet = input()
        
        if packet == '#':
            break
        
        quicksum = 0
        for i, c in enumerate(packet):
            code = ord(c)
            
            if code < 65:
                continue
            
            quicksum += (code - 64) * (i + 1)
            
        print(quicksum)

if __name__ == '__main__':
    main()