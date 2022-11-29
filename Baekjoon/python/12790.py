# source : https://www.acmicpc.net/problem/12790

for _ in range(int(input())):
    # input
    hp, mp, att, defence, equip_hp, equip_mp, equip_att, equip_defence = map(int, input().split())

    new_hp = 1 if hp + equip_hp < 1 else hp + equip_hp
    new_mp = 1 if mp + equip_mp < 1 else mp + equip_mp
    new_att = 0 if att + equip_att < 0 else att + equip_att
    new_defence = defence + equip_defence

    print(new_hp + (5 * new_mp) + (2 * new_att) + (2 * new_defence))