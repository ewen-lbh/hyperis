from characters import *
from ui import typewriter
from commands_parser import ask
from player import player

Artur.say("Merci d'avoir rejoint nos rangs. Bienvenue dans la résistance, dont je suis le chef, {}.".format(Artur.name_russian))
typewriter(
"""
Dans le quartier général de la résistance, tout semble calme. Très calme. Trop calme. Toi, du haut de ton rang de simple résistant arrivé depuis peu, tu cherche quelque chose a faire. L'endroit est rempli de truc en tout genre. Allant de la simple table où quelques résistants jouent au tarot à la salle d'entrainement, tu as du mal à choisir quoi faire. Tu sais cependant qu'en temps que résistant, les efforts autant mentaux que physiques font partie de ton quotidien. Il est temps de faire un choix sur ce que tu veux faire. Ce n'est pas en restant planté là que tu arriveras à quelque chose.
"""
)

action = ask((['tarot', 'repos'], 'entraînement'), True)

if action == 'tarot':
    player.smart += 0.01
elif action == 'entraînement':
    player.strength += 0.05

typewriter("Un résistant s'approche de toi pour te dire que le chef veut te voir")
