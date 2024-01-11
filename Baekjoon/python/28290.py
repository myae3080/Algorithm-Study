# source : https://www.acmicpc.net/problem/28290

def main():
    dict = {
        'fdsajkl;': 'in-out',
        'jkl;fdsa': 'in-out',
        'asdf;lkj': 'out-in',
        ';lkjasdf': 'out-in',
        'asdfjkl;': 'stairs',
        ';lkjfdsa': 'reverse'
    }
    
    # input
    string = input()
    
    print(dict[string] if string in dict.keys() else 'molu')

if __name__ == '__main__':
    main()