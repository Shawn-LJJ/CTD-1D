from Game.map import Map
from Game.functions.async_input import main as input_w_timer
from Game.functions.question_generator import main as question_gen
from Game.functions.buff_generator import main as buff_gen
from Game.functions.gambling import main as gambling
import asyncio
import os
import random

cmd_clear = 'cls' if os.name == 'nt' else 'clear'

class Logic():
    def __init__(self) -> None:
        # player data
        self.stage = 'A0'
        self.map = Map()
        self.time = 30
        self.positive_event_prob = 0.5

        # multiplier
        # {'fight type' : [random number upper bound limit boost, add/sub operator bias]}
        self.fight_boosts = {
            'battle' : [1, 1],
            'elite' : [1, 1],
            'boss' : [1, 1]
        }

        # stats
        self.num_of_fights = 0
        self.num_of_victory = 0
        self.buffs = []
    
    # the actual game logic in place
    def start(self) -> None:

        while True:

            # draw the map
            self.map.draw_map()
            self.map.draw_map_movement()

            # prompt for user input for movement and then get the action
            action = self.map.move()

            # assign time bonus if win/lose, and determine the fight duration
            if action == 'battle':
                time_bonus = 5
                time_needed = 10
            elif action == 'elite':

                while True:
                    try:
                        time_bonus = input(f'Enter the amount of time you want to wager (Max: {self.time} seconds): ')
                        if not time_bonus.isdigit():
                            raise   # invalid if it contains something that is not a digit

                        time_bonus = int(time_bonus)

                        # wagered time must not exceed total time player has
                        if time_bonus > self.time:
                            print('\nError, time wagered exceeds total time')
                        else:
                            break
                    except:
                        print('\nInvalid wager time')
                
                time_needed = 15
            
            elif action == 'boss':
                time_needed = self.time
            
            # check which domain is activated and see what action to do
            if action == 'occurence':
                buff_or_debuff = 'buff' if random.random() < self.positive_event_prob else 'debuff'
                print('Congrats, you can choose a buff' if buff_or_debuff == 'buff' else 'Too bad, you must choose a debuff')
                buffs = buff_gen(buff_or_debuff, 3)

                while True:
                    try:
                        print(f'\nYour available {buff_or_debuff}: ')
                        for i in range(len(buffs)):
                            print(f'{i + 1}. {buffs[i]}')
                        print('4. Gambling.')
                        buff_input = input(f'\nChoose your option: ')

                        user_option = int(buff_input)
                        if user_option != 4:
                            chosen_buff = buffs[int(buff_input) - 1]
                        else:
                            chosen_buff = None
                        break
                    except:
                        print(f'\nInvalid {buff_or_debuff} option.')
                
                if chosen_buff is None:
                    outcome, wager = gambling(self.time)
                    self.time += wager

                    if outcome == 'win':
                        print(f'Due to your big win with 3 matches, you have added {wager} seconds into your boss fight time and you get to choose a buff.')
                        print(f'Your new boss fight time: {self.time} seconds.')
                        buffs = buff_gen('buff', 3)
                        while True:
                            try:
                                print('\nYour available buff after gambling: ')
                                for i in range(len(buffs)):
                                    print(f'{i + 1}. {buffs[i]}')
                                buff_input = input(f'\nChoose your option: ')
                                chosen_buff = buffs[int(buff_input) - 1]
                                break
                            except:
                                print(f'\nInvalid buff option.')
                    
                    elif outcome == 'partial':
                        print(f'With only 2 matches, you had added {wager} seconds into your boss fight with no buff/debuff.')
                        print(f'Your new boss fight time: {self.time} seconds.')
                        input('Press enter to continue...')
                        continue

                    else:
                        print(f'You had lost the gambling. You lost {wager} seconds of boss fight and you have to pick a debuff.')
                        print(f'Your new boss fight time: {self.time} seconds.')
                        buffs = buff_gen('debuff', 3)
                        while True:
                            try:
                                print('\nYour available debuff after gambling: ')
                                for i in range(len(buffs)):
                                    print(f'{i + 1}. {buffs[i]}')
                                buff_input = input(f'\nChoose your option: ')
                                chosen_buff = buffs[int(buff_input) - 1]
                                break
                            except:
                                print(f'\nInvalid debuff option.')

                buff_name, buff_value = list(chosen_buff.items())[0]

                if buff_name == 'time':
                    self.time += buff_value

                elif buff_name == 'positive_event_prob':
                    self.positive_event_prob += buff_value

                else:
                    fight_type, mul_type, _ = buff_name.split('_')
                    mul_type = 0 if mul_type == 'upper' else 1

                    self.fight_boosts[fight_type][mul_type] += buff_value

                    if self.fight_boosts[fight_type][mul_type] < 0:
                        self.fight_boosts[fight_type][mul_type] = 0

                print(self.fight_boosts)
                print(self.time)
                input('Press enter to continue...')

            else:
                
                answer = question_gen(action, self.fight_boosts[action][0], self.fight_boosts[action][1])
                # fight the enemy/boss
                user_input = asyncio.run(input_w_timer(time_needed))

                os.system(cmd_clear)
                if user_input is not None:
                    print(f'Your answer is {user_input}.')

                    try:

                        if float(user_input) == answer:
                            print('You are correct!')
                            self.num_of_victory += 1

                            if action == 'battle' or action == 'elite':
                                print(f'You had awarded an additional {time_bonus} seconds for your boss fight!')
                                self.time += time_bonus
                                print(f'Your new boss time fight is now {self.time} seconds.')
                            
                            elif action == 'boss':
                                print('You have finally defeated the boss!')
                        
                        else:
                            raise
                    
                    except:
                        print(f'You are wrong. The correct answer is {answer}')

                        if action == 'elite':
                            print(f'You had lost your wager and will lose {time_bonus} seconds.')
                            self.time -= time_bonus
                            print(f'Your new boss time fight is now {self.time} seconds.')
                        
                        elif action == 'boss':
                            print('Game over!')

                    input('Press enter to continue...')
                
                self.num_of_fights += 1

            os.system(cmd_clear)
            if action == 'boss':
                break