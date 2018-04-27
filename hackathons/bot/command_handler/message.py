from command_pool import CommandPool
from command_handler import CommandHandler
from random import randint


@CommandPool.register_command_class
class MessageCommandHandler(CommandHandler):
    def __init__(self):
        self.messages = []

    def handle(self, text, rand_func=None):
        if rand_func is None:
            rand_func = randint
        if not self.messages and (text.startswith('messages get') or text.startswith('messages random')):
            return 'Сообщений нет'
        if text.startswith('messages start '):
            self.messages.append(text[15:])
        elif text.startswith('messages get'):
            result = self.messages[-1]
            del (self.messages[-1])
            return result
        elif text.startswith('messages random'):
            index = rand_func(0, len(self.messages) - 1)
            result = self.messages[index]
            return result

        if text.startswith('@'):
            raise RuntimeError(text)
