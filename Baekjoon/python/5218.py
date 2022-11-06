# source : https://www.acmicpc.net/problem/5218

for _ in range(int(input())):
    # input
    X, Y = input().split()
    
    distances = []
    for i in range(len(X)):
        x, y = ord(X[i]), ord(Y[i])
        
        if y >= x:
            distances.append(str(y - x))
        else:
            distances.append(str(y + 26 - x))
    
    print('Distances: ' + ' '.join(distances))