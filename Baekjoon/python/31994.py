# source : https://www.acmicpc.net/problem/31994

def main():
    requests = []
    
    for _ in range(7):
        # input
        semina, people = input().split()
        
        requests.append((semina, int(people)))
    
    requests.sort(key=lambda info: -info[1])
    
    print(requests[0][0])

if __name__ == '__main__':
    main()