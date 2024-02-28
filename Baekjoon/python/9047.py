# source : https://www.acmicpc.net/problem/9047

def main():
    # input
    for _ in range(int(input())):
        # input
        num = input()
                
        result = 0
        while num != '6174':
            result += 1
            
            max_num = ''.join(sorted(list(num), reverse=True))
            min_num = max_num[::-1]
            
            num = str(int(max_num) - int(min_num))
            
            if len(num) < 4:
                zeros = ''
                for _ in range(4 - len(num)):
                    zeros += '0'
                
                num = zeros + num
            
        print(result)

if __name__ == '__main__':
    main()