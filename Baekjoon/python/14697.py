# source : https://www.acmicpc.net/problem/14697

def main():
    # input
    room_a, room_b, room_c, students = map(int, input().split())
    
    if room_a == 1:
        print(1)
    else:
        is_possible = False
        for a in range(students // room_a + 1):
            if is_possible:
                break
            
            for b in range(students // room_b + 1):
                if is_possible:
                    break
                
                for c in range(students // room_c + 1):
                    if (room_a * a) + (room_b * b) + (room_c * c) > students:
                        break
                    
                    if (room_a * a) + (room_b * b) + (room_c * c) == students:
                        print(1)
                        is_possible = True
                        break
                    
        if not is_possible:
            print(0)
    
if __name__ == '__main__':
    main()