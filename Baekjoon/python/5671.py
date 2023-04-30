# source : https://www.acmicpc.net/problem/5671

def main():
    while 1:
        try:
            # input
            n, m = map(int, input().split())
            
            result = 0
            for i in range(n, m + 1):
                room_number = str(i)
                is_valid = True
                
                for digit in room_number:
                    if room_number.count(digit) > 1:
                        is_valid = False
                        break
                
                if is_valid:
                    result += 1
            
            print(result)
        except EOFError:
            break
    
if __name__ == '__main__':
    main()