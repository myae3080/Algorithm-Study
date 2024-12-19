# source : https://www.acmicpc.net/problem/15312

def main():
    strokes = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    
    # input
    A, B = input(), input()
    
    name_compatibility = []
    for i in range(len(A)):
        name_compatibility += [strokes[ord(A[i]) - 65], strokes[ord(B[i]) - 65]]
    
    while len(name_compatibility) > 2:
        curr_compatibility = []
        for i in range(1, len(name_compatibility)):
            curr_compatibility.append((name_compatibility[i - 1] + name_compatibility[i]) % 10)
        
        name_compatibility = curr_compatibility
    
    print(''.join([str(n) for n in name_compatibility]))

if __name__ == '__main__':
    main()