from time import sleep
from unidecode import unidecode
from fuzzywuzzy import process
from textwrap import TextWrapper
from shutil import get_terminal_size
from termcolor import colored
import sys

def previous(lisst, index):
    if index < 0: return None
    return lisst[index-1]

def hyperis_title(style="default"):
    with open('main-title-{}.txt'.format(style), 'r', encoding='utf8') as file:
        return file.read()

def ask(choices: list, error_msg: str, restrict_to_choices: bool = True, hint: str = ""):
    # Colorer l'indice de réponse
    hint = colored(hint, 'cyan')
    # Récupérer la réponse du joueur, et enlève les accents. Mettre l'indice de réponse si appliquable
    ans = unidecode(input(f'{hint}> '))
    # Certains choix n'auront pas de synonymes et seront donc simplement des chaîne de caractères.
    # On normalise la liste de choix pour que tout les choix soit une liste de synonymes
    choices = [ [s] if type(s) is not list else s for s in choices ]
    # On "aplatit" la liste de choix pour l'utiliser avec le module fuzzywuzzy: 
    # liste de listes → liste contenant touts les synonymes
    # Au passage, on enlève tout les accents avec unidecode
    flat_choices = [unidecode(synonym) for choice in choices for synonym in choice]
    # Grâce au module fuzzywuzzy, on récupère le choix qui est le plus proche parmis tout les synonymes confondus
    closest, score = process.extractOne(ans, flat_choices)
    # Si le score de similarité est assez élevé, on considère que le choix du joueur correspond au synonyme extrait.
    # Sinon, on considère que la réponse du joueur était en dehors des choix.
    if score >= 75:
        # On passe sur chaque choix
        for synonyms in choices:
            # On voit si le choix extrait par fuzzywuzzy est dans la liste de synonymes pour ce choix
            if closest in [unidecode(s) for s in synonyms]:
                # On fait une ligne vide
                print()
                # On revoie le premier synonyme pour ce choix
                return synonyms[0]
    """
    Comme `return` stopppe l'exécution de la fonction et renvoie une
    valeur, ces lignes seront exécutées seulement si aucune valeur 
    n'a été renvoyée, c'est à dire si la réponse ne contenait aucun 
    des choix valides.
    """
    # Si on autorise un choix en dehors de ceux proposés:
    if not restrict_to_choices: return None

    # Afficher le message
    typewriter(error_msg)
    # Retourner la valeur renvoyée par un nouvelle appel à la
    # fonction, re-demandant une réponse à l'utilisateur (récursion)
    try:
        return ask(choices, error_msg)
    except RecursionError:
        sys.exit("Veuillez relancer le programme et décidez-vous à repondre correctement! >:(")

def typewriter(
    text: str, 
    speed: int = 30, 
    method = 'char', 
    end='\n', 
    wrap_text: bool = True, 
    textwrapper_args: dict = None
):
    # On passe le texte en str
    text = str(text)

    if wrap_text:
        # On utilise TextWrapper pour éviter les retours à la ligne bizarres
        textwrapper_args = textwrapper_args or {}
        wrapper = TextWrapper(
            width=get_terminal_size().columns,
            **textwrapper_args
        )
        text = wrapper.fill(text)

    # On divise le texte en fragments, selon la méthode utilisée
    if method == 'char':
        # Division caractère par caractère
        fragments = list(text)
    elif method == 'line':
        # Division ligne par ligne
        fragments = [line + '\n' for line in text.split('\n')]
    else:
        # Si jamais la méthode utilisée n'est pas reconnue, on lève une erreur.
        raise ValueError('Unknown typewriter method ' + method)

    # On calcule la valeur du délai à appliquer entre l'écriture de chaque fragment
    delay = 1/speed

    # Pour chaque fragment...
    for i, fragment in enumerate(fragments):
        # On récupère le fragment précédent
        prev_fragment = previous(fragments, i)
        
        # On affiche le fragment, sans retour à la ligne
        print(fragment, end='')
        
        # On "flush" la sortie (module sys)
        sys.stdout.flush()

        # Si ce fragment est un espace et que le précédent en était un aussi, on n'attend pas le délai.
        if fragment == ' ' and prev_fragment == ' ':
            continue
        # Si ce fragment est un espace et que le fragment précédent était un point, c'est une fin de phrase:
        # On rajoute un délai additionnel
        if fragment == ' ' and prev_fragment in ('.', '?', '!'):
            sleep(0.5)
        # On attend le délai avant d'écrire le prochain fragment.
        sleep(delay)

    # On met un retour à la ligne final
    print(end, end='')

def ask_bool(error_msg: str = None, ask_again: bool = True):
    return ask(
        [
            ["oui", "yes", "ouais", "ja", "ya", "da", "si"], 
            ["non", "blyat", "блять", "niet", "no", "nein", "nan", "nope", "nop"]
        ],
        (error_msg or "Ceci est une question fermée! Répondez par oui ou par non"),
        restrict_to_choices=ask_again
    ) == 'oui'


def title(kind: str, num: int, name: str):
    kind = kind.lower()
    # Décorer la décoration en fonction du type de titre
    if kind == 'chapitre':
        decoration = colored('~ ~ ~ {title} ~ ~ ~', 'yellow')
    elif kind == 'act':
        decoration = colored('====== {title} ======', 'red')
    else:
        return ValueError(f"Unknown title kind {kind}")
    
    # Récupérer la taille du terminal
    width, height = get_terminal_size()

    # Créer le titre à partir de `kind`, `num` et `name`.
    name = f"{kind.title()} {num}: {name}"
    # Appliquer les décorations
    decorated = decoration.format(title=name)
    # Centrer le texte en utilisant la décoration, et espacer avec des lignes vides
    decorated = '\n' + decorated.center(width) + '\n'

    # Afficher le titre!
    typewriter(decorated, 5, 'line', wrap_text=False)

# Raccourcis pour title()
def act(num: int, name: str):
    return title('act', num, name)

def chapter(num: int, name: str):
    return title('chapitre', num, name)

# Raccourcis pour typewriter()
def narrator(text: str, speed: int = 30):
    return typewriter(text, speed, end='\n\n')
