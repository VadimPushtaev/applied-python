from consumable import NestedConsumable


class Action(NestedConsumable):
    def __init__(self, name, resources):
        self._name = name
        self._resources = resources

    def _get_nested_consumables(self):
        return self._resources
