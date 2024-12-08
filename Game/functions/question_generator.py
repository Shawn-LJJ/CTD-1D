import random
import operator

# fight type : (lower bound, upper bound, bias for add/sub question)
TYPES = {
    'battle' : (1, 20, 0.8),
    'elite' : (5, 40, 0.7),
    'boss' : (10, 100, 0.5)
}

def main(fight_type :str, bound_boost:float, operator_bias_boost:float):
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/' , operator.truediv)]
    operator_bias = TYPES[fight_type][2] * operator_bias_boost

    # prevent bias from reaching over 1
    operator_bias = 1 if operator_bias > 1 else operator_bias

    # weights for [add, sub, mul, div]
    operators_weights = [operator_bias, operator_bias, 1 - operator_bias, 1 - operator_bias]

    lower_bound = TYPES[fight_type][0]
    upper_bound = round(TYPES[fight_type][1] * bound_boost)

    # prevent upper bound from going lower than the lower bound
    if upper_bound <= lower_bound:
        upper_bound = lower_bound + 1

    ran1 = random.randint(lower_bound, upper_bound)
    ran2 = random.randint(lower_bound, upper_bound)
    op, fn = random.choices(operators, weights=operators_weights)[0]

    correctans = round(fn(ran1, ran2), 2)  # Rounded to 2 decimal places for division
    question = f"{ran1} {op} {ran2}"
    print(question)
    return correctans