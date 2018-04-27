from command_pool import CommandPool
from command_handler import CommandHandler
import random

@CommandPool.register_command_class
class RollHandler(CommandHandler):
    def handle(self, text):
        if text.startswith('roll'):
            text.strip('roll')
            args = text.split('d')
            count = args[0]
            edges = args[1]
            result = []

            for i in range(count):
                result.append(random.randint(1, edges))
            return '{} ({})'.format(sum(result), result)

        if text.startswith('@'):
            raise RuntimeError(text)