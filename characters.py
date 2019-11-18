from ui import typewriter
from colr import Colr as C

class Character:
    def __init__(self, name, role, klass, color):
        self.name, self.name_russian = name
        if self.name_russian is None: self.name_russian = self.name
        self.role = role
        self.klass = klass
        self.color = color
        
    def say(self, text):
        character_str = "[{}]".format(self.name_russian) 
        character_str = C().hex(self.color, character_str)
        
        typewriter(character_str + "  " + text)
    
Lydia = Character(
    name=("Lydia von Hardenberg", "Лидя фон Ардэнбэрг"),
    role="Reine d'Hyperis",
    klass="??",
    color="#b4a7d6"
)

Agidius = Character(
    name=("Ägidius Lowenstam","Эгидюс Ловэнштам"),
    role="Général de la Garde Royale et de l'Armée",
    klass="??",
    color="#f1c232"
)

Artur = Character(
    name=("Artur Zarzeit", "Артур Чарчайт"),
    role="Chef de la résistance",
    klass="??",
    color="#6d9eeb"
)

Enrich = Character(
    name=("Enrich Stein", "Энриш Штайн"),
    role="Sous-chef de la résistance",
    klass="??",
    color="#cc0000"
)

Grzeska = Character(
    name=("Grzęskä Czekoczkięwich", None),
    role="Ambassadeur de la RDN",
    klass="??",
    color="#674ea7"
)
