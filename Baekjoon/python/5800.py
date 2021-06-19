# sorting

for i in range(int(input())):
    # input
    input_list = list(map(int, input().split()))
    n = input_list[0]
    
    score_list = sorted(input_list[1:], reverse=True)
    max_num = 0

    for j in range(n - 1):
        max_num = max(max_num, score_list[j] - score_list[j + 1])


    print('Class', i + 1)
    print('Max', str(score_list[0]) + ',', 'Min', str(score_list[-1]) + ',', 'Largest gap', max_num)