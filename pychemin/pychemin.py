from lark import Lark
hyp_parser = Lark(r"""
%import common.ESCAPED_STRING -> STRING
%import common.SIGNED_NUMBER  -> SIGNED_NUMBER
%import common.WS
%ignore WS

?indent: "   " -> indent
?text: /.+/ -> text

?char_name: "[" /[^\]]+/  "]" -> name
?char_line: char_name " "+ text -> character
?narrator_line: "|" " "+ text -> narrator

?choices: text (", " text)* -> choices
?input_condition: ">> " choices -> input
?input_fallback: ">?" -> fallback


?directive: narrator_line
          | char_line
          | input_condition
          | input_fallback
dialog: (indent* directive /\n/)+
""", start='dialog')

with open('story.pychemin', 'r') as file:
      cont = file.read()      
_ = hyp_parser.parse(cont)
print('_________parsed_content_________')
print(_.pretty())
