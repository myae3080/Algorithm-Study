# source : https://www.acmicpc.net/problem/9421

def main():
    # input
    n = int(input())

    for num in range(7, n + 1):
        # check prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False

                break

        if is_prime:        
            # check happy number
            curr_num = num
            while 1:
                num_sum = sum([int(c) ** 2 for c in str(curr_num)])
                
                if num_sum == 1:
                    print(num)

                    break

                if num_sum == 4:
                    break

                curr_num = int(num_sum)

if __name__ == '__main__':
    main()