from datetime import datetime

class TimeInterval:
    DEFAULT_BEGIN = datetime(1970, 1, 1)

    def __init__(self, begin=None, end=None):
        if begin is None:
            begin = self._get_default_begin()
        if end is None:
            end = self._get_default_end()

        self._begin = begin
        self._end = end

    @classmethod
    def _get_default_begin(cls):
        return cls.DEFAULT_BEGIN

    @classmethod
    def _get_default_end(cls):
        return datetime.now()

    def get_length(self):
        return self._end - self._begin

    def __repr__(self):
        return 'TimeInterval({}, {})'.format(repr(self._begin), repr(self._end))

    def __str__(self):
        return '{} -> {}'.format(self._begin, self._end)
