# source : https://www.acmicpc.net/problem/28249

def main():
    scolville_units = {
        'Poblano': 1500
        , 'Mirasol': 6000
        , 'Serrano': 15500
        , 'Cayenne': 40000
        , 'Thai': 75000
        , 'Habanero': 125000
    }
    
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        result += scolville_units[input()]

    print(result)

if __name__ == '__main__':
    main()