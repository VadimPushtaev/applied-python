import sys
import os
import re
import argparse
from BaseGame import *

FILE_LIST = os.listdir('./games')
GAMES_LIST = []
for FILE in FILE_LIST:
    if re.fullmatch(r'.*.py', FILE):
        GAMES_LIST.append(FILE)

try:
    command_module = __import__("games", fromlist=GAMES_LIST)
except ImportError:
    pass

def parse_args(args):
    parser = argparse.ArgumentParser(description='This is a simple tester\
                                  for your code')
    parser.add_argument('name',
                        action="store",
                        help='Name of module')
    return parser.parse_args(args)

if __name__ == "__main__":
    scorer = Scorer()
    parser = parse_args(sys.argv[1:])
    module_dict = command_module.__dict__[parser.name].__dict__
    for module in module_dict:
        if module == 'NAME':
            name = module_dict[module]
        try:
            if issubclass(module_dict[module], BaseGame):
                game_class = module_dict[module]
        except TypeError:
            pass

    game = game_class(name, scorer)
    try:
        game.run()
    except KeyboardInterrupt:
        pass
    print("Your scores after game - {}".format(scorer.get_points(name)))