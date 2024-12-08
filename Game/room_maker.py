import random

class RoomMaker():
    def __init__(self):
        self.__original_rooms = {'start':{'event':'start', 'connections':['a1','b2','a3']},
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

    def make_room(self):

        #make a copy of map -> we wanna keep the base map but randomize the events
        new_room = self.__original_rooms.copy()
        possible_events = ['battle', 'occurence', 'elite',]
        
        for room in new_room:
            if room not in ['start', 'boss']:
                new_room[room]['event'] = random.choice(possible_events)
                
        return new_room