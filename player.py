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
    def __init__(self, win, name, atk, hp, pos=None, speed=1):
        self.win   = win
        self.name  = name
        self.atk   = atk
        self.hp    = hp
        self.pos   = pos or [(window_size[1]//2), (window_size[0]//2), NORTH]
        self.speed = speed
        self.sprite= self._get_sprite()
        
    def _get_sprite(self):
        sprite_name = self._as_word(self.pos[2]).lower()
        with open("sprites/player/facing-%s.txt" % sprite_name, 'r') as file:
            return file.read()

    def look(self, direction):
        self.pos[2] = direction
        self.sprite = self._get_sprite()
        

    def move(self, to):
        # TODO: handle case where player touches the edges of the map
        if to == LEFT:
            self.look(WEST)
            self.pos[0] -= self.speed
            if self.pos[0] < 0:
                self.pos[0] = 0
        elif to == RIGHT:
            self.look(EAST)
            self.pos[0] += self.speed
            if self.pos[0] > window_size[1]:
                self.pos[0] = window_size[1]
        elif to == DOWN:
            self.look(SOUTH)
            self.pos[1] += self.speed
            if self.pos[1] > window_size[0]:
                self.pos[1] = window_size[0]
        elif to == UP:
            self.look(NORTH)
            self.pos[1] -= self.speed
            if self.pos[1] < 0:
                self.pos[1] = 0
        else:
            raise NotImplementedError(
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
