class Action:
    def __init__(self, name, resources):
        self._name = name
        self._resources = resources

    def can_consume(self, dt, to_consume=1):
        return all(resource.can_consume(dt, to_consume) for resource in self._resources)

    def consume(self, dt, to_consume=1):
        if not self.can_consume(dt, to_consume):
            raise RuntimeError("Can't consume")

        for resource in self._resources:
            resource.consume(dt, to_consume)
