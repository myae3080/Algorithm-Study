# source : https://www.acmicpc.net/problem/2851

# input
mushrooms = [int(input()) for _ in range(10)]

result = 0

for i, mushroom in enumerate(mushrooms):
    expectation = result + mushroom
    
    if expectation == 100:
        print(expectation)
        break
    else:
        if abs(100 - result) < abs(100 - expectation):
            print(result)
            break
        else:
            result = expectation
            
            if i == 9:
                print(result)