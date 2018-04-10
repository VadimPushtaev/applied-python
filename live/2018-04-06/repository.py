class Repository:
    def __init__(self, actions):
        self._actions = actions
        self._actions_index = self._get_actions_index()

    def do_action(self, action_name, dt):
        action = self._get_action_by_name(action_name)
        if action is None:
            raise ValueError("Action couldn't be found")
        try:
            action.consume(dt)
            return True
        except RuntimeError:
            return False

    def _get_actions_index(self):
        return {action.name: action for action in self._actions}

    def _get_action_by_name(self, action_name):
        return self._actions_index.get(action_name)
