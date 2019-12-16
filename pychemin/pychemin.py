from lark import Lark
import sys
from unidecode import unidecode

story_file = sys.argv[1] if len(sys.argv) > 1 else "story"

if not story_file.endswith('.pychemin'):
      story_file += ".pychemin"

with open('parser.lark', 'r') as file:
      parser = Lark(file.read(), start='dialog')

with open(f'{story_file}', 'r') as file:
      cont = file.read()
      # cont = unidecode(cont)
      
_ = parser.parse(cont)
print('_________parsed_content_________')
print(_.pretty())
print(_)
