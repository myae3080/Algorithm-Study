# source : https://www.acmicpc.net/problem/4539

def main():
    # input
    for _ in range(int(input())):
        # input
        num = input()
        
        if len(num) == 1:
            print(num)
            continue
        
        result = []
        round_up = 0
        for i in range(len(num) - 1, -1, -1):
            if i == 0:
                result.append(str(int(num[i]) + round_up))
            else:
                curr_num = int(num[i]) + round_up
                if curr_num >= 5:
                    round_up = 1
                else:
                    round_up = 0
                
                result.append('0')
        
        print(''.join(result[::-1]))

if __name__ == '__main__':
    main()