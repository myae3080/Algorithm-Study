# source : https://www.acmicpc.net/problem/32969

def main():
    # input
    title = input()
    
    for word in ['bigdata', 'public', 'society']:
        if word in title:
            print('public bigdata')
            
            return
    
    print('digital humanities')

if __name__ == '__main__':
    main()