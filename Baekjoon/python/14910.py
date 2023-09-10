# source : https://www.acmicpc.net/problem/14910

def main():
    # input
    sequence = list(map(int, input().split()))
    
    if len(sequence) == 1:
        print('Good')
    else:
        is_asc = True
        for i in range(1, len(sequence)):
            if sequence[i - 1] > sequence[i]:
                is_asc = False
                break
        
        print('Good' if is_asc else 'Bad')
    
if __name__ == '__main__':
    main()