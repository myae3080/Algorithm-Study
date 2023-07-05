# source : https://www.acmicpc.net/problem/28074

def main():
    # input
    word = input()
    
    for c in 'MOBIS':
        if word.count(c) == 0:
            return 'NO'
        
    return 'YES'

if __name__ == '__main__':
    print(main())