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

        if text.startswith('_start '):
            self.messages.append(text[7:])
        elif text.startswith('_get'):
            result = self.messages[-1]
            del (self.messages[-1])
            return result
        elif text.startswith('_random'):
            index = rand_func(0, len(self.messages) - 1)
            result = self.messages[index]
            return result

        if text.startswith('@'):
            raise RuntimeError(text)
