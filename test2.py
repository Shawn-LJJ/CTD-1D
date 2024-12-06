import random
import operator

def questiongenhard(buffs):
    a = 100
    b = 100
    for buff in buffs['question_diff']:
        a * buff
        b * buff
    d = {'question_diff' : [], 'timing' : []}
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/' , operator.truediv)]
    ran1 = random.randint(10, a)
    ran2 = random.randint(10, b)
    op, fn = random.choice(operators)

    correctans = round(fn(ran1, ran2), 2)  # Rounded to 2 decimal places for division
    question = f"{ran1} {op} {ran2}"
    print(question)
    return correctans

def checkans(userguess, correctans):
    if userguess == correctans:
        return "correct"
    else:
        return "wrong"

# Main game loop for 10 cycles
score = 0
for i in range(10):
    print(f"Question {i+1}:")
    correctans = questiongenhard()
    try:
        userguess = float(input("Enter your answer: "))  # Allow decimals for division answers
        print(f"You guessed: {userguess}")
        if checkans(userguess, correctans) == "correct":
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correctans}")
    except ValueError:
        print("Invalid input! Skipping this question.")
    print("-" * 20)

print(f"Game over! Your final score is: {score}/10")