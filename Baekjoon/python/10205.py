# source : https://www.acmicpc.net/problem/10205

def main():
    # input
    for i in range(int(input())):
        # input
        heads = int(input())
        actions = input()
        
        heads += actions.count('c') - actions.count('b')
        
        print('Data Set {idx}:'.format(idx = i + 1))
        print(0) if heads < 0 else print(heads)
        print()
                
if __name__ == '__main__':
    main()