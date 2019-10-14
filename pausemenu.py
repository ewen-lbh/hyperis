from curses import panel

class PauseMenu:
    def __init__(self, win, items):
        """
        Initialiaze the pause menu
        :param items: An array of objects containing a name key and an action key
        """
        self.items = items
        self.win = win.subwin(0,0)
        self.position = 0
        self.panel = panel.new_panel()
        self.items = items
        self.items.append({'name': 'Exit', 'action': '__exit__'})

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.win.clear()