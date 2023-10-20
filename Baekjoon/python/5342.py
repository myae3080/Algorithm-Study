# source : https://www.acmicpc.net/problem/5342

def main():
    costs = {
        'Paper': 57.99,    
        'Printer': 120.50,    
        'Planners': 31.25,    
        'Binders': 22.50,    
        'Calendar': 10.95,    
        'Notebooks': 11.20,    
        'Ink': 66.95,    
    }
    
    total = 0
    while 1:
        # input
        supply = input()
        
        if supply == 'EOI':
            break
        
        total += costs[supply]
    
    print('$' + str(round(total, 2)))

if __name__ == '__main__':
    main()