# source : https://www.acmicpc.net/problem/20977

'''
    J O I 순서로 정렬되어야 하는 관계로
    string 의 count 함수를 이용해 결과 출력.
'''

def main():
    # input
    N = int(input())
    S = input()
    
    print('J' * S.count('J') + 'O' * S.count('O') + 'I' * S.count('I'))

if __name__ == '__main__':
    main()