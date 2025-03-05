# source : https://www.acmicpc.net/problem/3226

def main():
    # input
    N = int(input())
    
    fee = 0
    for _ in range(N):
        # input
        HHMM, DD = input().split()
        
        HH, MM = map(int, HHMM.split(':'))
        if 7 <= HH < 19:
            if HH == 18:
                if MM + int(DD) <= 60:
                    fee += int(DD) * 10
                else:
                    fee += ((60 - MM) * 10 + ((MM + int(DD)) - 60) * 5)
            else:
                fee += int(DD) * 10
        else:
            if HH == 6:
                if MM + int(DD) <= 60:
                    fee += int(DD) * 5
                else:
                    fee += ((60 - MM) * 5 + (MM + int(DD) - 60) * 10)
            else:
                fee += int(DD) * 5
        
    print(fee)

if __name__ == '__main__':
    main()