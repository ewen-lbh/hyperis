"""
Parse commands from the user
"""
from ui import typewriter

def yes_or_no(answer, accept_idk=True):
    YES = ["oui", "yes", "ouais", "ja", "ya", "da", "si"]
    NO = ["blyat", "блять", "niet", "non", "no", "nein", "nan", "nope", "nop"]
    IDK = ["jsp", "chais pas", "je ne sais pas", "jsais pas", "je sais pas"]

    if answer.count(YES) > 0:
        return True
    if answer.count(NO) > 0:
        return False
    if accept_idk and answer.count(IDK) > 0:
        return None

    raise ValueError("Please answer with yes or no")


def which_camp(answer):
    answer = answer.replace('é', 'e').replace('è', 'e').lower()

    QUEEN = ["reine", "lydia", "von hardenberg"]
    RESISTANCE = ["resistance", "revolte", "rebellion"]

    if answer not in QUEEN and answer not in RESISTANCE:
        return None

    is_with_queen = answer in QUEEN

    # Check for inverted responses
    AGAINST = ["contre", "pas pour"]

    invert_counts = sum(answer.count(i) for i in AGAINST)
    for _ in range(invert_counts):
        is_with_queen = not is_with_queen

    return "queen" if is_with_queen else "resistance"


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
