strokes = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 3,
    'F': 3,
    'G': 3,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 3,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 2,
    'X': 2,
    'Y': 2,
    'Z': 1
}

# input
string = input()

nums = [strokes[s] for s in string]
while len(nums) > 1:
    temp = []  
    for i in range(0, len(nums), 2):
        sum_num = sum(nums[i:i + 2])
        if sum_num > 10:
            temp.append(sum_num % 10)
        else:
            temp.append(sum_num)
    
    nums = temp

print('I\'m a winner!') if nums[0] % 2 else print('You\'re the winner?')