from termcolor import cprint
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
    def __init__(self):
        try:
            self.name = os.getlogin()
        except FileNotFoundError:
            self.name = None
        self.hp         = 100
        self.speed      = 100
        self.reputation = 0
        self.food       = 1
        self.smart      = 1/2
        self.strength   = 0

    def change(self, stat, value):
        # On récupère la valeur actuelle pour la modifier
        val = getattr(self, stat)
        # On change la valeur
        setattr(self, stat, val+value)
        # On récupère la nouvelle valeur
        new_val = getattr(self, stat)

        # On récupère le nom de la stat
        name = UI_STATS.get(stat, None)
        # Si il n'y en a pas, on quitte maintenant:
        # La modification n'entraînera pas l'affichage d'un message.
        if name is None: return

        # On crée le message à afficher: Nom: gain/perte -> nouvelle valeur.

        #                   Affiche le signe même lorsque la valeur est positive
        #                            \______________________________/
        message = "%s: %s%s -> %s" % (name, '+' if value > 0 else '', value, new_val)
        
        print('\n[', end='')
        if value < 0:
            cprint(message, 'red', end='')
        elif value > 0:
            cprint(message, 'green', end='')
        print(']\n')


player = Player()
