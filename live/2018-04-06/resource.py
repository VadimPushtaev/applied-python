from consumable import NestedConsumable


class Resource(NestedConsumable):
    def __init__(self, name, limits):
        self._name = name
        self._limits = limits

    def _get_nested_consumables(self):
        return self._limits
