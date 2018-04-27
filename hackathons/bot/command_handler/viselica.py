from command_pool import CommandPool
from command_handler import CommandHandler
import requests

@CommandPool.register_command_class
class ViselicaCommandHandler(CommandHandler):
    def __init__(self):
        self.clear()

    def clear(self):
        self.word = ''
        self.commands = ['check', 'start']
        self.commands_dict = {'check': self.check, 'start': self.start}
        self.is_started = False
        self.result = []
        self.know = False
        self.number_trying = 6

    def handle(self, text):
        print("adfsdf")
        parsed_text = text.strip().split()
        print(parsed_text)
        if parsed_text[0] == 'viselica':

            if parsed_text[1] in self.commands:
                print(self.commands_dict[parsed_text[1]](parsed_text))

    def check(self, parsed_text):
        if not self.is_started:
            return "The game is not started"
        if len(parsed_text[2]) == 1:
            char = parsed_text[2]
            self.know = False
            for i in range(len(self.word)):
                if self.word[i] == char:
                    self.know = True
                    self.result[i] = char

            if ''.join([*self.result]) == self.word and self.word != '':
                self.clear()
                return 'Congratulation!!! You win'

            if self.know:
                return 'Success, ' + ' '.join([*self.result])
            else:
                if self.number_trying == 0:
                    self.clear()
                    return 'Defeat!'
                self.number_trying -= 1
                return 'Wrong!\nNumber of trying: {}'.format(self.number_trying)
        else:
            return 'Wrong! Only single char!'

    def start(self, parsed_text):
        if self.is_started:
            return 'The game is already started'
        self.is_started = True
        self.word = self.get_word()
        self.result = ['_'] * len(self.word)
        return 'The game is started, length: {}'.format(len(self.word))

    def get_word(self):
        response = requests.get('https://castlots.org/generator-slov/generate.php', headers={
            'X-Requested-With': 'XMLHttpRequest',
        })
        return response.json()['va']



