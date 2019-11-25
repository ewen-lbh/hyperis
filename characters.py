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
    

## PERSOS PRINCIPAUX
##   

Lydia = Character(
    name=("Lydia von Hardenberg", "Лидя фон Ардэнбэрг"),
    role="Reine d'Hyperis",
    klass="??",
    color="#b4a7d6",
    side="queen"
)

Agidius = Character(
    name=("Ägidius Lowenstam","Эгидюс Ловэнштам"),
    role="Général de la Garde Royale et de l'Armée",
    klass="??",
    color="#f1c232",
    side="queen"
)

Artur = Character(
    name=("Artur Zarzeit", "Артур Чарчайт"),
    role="Chef de la résistance",
    klass="??",
    color="#6d9eeb",
    side="resistance"
)

Enrich = Character(
    name=("Enrich Stein", "Энриш Штайн"),
    role="Sous-chef de la résistance",
    klass="??",
    color="#cc0000",
    side="resistance"
)

Grzeska = Character(
    name=("Grzęskä Czekoczkięwich", None),
    role="Ambassadeur de la RDN",
    klass="??",
    color="#674ea7",
    side=None
)

##
## PERSOS SECONDAIRES

Boris = Character(
    name=("Boris Albanov", "Борис Албанов"),
    is_from="russa",
    side="resistance",
    traits=["baraqué"]
)

Melinda = Character(
    name=("Melinda Katona", "Мелинда Катона"),
    is_from="garen",
    side="resistance",
    traits=["blond"],
)

Anatoly = Character(
    name=("Anatoly Atanjlasor", "Анатоли Атанжласор"),
    is_from="siberia",
    side="resistance",
    traits=["blond"]
)

Artyom = Character(
    name=("Artyom Kashanski", "Артём Кашански"),
    is_from="bliarussa",
    side="resistance",
    traits=["brindille"]
)

Johanna = Character(
    name=("Johanna Feuerbach", "Жохана Фоербах"),
    is_from="austri",
    side="resistance",
    traits=["brune"]
)

## PNJ λ
##

Marco = Character(
    name=("Marco Morandino", "Марко Морандино"),
    is_from="corse",
    role="marchand",
    side=None
)

Rodolf = Character(
    name=("Rodolf Haz", "Родолф Хаз"),
    role="tavernier",
    side=None
)

Woldemar = Character(
    name=("Woldemar", "Волдемар"),
)

Anna = Character(
    name=("Anna Kirchov", "Ана Киршов")
)

Sveika = Character(
    name=("Sveika Dienaki", "Свеика Денаки"),
    special=True,
    role="marchand",
    is_from="lituanie"
)

Wladek = Character(
    name=("Wladek Machofnik", "Владек Машофник"),
    role="voyageur",
    is_from="pologne",
    special=True
)

Toma = Character(
    name=("Toma Gloglouglouglaglougleglengloglolen", "Тома Глоглуглуглаглуглэглэнглоглолэн"),
    role="vendeur"
)
