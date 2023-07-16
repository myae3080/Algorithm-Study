# source : https://www.acmicpc.net/problem/17450

def main():
    values = []
    for _ in range(3):
        # input
        price, weight = map(int, input().split())
        
        values.append((weight * 10) / (price * 10 - 500 if price * 10 >= 5000 else price * 10))
        
    best_value_idx = values.index(max(values))
    if best_value_idx == 0:
        print('S')
    elif best_value_idx == 1:
        print('N')
    else:
        print('U')
    
if __name__ == '__main__':
    main()