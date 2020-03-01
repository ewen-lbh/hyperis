from .ui import typewriter
from colr import Colr as C
from termcolor import cprint, colored
from .player import UI_STATS

class Character:
    def __init__(self, name, role=None, klass=None, color=None, side=None, traits=None, is_from=None, special=False, relation=0):
        self.name, self.name_russian = name
        if self.name_russian is None: self.name_russian = self.name
        self.role = role
        self.klass = klass
        self.color = color or '#fff'
        self.side = side
        self.traits = traits
        self.is_from = is_from
        self.special = special
        self.relation = relation
        
    def say(self, text):
        # On mets des crochets autour du nom du personnage, et on espace
        name = "[{}]  ".format(self.name_russian) 
        # On récupère la longueur avant de rajouter les caractères invisibles indiquant la couleur
        name_len = len(name)
        # On colore le préfixe du nom du personnage
        name = C().hex(self.color, name)
        
        typewriter(
            name + text,
            speed=40,
            end='\n\n', 
            textwrapper_args={
                'subsequent_indent': name_len * ' '
            }
        )

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
        message = "| %s: %s [%s]" % (
            name,
            colored(op_symbols[op]+str(value), color, attrs=['bold']),
            new_val
        )
        
        cprint(message, attrs=['bold'])

## SPECIAL CHARACTERS
##

# The "unknown" character, use [???] in pychemin files
Unknown = Character(
    name=("???", None),
    role=None,
    klass=None,
    is_from=None,
    color="#cccccc",
    side=None
)

## PERSOS PRINCIPAUX
##   

Lydia = Character(
    name=("Lydia von Hardenberg", "Лидя фон Ардэнбэрг"),
    role="Reine d'Hyperis",
    klass="??",
    color="#b4a7d6",
    is_from="grand harz",
    side="queen"
)

Agidius = Character(
    name=("Ägidius Lowenstam","Эгидюс Ловэнштам"),
    role="Général de la Garde Royale et de l'Armée",
    klass="??",
    color="#f1c232",
    is_from="bliarussa",
    side="queen"
)

Artur = Character(
    name=("Artur Zarzeit", "Артур Чарчайт"),
    role="Chef de la résistance",
    klass="??",
    color="#6d9eeb",
    is_from="Ruma",
    side="resistance"
)

Enrich = Character(
    name=("Enrich Stein", "Энриш Штайн"),
    role="Sous-chef de la résistance",
    klass="??",
    color="#cc0000",
    is_from="Ukaland",
    side="resistance"
)

Grzeska = Character(
    name=("Grzęskä Czekoczkięwich", None),
    role="Ambassadeur de la RDN",
    klass="??",
    is_from=["république des deux nations","pologne"],
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
    relation=30
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
    traits=["brune"],
    relation=-15
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
    is_from=["republique des deux nations","lituanie"]
)

Wladek = Character(
    name=("Wladek Machofnik", "Владек Машофник"),
    role="voyageur",
    is_from="pologne",
    special=True
)

Toma = Character(
    name=("Toma Gloglouglouglaglougleglengloglolen", "Тома Глоглуглуглаглуглэглэнглоглолэн"),
    is_from="madagascar",
    role="vendeur",
    relation=100
)
