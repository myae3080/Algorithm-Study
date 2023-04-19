# source : https://www.acmicpc.net/problem/25206

def main():
    grades = {
        'A+': 4.5,
        'A0': 4.0,
        'B+': 3.5,
        'B0': 3.0,
        'C+': 2.5,
        'C0': 2.0,
        'D+': 1.5,
        'D0': 1.0,
        'F': 0.0,
    }
    
    scores, credits = 0, 0
    for _ in range(20):
        # input
        subject, credit, grade = input().split()
        
        if grade == 'P':
            continue    
        else:
            scores += (float(credit) * grades[grade])
            credits += float(credit)
    
    print('{:.6f}'.format(round(scores / credits, 6)))
        

if __name__ == '__main__':
    main()