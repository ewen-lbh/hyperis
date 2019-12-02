from time import sleep
from unidecode import unidecode
from fuzzywuzzy import process
import sys

def title(style="default"):
    with open('main-title-{}.txt'.format(style), 'r', encoding='utf8') as file:
        return file.read()

def ask(choices: list, error_msg: str, restrict_to_choices: bool = True):
    # Récupérer la réponse du joueur, et enlève les accents.
    ans = unidecode(input('> '))
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
    if score >= 85:
        # On passe sur chaque choix
        for synonyms in choices:
            # On voit si le choix extrait par fuzzywuzzy est dans la liste de synonymes pour ce choix
            if closest in synonyms:
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

def typewriter(text: str, speed: int = 30, method = 'char'):
    # On divise le texte en fragments, selon la méthode utilisée
    if method == 'char':
        # Division caractère par caractère
        fragments = list(text)
    elif method == 'line':
        # Division ligne par ligne
        fragments = [line + '\n' for line in text.split('\n')]
    else:
        # Si jamais la méthode utilisée n'est pas reconnue, on lève
        # une erreur.
        raise ValueError('Unknown typewriter method ' + method)
    # On calcule la valeur du délai à appliquer entre l'écriture de 
    # chaque fragment
    delay = 1/speed
    # Pour chaque fragment...
    for fragment in fragments:
        # On affiche le fragment, sans retour à la ligne
        print(fragment, end='')
        # On "flush" la sortie (module sys)
        sys.stdout.flush()
        # On attend le délai avant d'écrire le prochain fragment
        sleep(delay)
    # On met un retour à la ligne final
    print()

def ask_bool():
    return ask(
        [
            ["oui", "yes", "ouais", "ja", "ya", "da", "si"], 
            ["non", "blyat", "блять", "niet", "no", "nein", "nan", "nope", "nop"]
        ],
        "Ceci est une question fermée! Répondez par oui ou par non"
        )
