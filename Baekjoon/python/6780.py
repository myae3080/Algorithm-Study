# source : https://www.acmicpc.net/problem/6780

def main():
    # input
    t1, t2 = int(input()), int(input())
    
    result = [t1, t2]
    idx = 1
    while result[idx - 1] >= result[idx]:
        result.append(result[idx - 1] - result[idx])
        
        idx += 1
    
    print(len(result))

if __name__ == '__main__':
    main()