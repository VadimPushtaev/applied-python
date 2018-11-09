import os
import re


def get_games_list():
    file_list = os.listdir('./games')
    games_list = []
    for file_name in file_list:
        if re.fullmatch(r'.*.py', file_name):
            games_list.append(file_name)

    return games_list


def get_game_dict():
    (game_class, name)

class GameLauncher:

    def __init__(self, game_dict):
        self._game_dict = game_dict
        self._game_storage = Storage()

    def print_rating(self):
        pass
    
    def choose_game(self):
        for game_name in self._game_dict:
            print("* {}".format(game_name))
        game = input("Choose one game:")


    def start(self):
        while True:
            try:
                print('Select anything:')
                print('* rating')
                print('* games')
                
                answer = input("Enter point name: ")
                if answer == 'rating':
                    self.print_rating()
                elif answer == 'games':
                    self.choose_game()
                else:
                    print("Repeat input")
                
                

                for cl in self._game_dict[game]:
                    if issubclass(cl, BaseGame):
                        cl.run()
            except KeyboardInterrupt:
                break
        print('Exiting...')
            

        

if __name__ == "__main__":
    game_list = get_games_list()
    try:
        command_module = __import__("games", fromlist=game_list)
    except ImportError:
        print('error')

    game_dict = {}

    for key in command_module.__dict__:
        if not re.match(r'__', key):
            game_dict[key] = command_module.__dict__[key]
    
    gm = GameLauncher(game_dict)
    gm.start()
