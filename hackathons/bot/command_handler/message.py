from command_pool import CommandPool
from command_handler import CommandHandler
from random import randint


@CommandPool.register_command_class
class MessageCommandHandler(CommandHandler):
    messages = []

    def handle(self, text):
        if text.startswith('_start '):
            self.messages.append(text[7:])
        elif text.startswith('_get'):
            result = self.messages[-1]
            del (self.messages[-1])
            return result
        elif text.startswith('_random'):
            index = randint(len(self.messages))
            result = self.messages[index]
            return result

        if text.startswith('@'):
            raise RuntimeError(text)
