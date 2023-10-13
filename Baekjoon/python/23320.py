# source : https://www.acmicpc.net/problem/23320

def main():
    # input
    n = int(input())
    scores = list(map(int, input().split()))
    proportion, min_score = map(int, input().split())
    
    print(n * proportion // 100, len([score for score in scores if score >= min_score]))
    
if __name__ == '__main__':
    main()