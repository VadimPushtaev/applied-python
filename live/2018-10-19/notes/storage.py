from abc import ABCMeta, abstractmethod
from typing import Optional


class AbstractStorage(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key: str) -> Optional[str]:
        pass

    @abstractmethod
    def set(self, key: str, value: str) -> None:
        pass


class MemoryStorage(AbstractStorage):
    def __init__(self):
        super().__init__()
        self._data = {}

    def get(self, key: str) -> Optional[str]:
        return self._data.get(key)

    def set(self, key: str, value: str) -> None:
        self._data[key] = value