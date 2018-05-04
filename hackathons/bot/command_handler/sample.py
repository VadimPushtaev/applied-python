from command_pool import CommandPool
from command_handler import CommandHandler


@CommandPool.register_command_class
class SampleCommandHandler(CommandHandler):
    def handle(self, text):
        if text.startswith('_'):
            return text

        if text.startswith('@'):
            raise RuntimeError(text)
