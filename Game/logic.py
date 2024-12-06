from Game.map import Map
from Game.async_input import main as input_w_timer
from time import sleep
import asyncio

class Logic():
    def __init__(self) -> None:
        self.stage = 'A0'
        self.map = Map()
        self.time = 180
    
    # the actual game logic in place
    def start(self) -> None:

        while True:

            # draw the map
            self.map.draw()

            # get next possible moves
            possible_moves = self.map.get_next_possible_pos()

            # wait for user input for selecting node and validate for where the player can go next (reprompt if is an invalid option)
            while True:
                # prompt and validate
                print(f'\nYour next available move choice: {", ".join(possible_moves)}')
                userInput = input('Pick your next move: ').strip().upper()
                if userInput in possible_moves:
                    break
                print('\nInvalid move')
                sleep(0.5)

            # move to the new position
            self.map.update(userInput)

            # get list of possible actions
            possible_actions = self.map.get_actions()

            # fight the enemy/boss
            user_input = asyncio.run(input_w_timer(3))
            print(user_input)

            # if defeated an enemy, then reward something, and unlock new path
            # if defeated a boss, game ends

            # but if an enemy/boss is undefeated, then how?

            break