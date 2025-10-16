# source : https://www.acmicpc.net/problem/33937

def main():
    # input
    A, B = input(), input()

    a = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(1, len(A)):
        if A[i] not in vowels and A[i - 1] in vowels:
            a = A[:i]

            break
    
    if a == '':
        print('no such exercise')

        return
    
    b = ''
    for j in range(1, len(B)):
        if B[j] not in vowels and B[j - 1] in vowels:
            b = B[:j]

            break
    
    if b == '':
        print('no such exercise')

        return

    print(a + b)

if __name__ == '__main__':
    main()