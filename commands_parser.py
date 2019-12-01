"""
Parse commands from the user
"""
from ui import typewriter
from unidecode import unidecode
from termcolor import cprint

def yes_or_no(answer, accept_idk=True, error_message="Veuillez répondre correctement"):
    YES = ["oui", "yes", "ouais", "ja", "ya", "da", "si"]
    NO = ["non", "blyat", "блять", "niet", "no", "nein", "nan", "nope", "nop"]
    IDK = ["jsp", "chais pas", "je ne sais pas", "jsais pas", "je sais pas"]
    
    choices = [YES, NO]
    if accept_idk: choices.append(IDK)
    
    return ask(choices, False, error_message)

QUEEN = ["reine", "lydia", "von hardenberg"]
RESISTANCE = ["resistance", "revolte", "rebellion"]


def get_input(question, choices=None):
    choices = list() if choices is None else choices
    template = ("{choices}> ", "")
    choices_template = ("[", "/", "]")  # open, separator, close

    if len(choices):
        choices_str = choices_template[0] + \
            choices_template[1].join(choices) + choices_template[2]
    else:
        choices_str = ""
        
    template = [ t.format(q=question, choices=choices_str) for t in template ]

    return input(template[0] + question + template[1])

def dbg(string): print(f'[DEBUG] {string}')

def ask(choices, allow_not_in_choices=False, error_message="Veuillez faire un choix valide !"):
    ans = input("> ")
    ans = unidecode(ans)
    dbg(ans)
    for choice in choices:
        if type(choice) is not list:
            choice = [choice]
        dbg(choice)
        for choice_synonym in choice:
            dbg(choice_synonym)
            if choice_synonym in ans:
                return choice[0]
    if allow_not_in_choices:
        return None
    else:
        cprint('\n'+error_message, 'red')
        return ask(choices, allow_not_in_choices, error_message)
