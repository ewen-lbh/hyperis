from lark import Lark
from lark.indenter import Indenter
import sys
from unidecode import unidecode
from ui import narrator, ask, ask_bool

story_file = sys.argv[1] if len(sys.argv) > 1 else "story"

if not story_file.endswith('.pychemin'):
      story_file += ".pychemin"

def _remove_blank_lines(content):
      lines = content.split('\n')
      lines = [ l for l in lines if l.strip() ]
      return '\n'.join(lines)

with open('pychemin/grammar.lark', 'r') as file:
      parser = Lark(_remove_blank_lines(file.read()), start='dialog')

with open(f'pychemin/{story_file}', 'r') as file:
      cont = file.read()
      # cont = unidecode(cont)


parsed = parser.parse(cont)

# TODO: first parse idents to transform the parser's output into sth meaningful
# eg:
"""
[
      <Node> {
            type: "question"
            question: "..."
            choices: [
                  (String) ...
            ],

            hint: None
            children: [
                  (Node) ...
            ]
      },
      {
            type: "narrator"
            text: "Bonsoir, tout le monde"
      }
]
"""

def remove_blank_lines(root):
      real_lines = []
      for line in parsed.children:
            if not hasattr(line, 'data') and not str(line).strip():
                  continue
            else:
                  real_lines.append(line)
      return real_lines


def to_indent_directive_list(children):
      resolved = []
      for line in children:
            indent = len([c for c in line.children if c.data == 'indent'])
            resolved.append((indent, line.children[0]))
      return resolved

def resolve_indents(directives):
      """
      Resovles [(ident, directive), ...] into:
      [
            [i0],
            [i0, [i1]],
            [i0, [i1, i1, [i2]]],
            [i0],
            ...
      ]

      with i<n> a directive with an <n>-level indent
      """
      return to_indent_directive_list(directives)
      resolved = []
      idx = 0
      prev_dirctive = None
      for (i, d) in directives:
            if prev_dirctive is None and i != 0:
                  raise SyntaxError("The first directive shouldn't be indented.")
            if i==0:
                  resolved.append([d])
                  idx += 1
            else:
                  resolved[idx].append([d])
            prev_dirctive = (i, d)

lines = remove_blank_lines(parsed)
lines = resolve_indents(lines)
import json

def walk(directives):
      import ui
      act_idx = 1
      chapter_idx = 1
      for (i, directive) in directives:
            print(i, str(directive) + '\n---')
      print('========')
walk(lines)
