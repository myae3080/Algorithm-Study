# source : https://www.acmicpc.net/problem/17598

def main():
    lion_cnt = 0
    for _ in range(9):
        # input
        if input() == 'Lion':
            lion_cnt += 1
    
    print('Lion' if lion_cnt >= 5 else 'Tiger')

if __name__ == '__main__':
    main()