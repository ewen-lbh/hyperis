import colorama
from termcolor import cprint, colored
colorama.init()

def aligned(string:str, align:str="center", width:int=0):
    if width == 0: width = len(string)

    if align == 'center':
        return '{:^{w}}'.format(string, w=width)
    elif align == 'right':
        return '{:>{w}}'.format(string, w=width)
    else:
        return '{:{w}}' .format(string, w=width)

def box(content:str, color:str='white', pad:int=1, align:str="center", width:int=0, first_line_is_title:bool=True, margin:int=1):
    from math import ceil
    lines = content.split('\n')
    width = width or max(len(l) for l in lines)
    boxed = []
    if first_line_is_title:
        title = lines[0]
        lines = lines[1:] # Blank line jump + all other lines
        title = colored(title, 'cyan', attrs=['bold']) + ' '  * (width - len(title))

    boxed.append('╭' + '─' * (width+pad*2) + '╮')
    if first_line_is_title:
        boxed.append('│' + ' ' * pad + title + ' ' * pad + '│')
        boxed.append('│' + '-' * (width+pad*2) + '│')
    for l in lines: boxed.append('│' + ' ' * pad + aligned(l, align, width) + ' ' * pad + '│')
    boxed.append('╰' + '─' * (width+pad*2) + '╯')

    print('\n' * margin + '\n'.join(boxed) + '\n' * margin)
    
print(box("\nGGIHRIHIGRHIHGE"))