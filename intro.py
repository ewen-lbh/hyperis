from ui import typewriter, title
from characters import *
from commands_parser import *

intro = """Il y avait depuis 1687, un royaume nommé Hyperis. 
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
"""

typewriter(title(), speed=5, method="line")
typewriter(intro, speed=25)

camp = which_camp(get_input(""))
while camp is None:
    typewriter("Veuillez choisir un camp!\n", speed=80)
    camp = which_camp(get_input(""))

if camp == "queen":
    Lydia.say("Bon choix. Bienvenue parmi nous! MUAUAHHAHAHHAHHAHAHHAHAHAHHA")
else:
    Artur.say("Merci d'avoir rejoint nos rangs. Bienvenue dans la résistance, dont je suis le chef, {}".format(Artur.name_russian))
