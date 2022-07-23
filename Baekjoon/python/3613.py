# source : https://www.acmicpc.net/problem/3613

# input
input_str = input()

result = ""

if not input_str[0].islower() or input_str[-1] == '_':
    result = 'Error!'
else:
    # to cpp
    if input_str.find("_") == -1:
        for c in input_str:
            if c.isupper():
                result += "_" + c.lower()
            elif c == "_":
                result = "Error!"
                break
            else:
                result += c
    # to java
    else:
        to_upper = False
        
        for i in range(len(input_str)):
            c = input_str[i]
            
            if c == "_":
                if input_str[i + 1] == '_':
                    result = 'Error!'
                    break
                else:
                    to_upper = True
            elif c.isupper():
                result = "Error!"
                break
            else:
                if to_upper:
                    result += c.upper()
                    to_upper = False
                else:
                    result += c
                    
print(result)