from sys import argv
from hyperis import paths
from hyperis.walker import Walker
from hyperis.parser import Parser

class Game:
  def __init__(self, entry_point):
    self.story   = open(entry_point, 'r').read()

  def start(self):
    directives = Parser().parse(self.story)
    Walker(directives).walk()

if __name__ == "__main__":
  story = argv[1] or paths.STORY_ENTRY_POINT
  game = Game(story)
  game.start()
