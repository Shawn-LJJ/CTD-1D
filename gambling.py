import random as rand

def gambling(timer):
    print("Let's go gambling")
    print("You have {}s left".format(timer))
    check = input("Do you want to gamble? (y/n):")
    
    while True:
        try:
            wager = int(input("How much you wanna risk?: "))
        except:
            print("Invalid input")
            continue
        else:
            if wager > timer or wager <= 0:
                print("Not enough")
                continue
            break

    if timer > 0 and str(check).upper() == 'Y':
        results = (rand.randint(0,3),rand.randint(0,3),rand.randint(0,3))
        print(results)
        if results[0] == results[1] and results[1] == results[2] and results[0] == results[2]:
            print("THE HERTA")
            #TODO ADD WIN CONDITION HERE
            timer += wager*0.5
        elif results[0] != results[1] and results[1] != results[2] and results[0] != results[2]:
            print("aw dangit")
            #TODO ADD LOSE CONDITION HERE
            timer = timer - wager
        else:
            print("pity")
            #TODO ADD PARTIAL WIN CONDITION HERE
            timer += wager*1
        print("Current timer is now: {}".format(timer))
    elif timer <= 0 and str(check).upper() == 'Y':
        print("Boohoo you're out of time you addict.")
    
    if(timer > 0):
        check = input("Do you want to continue? (y/n): ")
        if str(check).upper() == 'Y':
            gambling(timer)
        else:
            print("The herta is disappointed")
            return

        
gambling(69)