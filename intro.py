from ui import typewriter, hyperis_title, ask, narrator
from player import player
import os
import sys
from datetime import datetime
from time import sleep
from random import randint
os.system('clear')

def procedure(text):
    dots = randint(5, 10)
    typewriter(text, end='')
    typewriter("." * dots, speed=10, end='')
    print('OK.')

# Tout en vert
print('\033[38;5;10m', end='')

procedure("Booting into emergency recovery mode")

typewriter("""


TIMEWORKS CO.
QUICKJUMP RELAPSE E57-D
EMERGENCY RECOVERY MODE

YEAR..................4096
SERIAL NUMBER.........1144483135789431
LAST BOOT TIME........4752715552 days ago
""", wrap_text=False)

typewriter("/!\\ UNSECURE POST-EMERGENCY BOOT PROCEDURE DETECTED /!\\")
typewriter("Launching post-emergency boot procedure /EMERGPROC.HYP.............")
print()
print()
print()
print()
typewriter("Votre nom ?", speed=40)
player.name = input("> ")
print()
procedure("Identification")
print()
print()
typewriter("Citoyen numéro................", end=''); print( int(datetime.now().timestamp()) + os.getpid())
typewriter("Nom...........................", end=''); print(player.name)
print()
print()

typewriter("Voulez-vous continuer ?")
def y_n():
    ans = input("[Y/N]  > ").strip().upper()
    if ans == 'Y': return True
    if ans == 'N': return False
    return y_n()

if not y_n(): sys.exit()

print()
print()

procedure("Démarrage du moteur de voyage temporel")
procedure("Lecture de /QUICKWARP/LOCATIONS/WORMHOLES/HYPERIS.LOC")
procedure("Réglages des matrices de déformation spatio-temporelle")
procedure("Calibrage des stabilisateurs")
procedure("Calcul de la trajectoire")
procedure("Ajustement du saut")
typewriter("Saut dans...")
typewriter("3.........", speed=10)
typewriter("2.........", speed=10)
typewriter("1.........", speed=10)


os.system('clear')
print('\033[0m', end='')

print('\n' * 4)
typewriter(hyperis_title(), speed=5, method="line", wrap_text=False)
narrator("""Il y avait depuis 1687, un royaume nommé Hyperis. 
Sa naissance étouffa celle du Saint Empire Romain Germanique et des Empires Russe et Autrichiens. 
Le royaume devint alors le plus grand de tous. Cependant, jamais il ne se déclara comme un empire. 
Depuis lors, la Reine du pays était vénérée autant que Dieu et les couronnements étaient vus comme des actes divins. ...
Jusqu’en 1779 où le couronnement de la jeune reine de 14 ans Lydia Von Hardenberg fit polémique. 
Jamais dans l’histoire d’Hyperis, une reine si jeune fut couronnée. 
Personne ne l’estima apte à gouverner et le peuple douta de sa légitimité. 
Alors, Lydia réagit comme n’importe quel enfant de 14 ans. 
Paniquée, elle demanda de l’aide à son général, Ägidius Lowenstam. 
Ce dernier lui conseilla de durcir les lois. Et c’est ce qu’elle fit...
Le peuple s’indigna et Lydia leur affirma que c’était pour leur bien et qu’elle savait ce qu’elle faisait. 
Mais une révolte émergea et la reine décida d’envoyer l’armée pour 
éteindre la flamme qui risquait de mettre le feu aux poudres.
C’est dans ce contexte que vous devez choisir un camp, tout neutre étant 
considéré pour un traître aux deux côtés. 

Vos choix pourront peut-être changer l’histoire...
""")

import beginning
