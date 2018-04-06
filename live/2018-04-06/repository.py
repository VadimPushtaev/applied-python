class Repository:
    def __init__(self, actions):
        self._actions = actions

    def do_action(self, action_name, dt):
        action = self._get_action_by_name(action_name)
        if action is None:
            raise ValueError("Action couldn't be found")
        try:
            action.consume(dt)
            return True
        except RuntimeError:
            return False

    def _get_action_by_name(self, action_name):
        try:
            return next(action for action in self._actions if action.name == action_name)
        except StopIteration:
            return None
