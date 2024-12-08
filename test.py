# YO IT CAN RANDOMIZE

# map is made up of tiles, user cannot go to a tile behind them,
#Randomize rooms:

#All possible rooms
#adding event none to start

import random

rooms = {'start':{'event':'start', 'connections':['a1','b2','a3']},
         'a1':{'event':'battle','connections':['c1','b2']},
         'b2':{'event':'occurence','connections':['c1','d2','c3']},
         'a3':{'event':'elite','connections':['b2','c3']},
         'c1':{'event':'battle','connections':['e1','d2']},
         'c3':{'event':'occurence','connections':['d2','e3']},
         'd2':{'event':'elite','connections':['e1','f2','e3']},
         'e1':{'event':'battle','connections':['g1','f2']},
         'e3':{'event':'occurence','connections':['f2','g3']},
         'f2':{'event':'elite','connections':['g1','h2','g3']},
         'g1':{'event':'battle','connections':['i1','h2']},
         'g3':{'event':'occurence','connections':['h2','i3']},
         'h2':{'event':'elite','connections':['i1','boss','i3']},
         'i1':{'event':'battle','connections':['boss']},
         'i3':{'event':'occurence','connections':['boss']},
         'boss':{'event':'boss'},
         }

#make a copy of map -> we wanna keep the base map but randomize the events
#idk if need copy
rooms_available = rooms.copy()
current_room = 'start'
current_action = 'player_movement'
    #Show Status/map OVER HERE JIULIN ↓
    #print(f'Current Position:\n {current_room}')

#defining symbols on map
symbols = {
    'player': '@',
    'occurence': 'o',
    'battle': 'b',
    'elite': 'e',
    'boss': 'w',
    'locked': 'x',
    'empty': '.'
    }

#formatting map
hex_map = [
        r'     a b c d e f g h i            ',
        r'    / \ / \ / \ / \ / \           ',
        r'   | a1 | c1 | e1 | g1 | i1 |   1 ',
        r'  / \ / \ / \ / \ / \ / \         ',
        r' | start | b2 | d2 | f2 | h2 | w | 2  ',
        r'  \ / \ / \ / \ / \ / \ /         ',
        r'   | a3 | c3 | e3 | g3 | i3 |   3 ',
        r'    \ / \ / \ / \ / \ /           ',
             ]

#randomizer
def randomize_rooms():
    possible_events = ['battle', 'occurence', 'elite',]
    for room in rooms_available:
        if room not in ['start', 'boss']:
            rooms_available[room]['event'] = random.choice(possible_events)

randomize_rooms()


#map legend generation
def render_map(current_room):
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
    for row in range(len(hex_map)):
        line = hex_map[row]

        for room_name in rooms:
            if room_name in line:
                room_event = rooms[room_name]['event']

                symbol = symbols.get(room_event, symbols['empty'])

                if current_room == room_name:
                    symbol = symbols['player']

                line = line.replace(room_name, symbol)

        print(line)

#map movement generation
def render_map_movement(current_room, previous_room):
    print('''
Movement Map:
Type in the room you want to move into!
    ''')
    for row in hex_map:
        line = row

        for room_name in rooms:
          if room_name == current_room:
              line = line.replace(room_name, symbols['player'])

          if room_name == previous_room:
            line = line.replace(previous_room, symbols['locked'])

          if room_name not in rooms[current_room]['connections']:

              line = line.replace(room_name, symbols['locked'])



        print(line)

previous_room = None #defining prev room

while True:
    render_map(current_room)

    render_map_movement(current_room, previous_room)

    # movement between rooms
    if current_action == 'player_movement':
        move_to = input(f'move where?\n {rooms_available[current_room]["connections"]}\n')
        if move_to in rooms_available[current_room]['connections'] and rooms_available[move_to]['event'] != 'locked':
            rooms_available[current_room]['event'] = 'locked'
            #new code
            previous_room = current_room
            current_room = move_to
            current_action = rooms_available[current_room]['event']
        else:
            print('room is unavailable')

    # occurence domain
    if current_action == 'occurence':
        print('occurence')
        current_action = 'player_movement'

    # battle domain
    if current_action == 'battle':
        print('battle')
        current_action = 'player_movement'

    # elite domain
    if current_action == 'elite':
        print('elite')
        current_action = 'player_movement'

    # boss domain
    if current_action == 'boss':
        print('boss')
        current_action = 'end'

    if current_action == 'end':
        print('game end')
        break