from time import sleep
from Game.logic import Logic

class Game():

    def start_menu(self) -> None:
        
        choice = None

        while choice != '2':
            
            print('\n1. Start game\n2. Exit')
            choice = input('>> ').strip()

            if choice == '1':
                self.game = Logic()
                self.game.start()
            elif choice != '2': 
                print('\nInvalid option')
                sleep(0.5)