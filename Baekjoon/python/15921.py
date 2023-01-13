# source : https://www.acmicpc.net/problem/15921

# input
n = int(input())

if not n:
    print('divide by zero')
else:
    # input
    records = list(map(int, input().split()))

    avg = sum(records) / n
    count_by_records = {}
    for record in records:
        if record not in count_by_records:
            count_by_records[record] = 1
        else:
            count_by_records[record] += 1

    expected_val = 0
    for key, val in count_by_records.items():
        expected_val += key * (val / n)
        
    if not expected_val:
        print('divide by zero')
    else:
        print('{:.2f}'.format(round(avg / expected_val, 3)))