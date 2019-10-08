from config import window_size

class Player:
    def __init__(self, win, name, atk, hp, pos=None):
        self.win  = win
        self.name = name
        self.atk  = atk
        self.hp   = hp
        self.pos  = pos or [d//2 for d in window_size]
        
    def move(self, to, speed=1):
        # TODO: handle case where player touches the edges of the map
        if to == 'left':
            self.pos[0] -= speed
        elif to == 'right':
            self.pos[0] += speed
        elif to == 'up':
            self.pos[1] += speed
        elif to == 'down':
            self.pos[1] -= speed
        else:
            raise NotImplementedError("Unrecognized direction for Player.move: {}".format(to))
        
    def interact(self, object='facing'):
        # TODO
        raise NotImplementedError('Interact is not implemented yet')
    
    def debug(self):
        self.win.addstr(0, 0, """-----Player "{name}"-----
atk         {atk}
hp          {hp}
position    x: {posx}, y: {posy}
--------------------------------""".format(
            hp=self.hp, 
            atk=self.atk, 
            posx=self.pos[0], 
            posy=self.pos[1], 
            name=self.name
            ))
        