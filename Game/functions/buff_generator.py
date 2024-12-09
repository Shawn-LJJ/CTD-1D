import random
from numpy.random import choice

BUFFS = {
    'time' : lambda : random.randint(1, 15), 
    'positive_event_prob' : lambda : round(random.random() * 0.1, 2), 
    'battle_upper_bound' : lambda : round(random.random() * -0.1, 2),
    'battle_operator_bias' : lambda : round(random.random() * 0.1, 2),
    'elite_upper_bound' : lambda : round(random.random() * -0.2, 2),
    'elite_operator_bias' : lambda : round(random.random() * 0.12, 2),
    'boss_upper_bound' : lambda : round(random.random() * -0.3, 2),
    'boss_operator_bias' : lambda : round(random.random() * 0.15, 2)
}

BUFFS_NAME = {
    'time' : 'Time gained/lost', 
    'positive_event_prob' : 'Positive event probability', 
    'battle_upper_bound' : 'Battle math number range',
    'battle_operator_bias' : 'Battle addition/subtraction operator probability',
    'elite_upper_bound' : 'Elite math number range',
    'elite_operator_bias' : 'Elite addition/subtraction operator probability',
    'boss_upper_bound' : 'Boss math number range',
    'boss_operator_bias' : 'Boss addition/subtraction operator probability'
}

def main(buff_or_debuff, num = 1) -> list:
    buffs = choice(list(BUFFS.keys()), size=num, replace=False)
    final_buffs = []
    for buff in buffs:
        final_buffs.append({buff : BUFFS[buff]() if buff_or_debuff == 'buff' else -1 * BUFFS[buff]()})
    return final_buffs