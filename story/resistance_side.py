from characters import *
from ui import narrator, ask, act, chapter, ask_bool
from player import player

act(1, '')
chapter(1, 'Le QG')

Artur.say("Merci d'avoir rejoint nos rangs. Bienvenue dans la résistance, dont je suis le chef, {}.".format(Artur.name_russian))
narrator("Dans le quartier général de la résistance, tout semble calme. Très calme. Trop calme. Toi, du haut de ton rang de simple résistant arrivé depuis peu, tu cherche quelque chose a faire. L'endroit est rempli de truc en tout genre. Allant de la simple table où quelques résistants jouent au tarot à la salle d'entrainement, tu as du mal à choisir quoi faire. Tu sais cependant qu'en temps que résistant, les efforts autant mentaux que physiques font partie de ton quotidien. Il est temps de faire un choix sur ce que tu veux faire. Ce n'est pas en restant planté là que tu arriveras à quelque chose.")

action = ask((['tarot', 'repos'], ['entraînement', 'entraîner']), "Choisis entre jouer au tarot ou t'entraîner", False)

if action == 'tarot':
    player.change('smart', 0.01)
elif action == 'entraînement':
    player.change('strength', 0.05)

narrator("Un résistant s'approche de toi pour te dire que le chef veut te voir")

chapter(2, 'La mission')

narrator("C'est la première fois que Artur Zarzeit, le chef de la résistance, demande à te voir. Non, qu'il demande à voir un non gradé en fait. En réalité, cela te fais un peu peur. Il doit bien avoir une bonne raison pour que la personne la plus recherchée par la Garde Royale se montre à un résistant lambda.")

Artur.say(f"C'est bien {player.name} ?")

ans = ask_bool("*soupir* Je prends ça pour un oui...", ask_again=False)

if not ans:
    narrator("Artur sourit, désespéré")

Artur.say("Peu importe. J'ai une mission pour toi. C'est important alors écoute moi bien. Un convoi d’arme pour l’armée arrive à Potsdam ce soir vers 19h. Avec une équipe, tu devras l’intercepter avant qu’il n’arrive à bon port. Compris ?")

ans = ask_bool()

if ans:
    player.change('reputation', +0.1)
    Artur.say("Dans ce cas, tu peux rejoindre les autres dans le hall")
else:
    player.change('reputation', -0.15)
    Artur.say("Je ne vais tout de même pas me répéter … On va faire bref. Il faut que tu te rende à Potsdam pour stopper une diligence")
    
    narrator("Enrich arrive au milieu de la conversation, légèrement désespéré … trèèès légèrement désespéré.")

    Enrich.say(f"Tu es sûr que {player.name} est vraiment la bonne personne ?")

    narrator("Artur te fais un rapide signe comme quoi il veut parler seul avec le sous-chef et surtout pour t’intimer d’aller rejoindre les autres. Par conséquent tu sors donc du bureau du chef.")

narrator("Tu te retrouve donc dans le hall, avec cinq autres résistants. Il y a deux femmes et trois hommes. Parmis les femmes, l’une est blonde et l’autre brune, tandis que chez les hommes, l’un est un grand costaud, un autre est blond et le dernier est fin comme une brindille.")

ans = ask(
    [
        'brune',
        'blonde',
        ['grand', 'costaud'],
        'blond',
        ['fin', 'brindille']
    ],
    "Choisit avec qui tu veux parler. Utilise un trait physique pour désigner la personne.",
    hint="Parler à"
)

narrator("----- EN TRAVAUX ------", speed=2)
