# source : https://www.acmicpc.net/problem/16017

def main():
    # input
    digits = [int(input()) for _ in range(4)]
    
    is_telemarketer = True
    if digits[0] not in [8, 9] or digits[3] not in [8, 9]:
        is_telemarketer = False
        
    if digits[1] != digits[2]:
        is_telemarketer = False
    
    print('ignore') if is_telemarketer else print('answer')

if __name__ == '__main__':
    main()