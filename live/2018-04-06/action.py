class Action:
    def __init__(self, name, amount_resource_pairs):
        self._name = name
        self._amount_resource_pairs = amount_resource_pairs

    def _can_consume(self, dt):
        return all(
            resource.can_consume(dt, amount)
            for amount, resource in self._amount_resource_pairs
        )

    def consume(self, dt):
        if not self._can_consume(dt):
            raise RuntimeError("Can't consume")

        for amount, resource in self._amount_resource_pairs:
            resource.consume(dt, amount)
