class Character:
    def __init__(name, role, klass):
        self.name, self.name_russian = name
        self.role = role
        self.klass = klass
    
Lydia = Character(
    name=("Lydia von Hardenberg", "Лидя фон Ардэнбэрг"),
    role="Reine d'Hyperis",
    klass="??"
)

Agidius = Character(
    name=("Ägidius Lowenstam","Эгидюс Ловэнштам"),
    role="Général de la Garde Royale et de l'Armée",
    klass="??"
)

Artur = Character(
    name=("Artur Zarzeit", "Артур Чарчайт"),
    role="Chef de la résistance",
    klass="??"
)

Enrich = Character(
    name=("Enrich Stein", "Энриш Штайн"),
    role="Sous-chef de la résistance",
    klass="??"
)

Grzeska = Character(
    name=("Grzęskä Czekoczkięwich", None),
    role="Ambassadeur de la RDN",
    klass="??"
)
