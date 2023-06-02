# source : https://www.acmicpc.net/problem/26264

def main():
    # input
    n = int(input())
    inputStr = input()
    
    se_cnt = inputStr.count('se')
    big_cnt = inputStr.count('big')
    
    print('bigdata? security!') if se_cnt == big_cnt else print('security!') if se_cnt >big_cnt else print('bigdata?')
    
if __name__ == '__main__':
    main()