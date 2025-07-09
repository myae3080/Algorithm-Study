# source : https://www.acmicpc.net/problem/2212

def main():
    # input
    N, K = int(input()), int(input())
    sensors = list(map(int, input().split()))
    
    sensors.sort()
    
    sensor_distance = []
    for i in range(1, N):
        sensor_distance.append(sensors[i] - sensors[i - 1])
    
    sensor_distance.sort()
    
    print(sum(sensor_distance[:N - K]))

if __name__ == '__main__':
    main()