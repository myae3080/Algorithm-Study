# source : https://www.acmicpc.net/problem/17293

def main():
    # input
    n = int(input())
    
    for i in range(n, -1, -1):
        if i >= 3:
            print('%d bottles of beer on the wall, %d bottles of beer.\nTake one down and pass it around, %d bottles of beer on the wall.' % (i, i, i - 1))
        elif i == 2:
            print('%d bottles of beer on the wall, %d bottles of beer.\nTake one down and pass it around, %d bottle of beer on the wall.' % (i, i, i - 1))
        elif i == 1:
            print('%d bottle of beer on the wall, %d bottle of beer.\nTake one down and pass it around, %s bottles of beer on the wall.' % (i, i, 'no more'))
        else:
            if n == 1:
                print('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, %d bottle of beer on the wall.' % n)
            else:
                print('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, %d bottles of beer on the wall.' % n)
        
        print()

if __name__ == '__main__':
    main()