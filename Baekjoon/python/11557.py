# source : https://www.acmicpc.net/submit/11557
# sorting

for _ in range(int(input())):
    school_list = []

    for __ in range(int(input())):
        # input
        a, b = input().split()

        school_list.append([a, int(b)])        
    
    school_list.sort(key=lambda x: -x[1])

    print(school_list[0][0])