# source : https://www.acmicpc.net/problem/2596

def main():
    # input
    n = int(input())
    string = input()
    
    translation = {
        '000000': 'A'
        , '001111': 'B'
        , '010011': 'C'
        , '011100': 'D'
        , '100110': 'E'
        , '101001': 'F'
        , '110101': 'G'
        , '111010': 'H'
    }
    
    result = ''
    for i in range(0, n * 6, 6):
        curr_str = string[i:i + 6]
        
        is_no_found = True
        for t in translation.keys():
            diff = 0
            for j in range(6):
                if curr_str[j] != t[j]:
                    diff += 1
                
                if diff > 1:
                    break
            
            if diff < 2:
                is_no_found = False
                result += translation[t]
                break
        
        if is_no_found:
            result = str(int((i / 6) + 1))
            break
    
    print(result)

if __name__ == '__main__':
    main()