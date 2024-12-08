from Game.room_maker import RoomMaker

class Map():
    def __init__(self) -> None:

        room_maker = RoomMaker()
        self.rooms_available = room_maker.make_room()

        # player data
        self.current_room = 'start'
        self.previous_room = None
        self.current_action = 'player_movement'

        self.symbols = {
            'player': '@',
            'occurence': 'o',
            'battle': 'b',
            'elite': 'e',
            'boss': 'w',
            'locked': 'x',
            'empty': '.'
        }

        self.hex_map = [
            r'     a b c d e f g h i            ',
            r'    / \ / \ / \ / \ / \           ',
            r'   | a1 | c1 | e1 | g1 | i1 |   1 ',
            r'  / \ / \ / \ / \ / \ / \         ',
            r' | start | b2 | d2 | f2 | h2 | w | 2  ',
            r'  \ / \ / \ / \ / \ / \ /         ',
            r'   | a3 | c3 | e3 | g3 | i3 |   3 ',
            r'    \ / \ / \ / \ / \ /           ',
        ]

    # map legend generation
    def draw_map(self) -> None:
        print('''
Map Legend:
player: @

rooms:
occurence: o
battle: b
elite: e
boss: w
locked: x
        ''')
        for row in range(len(self.hex_map)):
            line = self.hex_map[row]

            for room_name in self.rooms_available:
                if room_name in line:
                    room_event = self.rooms_available[room_name]['event']

                    symbol = self.symbols.get(room_event, self.symbols['empty'])

                    if self.current_room == room_name:
                        symbol = self.symbols['player']

                    line = line.replace(room_name, symbol)

            print(line)
    
    def draw_map_movement(self) -> None:
        print('''
Movement Map:
Type in the room you want to move into!
        ''')
        for row in self.hex_map:
            line = row

            for room_name in self.rooms_available:
                if room_name == self.current_room:
                    line = line.replace(room_name, self.symbols['player'])

                if room_name == self.previous_room:
                    line = line.replace(self.previous_room, self.symbols['locked'])

                if room_name not in self.rooms_available[self.current_room]['connections']:

                    line = line.replace(room_name, self.symbols['locked'])

            print(line)
    
    # make a move and then return the domain the player had occupied
    def move(self) -> str:
        if self.current_action == 'player_movement':
            while True:
                print(f'\nYour next available move choice: {self.rooms_available[self.current_room]["connections"]}')
                move_to = input('Pick your next move: ').strip().lower()
                if move_to in self.rooms_available[self.current_room]['connections'] and self.rooms_available[move_to]['event'] != 'locked':
                    self.rooms_available[self.current_room]['event'] = 'locked'
                    self.previous_room = self.current_room
                    self.current_room = move_to
                    self.current_action = self.rooms_available[self.current_room]['event']
                    break
                else:
                    print('\nRoom is unavailable')

        action = self.current_action
        print()

        # occurence domain
        if self.current_action == 'occurence':
            print('Domain activated: Occurence')
            self.current_action = 'player_movement'

        # battle domain
        if self.current_action == 'battle':
            print('Domain activiated: Battle')
            self.current_action = 'player_movement'

        # elite domain
        if self.current_action == 'elite':
            print('Domain activated: Elite')
            self.current_action = 'player_movement'

        # boss domain
        if self.current_action == 'boss':
            print('Boss fight!')
            self.current_action = 'end'
        
        return action