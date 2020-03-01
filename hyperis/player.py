from termcolor import cprint, colored
import os

UI_STATS = {
    'hp': "Vie",
    'speed': "Vitesse",
    'reputation': "Réputation",
    'food': "Niveau d'alimentation",
    'strength': "Force",
    'smart': "Intelligence"
}

class Player:
    def __init__(self, name = None):
        self.name = name
        try:
            self.name = os.getlogin()
        except FileNotFoundError:
            self.name = name
        self.hp         = 100
        self.speed      = 100
        self.reputation = 0
        self.food       = 1
        self.smart      = 1/2
        self.strength   = 0

    def change(self, stat, op, value):
        def rst(a, b):
            raise NotImplementedError("Stat resetting is not implemented yet.")
        ops = {
            'add': lambda a, b: a + b,
            'subtract': lambda a, b: a - b,
            'set': lambda a, b: b,
            'reset': rst,
            'multiply': lambda a, b: a * b
        }
        op_symbols = {
            'add': '+',
            'subtract': '-',
            'set': '-> ',
            'reset': '-> ',
            'multiply': '×'
        }
        # On récupère la valeur actuelle pour la modifier
        val = getattr(self, stat)
        # On change la valeur
        setattr(self, stat, ops[op](val, value))
        # On récupère la nouvelle valeur
        new_val = getattr(self, stat)
        diff = new_val - val

        # On récupère le nom de la stat
        name = UI_STATS.get(stat, None)
        # Si il n'y en a pas, on quitte maintenant:
        # La modification n'entraînera pas l'affichage d'un message.
        if name is None: return

        # On crée le message à afficher
        color = 'red' if diff < 0 else 'green' if diff > 0 else 'white'
        value_change_msg = colored(op_symbols[op]+str(value), color, attrs=['bold'])
        full_msg = ' ' * 8 + value_change_msg + colored(f' {name}') + (colored(f' => {new_val}', attrs=['dark']) if op != 'set' else '')
        print('\n\n' + full_msg + '\n\n')
        


player = Player(name='Ewen')
