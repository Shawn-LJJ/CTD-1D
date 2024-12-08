import random as rand

def main(timer):
    print("Let's go gambling")
    
    while True:
        try:
            wager = int(input("How much you wanna risk?: "))
        except:
            print("Invalid input")
            continue
        else:
            if wager > timer:
                print("Not enough")
                continue
            break
    
    input('Press enter to gamble...')
    results = (rand.randint(0,3),rand.randint(0,3),rand.randint(0,3))
    print(results)
    if results[0] == results[1] and results[1] == results[2] and results[0] == results[2]:
        print("THE HERTA")
        return ('win', wager * 2)
    elif results[0] != results[1] and results[1] != results[2] and results[0] != results[2]:
        print("aw dangit")
        return ('lose', -1 * wager)
    else:
        print("pity")
        return ('partial', wager)
    