# source : https://www.acmicpc.net/problem/3449

for _ in range(int(input())):
    # input
    a, b = input(), input()
    
    print('Hamming distance is {0}.'.format(len([1 for i in range(len(a)) if a[i] != b[i]])))