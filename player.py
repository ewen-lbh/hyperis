from config import window_size

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Player:
    def __init__(self, win, name, atk, hp, pos=None, speed=1, facing=NORTH):
        self.win   = win
        self.name  = name
        self.atk   = atk
        self.hp    = hp
        self.pos   = pos or [(window_size[1]//2), (window_size[0]//2), facing]
        self.speed = speed
        self.sprite= '☺'
        self.reputation = 0 # Value between -1 and 1: -1 == rly bad, 1 == gr8
        
    def _get_sprite(self):
        sprite_name = self._as_word(self.pos[2]).lower()
        with open("sprites/player/facing-%s.txt" % sprite_name, 'r') as file:
            return file.read()

    def look(self, direction):
        self.pos[2] = direction
        self.sprite = '☺'

    def move(self, to):
        # TODO: handle case where player touches the edges of the map
        self.win.clear()
        if to == LEFT:
            self.look(WEST)
            if self.pos[0] < 0:
                self.pos[0] = 0
            else:
                self.pos[0] -= self.speed
        elif to == RIGHT:
            self.look(EAST)
            if self.pos[0] > window_size[1]:
                self.pos[0] = window_size[1]
            else:
                self.pos[0] += self.speed
        elif to == DOWN:
            self.look(SOUTH)
            if self.pos[1] > window_size[0]:
                self.pos[1] = window_size[0]
            else:
                self.pos[1] += self.speed
        elif to == UP:
            self.look(NORTH)
            if self.pos[1] < 0:
                self.pos[1] = 0
            else:
                self.pos[1] -= self.speed
        else:
            raise TypeError(
                "Unrecognized direction code for Player.move: {}".format(to))

    def interact(self, object='facing'):
        # TODO
        raise NotImplementedError('Interact is not implemented yet')
    
    def _as_word(self, code):
        return {
            NORTH: 'NORTH',
            SOUTH: 'SOUTH',
            EAST: 'EAST',
            WEST: 'WEST',
        }.get(code, '?')

    def debug(self):
        self.win.addstr(0, 0, """-----Player "{name}"-----
atk         {atk}
hp          {hp}
position    x: {posx}, y: {posy}, facing: {facing}
--------------------------------""".format(
            hp=self.hp,
            atk=self.atk,
            posx=self.pos[0],
            posy=self.pos[1],
            facing=self._as_word(self.pos[2]),
            name=self.name
        ))
    
    def render(self):
        self.win.addstr(self.pos[1], self.pos[0], self.sprite)        
