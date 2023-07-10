# source : https://www.acmicpc.net/problem/20492

def main():
    # input
    reward = int(input())
    
    print(int(reward * 0.78), int(reward * 0.8 + reward * 0.2 * 0.78))
    
if __name__ == '__main__':
    main()