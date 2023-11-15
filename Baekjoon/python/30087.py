# source : https://www.acmicpc.net/problem/30087

semina_by_room = {
    'Algorithm': '204',
    'DataAnalysis': '207',
    'ArtificialIntelligence': '302',
    'CyberSecurity': 'B101',
    'Network': '303',
    'Startup': '501',
    'TestStrategy': '105'
}

def main():
    # input
    n = int(input())
    seminas = [input() for _ in range(n)]
    
    for semina in seminas:
        print(semina_by_room[semina])

if __name__ == '__main__':
    main()