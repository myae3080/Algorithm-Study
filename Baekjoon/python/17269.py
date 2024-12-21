# source : https://www.acmicpc.net/problem/17269

def main():
    # input
    N, M = map(int, input().split())
    A, B = input().split()
    
    strokes = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    
    min_num = min(N, M)
    name_compatibility = ''
    for i in range(min_num):
        name_compatibility += str(strokes[ord(A[i]) - 65])
        name_compatibility += str(strokes[ord(B[i]) - 65])
    
    if len(A) > len(B):
        for c in A[min_num:]:
            name_compatibility += str(strokes[ord(c) - 65])
    else:
        for c in B[min_num:]:
            name_compatibility += str(strokes[ord(c) - 65])
    
    while len(name_compatibility) > 2:
        curr_compatibility = ''
        for i in range(1, len(name_compatibility)):
            curr_compatibility += str((int(name_compatibility[i - 1]) + int(name_compatibility[i])) % 10)
        
        name_compatibility = curr_compatibility
    
    print('%d%%' % int(name_compatibility))

if __name__ == '__main__':
    main()