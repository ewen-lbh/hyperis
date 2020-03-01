from lark import Lark, Transformer
from lark.indenter import Indenter
import sys
from termcolor import cprint
from unidecode import unidecode
from hyperis import ui
from hyperis import debug
from hyperis.player import player, UI_STATS
from hyperis import characters

story_file = sys.argv[1] if len(sys.argv) > 1 else "story"

def main(story_file):
      if not story_file.endswith('.pychemin'):
            story_file += ".pychemin"

      def _remove_blank_lines(content):
            lines = content.split('\n')
            lines = [ l for l in lines if l.strip() ]
            return '\n'.join(lines)

      with open('pychemin/grammar.lark', 'r') as file:
            parser = Lark(_remove_blank_lines(file.read()), start='dialog', maybe_placeholders=True)

      with open(f'story/{story_file}', 'r') as file:
            cont = file.read()
            # cont = unidecode(cont)

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
                  directive = [c for c in line.children if c.data != 'indent'][0]  # There should be at most one directive per line (and 0+ indent tokens)
                  resolved.append((indent, directive))
            return resolved
            
      class RemoveAnons(Transformer):
            def __ANON_2(self, args):
                  print(args)
                  return args[0]
                  

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

      parsed = parser.parse(cont)
      parsed = RemoveAnons(visit_tokens=True).transform(parsed)
      lines = remove_blank_lines(parsed)
      lines = resolve_indents(lines)
      import json
      
      def treat_text(text, ctx):
            import re
            matches = re.finditer(r'#([\w_]+) ', text)
            if not matches: return text
            for m in matches:
                  debug.log(f'Replacing {m.group(0)} with {m.group(1)} ')
                  text.replace(m.group(0), str(ctx[m.group(1)]) + ' ')
            return text
            
      def remove_comments(directives):
            return [ d for d in directives if d.data != 'comment' ]
      
      def walk(directives, exec_ctx = {}):
            line_count = 0
            act_idx = exec_ctx.get('act_idx', 1)
            chapter_idx = exec_ctx.get('chapter_idx', 1)
            prev_dirctive = exec_ctx.get('prev_dirctive', None)
            collecting_inputs = exec_ctx.get('collecting_inputs', False)
            collecting_fallback_reaction = exec_ctx.get('collecting_fallback_reaction', False)
            fallback_reaction_directives = exec_ctx.get('fallback_reaction_directives', [])
            input_fallback_continue = exec_ctx.get('input_fallback_continue', False)
            input_entered = exec_ctx.get('input_entered', False)
            input_condition = exec_ctx.get('input_condition', {})
            input_hint = exec_ctx.get('input_hint', "")
            input_errmsg = exec_ctx.get('input_errmsg', None)
            valid_answers = exec_ctx.get('valid_answers', None)
            answer_indent = exec_ctx.get('answer_indent', 0)
            exec_ctx = { 'act_idx': act_idx, 'chapter_idx': chapter_idx }
            # For interpolations
            ctx = {
                  'name': player.name
            }
            for (i, directive) in directives:
                  line_count += 1
                  debug.log(f'@{line_count}:{i*4} -- ({i}, {directive.data})')
                  if i == answer_indent and collecting_inputs:
                        debug.log(f'Adding directive {directive.data} to {valid_answers} case')
                        input_condition[valid_answers].append((i, directive))
                  elif i == answer_indent and collecting_fallback_reaction:
                        fallback_reaction_directives.append((i, directive))
                  elif i == answer_indent-1 and (collecting_inputs or collecting_fallback_reaction) and not directive.data.startswith('input'):
                        collecting_inputs = False
                        collecting_fallback_reaction = False
                        def fallback(ctx, exec_ctx):
                              def _fb():
                                    if fallback_reaction_directives:
                                          debug.log(f'Executing fallback directives')
                                          walk(fallback_reaction_directives, exec_ctx)
                              return _fb
                        ctx['answer'] = ui.ask([json.loads(k) for k in input_condition.keys()], error_callback=fallback(ctx, exec_ctx), ask_again=input_fallback_continue, restrict_to_choices=not fallback_reaction_directives, hint=input_hint)
                        for cond, directives in input_condition.items():
                              debug.log(f'{directives}')
                              if ctx['answer'] in json.loads(cond):
                                    exec_ctx = walk(directives, exec_ctx)
                        fallback_reaction_directives = []
                        input_condition = {}
                  elif directive.data == 'comment':
                        pass
                  elif directive.data == 'new_act':
                        ui.act(act_idx, directive.children[0])
                        act_idx += 1
                  elif directive.data == 'new_chapter':
                        ui.chapter(chapter_idx, directive.children[0])
                        chapter_idx += 1
                  elif directive.data == 'narrator_line':
                        txt = treat_text(directive.children[0].value, ctx)
                        ui.narrator(txt)
                  elif directive.data == 'char_line':
                        char_node = directive.children[0]
                        char_name = char_node.value
                        char_name = 'Unknown' if char_name == '???' else char_name
                        try:
                              char = getattr(characters, char_name)
                        except AttributeError:
                              raise RuntimeError(f"No character named '{char_name}' at {char_node.line}:{char_node.column}")
                        txt = treat_text(directive.children[1].value, ctx)
                        char.say(txt)
                  elif directive.data.startswith('input'):
                        answer_indent = i+1
                        debug.log(f'Collecting inputs. answer_indent={answer_indent}')
                        if directive.data in ('input', 'input_required'):
                              collecting_fallback_reaction = False
                              collecting_inputs = True
                              valid_answers = json.dumps([ v.strip() for v in directive.children[0].value.split(',') ])
                              input_condition[valid_answers] = []
                        if directive.data == 'input_hint':
                              debug.log(f'Setting input hint to {directive.children[0].value}')
                              input_hint = directive.children[0].value
                        if directive.data.startswith('input_fallback'):
                              debug.log('ogrhigherihgre')
                              fallback_reaction_directives = []
                              collecting_inputs = False
                              collecting_fallback_reaction = True
                              input_fallback_continue = directive.data == 'input_fallback_continue'
                  elif directive.data == 'stat_change':
                        if len(directive.children) == 2:
                              target = player
                              stat_name = directive.children[0].value
                              operation = directive.children[1]
                        else:
                              target = getattr(characters, directive.children[0].value)
                              stat_name = directive.children[1].value
                              operation = directive.children[2]
                        value = float(operation.children[0].value)
                        op = operation.data
                        target.change(stat_name, op, value)
                  elif directive.data == 'load_file':
                        file = directive.children[0].value.replace(' ', '_')
                        debug.log(f'Loading {file}.pychemin...')
                        main(file)
                  else:
                        print(i, str(directive) + '\n---')
                  prev_dirctive = directive
            return exec_ctx
            print('========')
      walk(lines)

if __name__ == "__main__":
    main(story_file)
