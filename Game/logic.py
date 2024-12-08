from Game.map import Map
from Game.functions.async_input import main as input_w_timer
from Game.functions.question_generator import main as question_gen
import asyncio
import os

cmd_clear = 'cls' if os.name == 'nt' else 'clear'

class Logic():
    def __init__(self) -> None:
        self.stage = 'A0'
        self.map = Map()
        self.time = 180

        # boost
        # {'fight type' : [random number upper bound limit boost, add/sub operator bias]}
        self.fight_boosts = {
            'battle' : [1, 1],
            'elite' : [1, 1],
            'boss' : [1, 1]
        }

        # stats
        self.num_of_fights = 0
        self.num_of_victory = 0
    
    # the actual game logic in place
    def start(self) -> None:

        while True:

            # draw the map
            self.map.draw_map()
            self.map.draw_map_movement()

            # prompt for user input for movement and then get the action
            action = self.map.move()
            
            # check which domain is activated and see what action to do
            if action == 'occurence':
                pass

            else:
                
                answer = question_gen(action, self.fight_boosts[action][0], self.fight_boosts[action][1])
                # fight the enemy/boss
                user_input = asyncio.run(input_w_timer(10))

                os.system(cmd_clear)
                if user_input is not None:
                    print(f'Your answer is {user_input}')
                    print('But you are correct/wrong')
                    input('Press enter to continue...')

            # if defeated an enemy, then reward something, and unlock new path
            # if defeated a boss, game ends

            # but if an enemy/boss is undefeated, then how?

            os.system(cmd_clear)
            if action == 'boss':
                break