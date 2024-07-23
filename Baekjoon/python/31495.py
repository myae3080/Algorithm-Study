# source : https://www.acmicpc.net/problem/31495

def main():
    # input
    input_str = input()
    
    if input_str.count('"') < 2:
        print('CE')
        return
    
    if input_str[0] != '"' or input_str[-1] != '"':
        print('CE')
        return
    
    no_double_quotes_str = input_str.replace('"', '')
    if no_double_quotes_str == '':
        print('CE')
        return
    
    print(no_double_quotes_str)

if __name__ == '__main__':
    main()