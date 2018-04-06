class Resource:
    def __init__(self, name, limits):
        self._name = name
        self._limits = limits

    def can_consume(self, dt, to_consume=1):
        return all(limit.can_consume(dt, to_consume) for limit in self._limits)

    def consume(self, dt, to_consume=1):
        if not self.can_consume(dt, to_consume):
            raise RuntimeError("Can't consume")

        for limit in self._limits:
            limit.consume(dt, to_consume)
