from abc import abstractmethod, ABCMeta

class CommandHandler(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, command_text):
        pass
