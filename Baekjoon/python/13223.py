# source : https://www.acmicpc.net/problem/13223

def main():
    # input
    sh, sm, ss = map(int, input().split(':'))
    eh, em, es = map(int, input().split(':'))
    
    start_sec = sh * 3600 + sm * 60 + ss
    end_sec = eh * 3600 + em * 60 + es
    
    if start_sec >= end_sec:
        result_sec = 24 * 3600 - start_sec + end_sec
    else:
        result_sec = end_sec - start_sec
        
    print('{0}:{1}:{2}'.format(
        str(result_sec // 3600).zfill(2),
        str((result_sec % 3600) // 60).zfill(2),
        str(result_sec % 60).zfill(2)
    ))

if __name__ == '__main__':
    main()