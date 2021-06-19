# string, recursion

def recursive_func(num_str, count):
    length = len(num_str)

    if length == 1:
        print(count)
        if int(num_str) % 3 == 0:
            print('YES')
        else:
            print('NO')
    else:
        count += 1
        total = 0

        for s in num_str:
            total += int(s)
        
        recursive_func(str(total), count)

# input
recursive_func(input(), 0)