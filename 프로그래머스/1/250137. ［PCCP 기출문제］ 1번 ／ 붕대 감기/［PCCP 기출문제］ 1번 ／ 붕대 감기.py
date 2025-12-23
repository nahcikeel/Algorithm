def solution(bandage, health, attacks):
    t, heal, bonus = bandage
    max_hp = health
    hp = health

    combo = 0
    attack_idx = 0

    last_time = attacks[-1][0]

    for time in range(1, last_time + 1):
        # 공격이 있는 시간인지 확인
        if attack_idx < len(attacks) and attacks[attack_idx][0] == time:
            dmg = attacks[attack_idx][1]
            hp -= dmg
            combo = 0
            attack_idx += 1

            if hp <= 0:
                return -1
        else:
            # 붕대 감기 성공
            combo += 1
            hp = min(max_hp, hp + heal)

            if combo == t:
                hp = min(max_hp, hp + bonus)
                combo = 0

    return hp
