from command_pool import CommandPool
from command_handler import CommandHandler

@CommandPool.register_command_class
class Test1421(CommandHandler):
    def handle(self, text):
        if text.startswith('1421'):
            return 'Hello bro!'

