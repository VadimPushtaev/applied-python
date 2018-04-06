class Limit:
    def __init__(self, quota, period):
        self._quota = quota
        self._period = period
        self._start = None
        self._consumed = 0

    def can_consume(self, dt, to_consume=1):
        if self._start is None or self._start + self._period <= dt:
            self._start = dt
            self._consumed = 0

        return self._consumed + to_consume <= self._quota

    def consume(self, dt, to_consume=1):
        if not self.can_consume(dt, to_consume):
            raise RuntimeError("Can't consume")

        self._consumed += to_consume
