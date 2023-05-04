# source : https://www.acmicpc.net/problem/15820

def main():
    # input
    s1, s2 = map(int, input().split())

    for _ in range(s1):
        # input
        sample_answer, answer = map(int, input().split())

        if sample_answer != answer:
            return 'Wrong Answer'

    for _ in range(s2):
        # input
        system_answer, answer = map(int, input().split())

        if system_answer != answer:
            return 'Why Wrong!!!'

    return 'Accepted'

if __name__ == '__main__':
    print(main())