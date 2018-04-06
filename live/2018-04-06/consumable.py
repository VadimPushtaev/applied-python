from abc import ABCMeta, abstractmethod


class Consumable(metaclass=ABCMeta):
    @abstractmethod
    def can_consume(self, dt, to_consume):
        pass

    @abstractmethod
    def consume(self, dt, to_consume):
        pass


class NestedConsumable(Consumable):
    @abstractmethod
    def _get_nested_consumables(self):
        pass

    def can_consume(self, dt, to_consume=1):
        return all(
            consumable.can_consume(dt, to_consume)
            for consumable in self._get_nested_consumables()
        )

    def consume(self, dt, to_consume=1):
        if not self.can_consume(dt, to_consume):
            raise RuntimeError("Can't consume")

        for consumable in self._get_nested_consumables():
            consumable.consume(dt, to_consume)
