import shutil
window_size = shutil.get_terminal_size((80, 20))  # (rows, cols)
window_size = (window_size.lines, window_size.columns)