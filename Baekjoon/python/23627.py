# source : https://www.acmicpc.net/problem/23627

def main():
    # input
    string = input()
    
    if len(string) < 5:
        print('not cute')
    else:
        print('cute' if string[-5:] == 'driip' else 'not cute')

if __name__ == '__main__':
    main()