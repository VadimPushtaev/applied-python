from abc import ABCMeta, abstractmethod
from collections import defaultdict

class Scorer:
    def __init__(self):
        self._data = defaultdict(list)

    def add_scores(self, name, point):
        self._data[name].append(point)

    def get_points(self, name):
        return self._data[name]
    

class BaseGame(metaclass=ABCMeta):
    def __init__(self, name, scorer):
        self.__name = name
        self.__scorer = scorer

    def add_scores(self, point):
        self.__scorer.add_scores(self.__name, point)


    @abstractmethod
    def run(self):
        pass
