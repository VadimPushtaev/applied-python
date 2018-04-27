import sys

class CommandPool:
    COMMAND_CLASSES = []

    @classmethod
    def register_command_class(cls, klass):
        cls.COMMAND_CLASSES.append(klass)

    def __init__(self):
        self._command_handlers = [klass() for klass in self.COMMAND_CLASSES]
    
    def handle(self, command_text):
        for handler in self._command_handlers:
            try:
                result = handler.handle(command_text)
                if result is not None:
                    return result
            except Exception as e:
                print(sys.exc_info())
 
